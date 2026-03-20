# -----------------------------------------------------------------------------
#  Dependency_installer.py
#  Copyright (c) 2024 Asha the Fox 🦊
#  All rights reserved.
#
#  This module provides functions to verify and install the required packages for ATbot.
#  It is intended to be used as a library to support other scripts in the project (mainly AT_bot.py), DO NOT RUN DIRECTLY.
#  
#  Functions:
#      get_package_size(package_name) - Verifies if a package is installed, and if not, get it's estimated size.
#      install_packages(packages_list) - Installs the package list given as parameter.
# -----------------------------------------------------------------------------

__author__ = "Asha Geyon (Natpol50)"
__version__ = 1.1
__all__ = ['get_package_size', 'install_packages', 'install_requirements', 'get_missing_requirements']
__last_revision__ = '2024-11-09'


import subprocess
import logging
import os
import json
import urllib.request
import importlib.util
import sys
import platform
import re

Trans_dic = {
    # A dictionary that maps package names to their corresponding import names.
    # It's necessary because some packages have different names when imported compared to when installed.

    'discord.py': 'discord',
    'Pillow' : 'PIL',
    'windows-curses': 'curses'

}

def is_windows_curses_needed() -> bool:
    """
    Check if windows-curses package is needed on this system.
    Returns True if on Windows and proper curses is not installed.
    """
    if platform.system() != 'Windows':
        return False
    
    try:
        import curses
        # Try to initialize curses to verify it actually works
        try:
            stdscr = curses.initscr()
            curses.endwin()
            return False  # If we get here, curses works properly
        except Exception:
            return True  # Curses exists but doesn't work (likely the dummy module)
    except ImportError:
        return True  # No curses module at all

def get_package_size(package_name: str) -> float:
    """
    Retrieve the size of a package from PyPI. The size is reported in MB.
    Args:
    - package_name (str): The name of the package, version constraint will not be treated.
    Returns:
    - float: Size of the package in MB, or -1 if an error occurred, 0 if already installed.
    """
    # Removes version/operator constraints
    Base_package_name = re.split(r'[<>=!~]', package_name, maxsplit=1)[0].strip()
   
    # Special handling for windows-curses
    if Base_package_name == 'windows-curses':
        if is_windows_curses_needed():
            logging.info("Windows-curses package is required and not properly installed.")
        else:
            logging.info("Proper curses implementation is already available.")
            return 0.0
    else:
        # Map package name to importable module name if available
        if Base_package_name in Trans_dic:
            Importable_module_name = Trans_dic[Base_package_name]
        else:
            Importable_module_name = Base_package_name
       
        # Check if the package is already installed (except for windows-curses)
        if importlib.util.find_spec(Importable_module_name) is not None:
            logging.info(f"Package '{Base_package_name}' is already installed.")
            return 0.0

    try:
        # Fetch package information from PyPI
        url = f"https://pypi.org/pypi/{Base_package_name}/json"
        with urllib.request.urlopen(url) as response:
            Package_info = json.loads(response.read().decode())
            Version = Package_info['info']['version']
            Release_data = Package_info['releases'][Version]
            # Calculate the total size of the package in bytes
            Total_size_bytes = sum(file['size'] for file in Release_data)
           
            del Package_info
            del Version
            del Release_data
            # Convert size to MB
            Total_size_mb = Total_size_bytes / (1024 ** 2)
            logging.info(f"The size of the '{Base_package_name}' package is {Total_size_mb:.2f} MB")
            return Total_size_mb
    except Exception as e:
        logging.warning(f"Error retrieving size for package '{Base_package_name}': {e}")
        return -1.0


def install_packages(pkg_list: list) -> None:
    """
    Install a list of packages using pip.

    Args:
    - pkg_list (list of str): List of library names to be installed.

    Returns:
    - None
    """
    for Pkg in pkg_list:
        try:
            subprocess.check_call(['pip', 'install', Pkg])
            print(f"Successfully installed: {Pkg}")
            logging.info(f"Successfully installed: {Pkg}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing: {Pkg}\nPlease verify if all prerequisites are met. Refer to the wiki for details.")
            logging.critical(f"Error installing '{Pkg}': {e}")
            input('Press Enter to continue...')


def install_requirements(requirements_file: str) -> bool:
    """
    Install dependencies from a requirements file using pip.

    Args:
    - requirements_file (str): Path to the requirements file.

    Returns:
    - bool: True if installation succeeded, False otherwise.
    """
    if not os.path.exists(requirements_file):
        logging.critical(f"Requirements file not found: {requirements_file}")
        print(f"Requirements file not found: {requirements_file}")
        return False

    try:
        subprocess.check_call(['pip', 'install', '-r', requirements_file])
        logging.info(f"Successfully installed dependencies from: {requirements_file}")
        print(f"Successfully installed dependencies from: {requirements_file}")
        return True
    except subprocess.CalledProcessError as e:
        logging.critical(f"Error installing dependencies from '{requirements_file}': {e}")
        print("Error installing dependencies from requirements file.")
        return False


def _requirement_applies_to_current_platform(line: str) -> bool:
    """
    Best-effort marker support for requirements lines using platform_system.
    """
    if ';' not in line:
        return True

    marker = line.split(';', 1)[1].strip().lower()
    system_name = platform.system().lower()

    if "platform_system" not in marker:
        return True

    if "==" in marker:
        target = marker.split("==", 1)[1].strip().strip("\"'")
        return system_name == target.lower()
    if "!=" in marker:
        target = marker.split("!=", 1)[1].strip().strip("\"'")
        return system_name != target.lower()

    return True


def _parse_requirements_file(requirements_file: str) -> list[str]:
    """
    Parse a requirements file and return applicable requirement entries.
    """
    Parsed_requirements: list[str] = []

    with open(requirements_file, 'r', encoding='utf-8') as req_file:
        for Raw_line in req_file:
            Line = Raw_line.strip()
            if not Line or Line.startswith('#'):
                continue
            if Line.startswith('-r') or Line.startswith('--requirement'):
                continue

            # Remove inline comments
            if ' #' in Line:
                Line = Line.split(' #', 1)[0].strip()

            if not _requirement_applies_to_current_platform(Line):
                continue

            Requirement_entry = Line.split(';', 1)[0].strip()
            if Requirement_entry:
                Parsed_requirements.append(Requirement_entry)

    return Parsed_requirements


def get_missing_requirements(requirements_file: str) -> tuple[list[str], float, list[str]]:
    """
    Return missing dependencies from a requirements file.

    Returns:
    - missing_requirements (list[str]): Requirements that appear missing.
    - total_size_mb (float): Estimated total download size in MB for missing requirements.
    - unresolved_requirements (list[str]): Requirements for which size/state could not be resolved.
    """
    Missing_requirements: list[str] = []
    Unresolved_requirements: list[str] = []
    Total_size_mb = 0.0

    if not os.path.exists(requirements_file):
        logging.warning(f"Requirements file not found while scanning missing deps: {requirements_file}")
        return Missing_requirements, Total_size_mb, Unresolved_requirements

    for Requirement in _parse_requirements_file(requirements_file):
        Dep_size = get_package_size(Requirement)
        if Dep_size > 0:
            Missing_requirements.append(Requirement)
            Total_size_mb += Dep_size
        elif Dep_size == -1:
            Unresolved_requirements.append(Requirement)

    return Missing_requirements, Total_size_mb, Unresolved_requirements

if __name__ == "__main__":
    print("This is a library module and is not intended to be run directly, please use AT_bot.py .")