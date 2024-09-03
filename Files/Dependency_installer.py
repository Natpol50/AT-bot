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
__version__ = 1.0
__all__ = ['get_package_size', 'install_packages']


import subprocess
import logging
import os
import json
import urllib.request
import importlib.util


Trans_dic = {
    # A dictionary that maps package names to their corresponding import names.
    # It's necessary because some packages have different names when imported compared to when installed.

    'discord.py': 'discord',
    'Pillow' : 'PIL',
    'windows-curses': 'curses'

}

def get_package_size(package_name):
    """
    Retrieve the size of a package from PyPI. The size is reported in MB.

    Args:
    - package_name (str): The name of the package, version constraint will not be treated.

    Returns:
    - float: Size of the package in MB, or -1 if an error occurred, 0 of already installed.
    """
    # Removes the package version constraint ( honestly, it's because i don't really know how to verfiy with a specific version.)
    base_package_name = package_name.split('==')[0]
    
    # Map package name to importable module name if available
    if base_package_name in Trans_dic :
        importable_module_name = Trans_dic[base_package_name]
    else :
        importable_module_name = base_package_name
    
    # Check if the package is already installed
    if importlib.util.find_spec(importable_module_name) is not None:
        logging.info(f"Package '{base_package_name}' is already installed.")
        return 0.0

    try:
        # Fetch package information from PyPI
        url = f"https://pypi.org/pypi/{base_package_name}/json"
        with urllib.request.urlopen(url) as response:
            package_info = json.loads(response.read().decode())
            version = package_info['info']['version']
            release_data = package_info['releases'][version]

            # Calculate the total size of the package in bytes
            total_size_bytes = sum(file['size'] for file in release_data)

            # Convert size to MB
            total_size_mb = total_size_bytes / (1024 ** 2)

            logging.info(f"The size of the '{base_package_name}' package is {total_size_mb:.2f} MB")
            return total_size_mb
    except Exception as e:
        logging.warning(f"Error retrieving size for package '{base_package_name}': {e}")
        return -1.0


def install_packages(pkg_list):
    """
    Install a list of packages using pip.

    Args:
        lib_list (list of str): List of library names to be installed.
    """
    for pkg in pkg_list:
        try:
            subprocess.check_call(['pip', 'install', pkg])
            print(f"Successfully installed: {pkg}")
            logging.info(f"Successfully installed: {pkg}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing: {pkg}\nPlease verify if all prerequisites are met. Refer to the wiki for details.")
            logging.critical(f"Error installing '{pkg}': {e}")
            input('Press Enter to continue...')

if __name__ == "__main__":
    print("This is a library module and is not intended to be run directly, please use AT_bot.py .")