import subprocess
import logging
import os
import json
import urllib.request
import importlib.util


Trans_dic = {
    'discord.py': 'discord',
    'Pillow' : 'PIL',
    'windows-curses': 'curses'
}
def get_package_size(package_name): # Isn't it better to know the size of what you'll install ?
    package_name = package_name.split('==')[0]
    if package_name in Trans_dic.keys() :
        package_import = Trans_dic[package_name]
    else :
        package_import = package_name

    if importlib.util.find_spec(package_import) is not None: # First, verify if package is present
        return 0
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        with urllib.request.urlopen(url) as response:
            package_info = json.loads(response.read().decode())
            version = package_info['info']['version']
            release_data = package_info['releases'][version]
            total_size = sum(file['size'] for file in release_data)
            
            # Reconverting the size to MB
            total_size = total_size / (1024 ** 2)
            logging.info(f"The size for the {package_info} package is {total_size} MB")
            return total_size
    except Exception as e:
        logging.warning(f"Error retrieving size for {package_name}: {e}")
        return -1
    


def libraries(lib_list):  # A small function to install the required libraries
    for lib in lib_list:
        try:
            subprocess.check_call(['pip', 'install', lib])
            print(f"Successfully installed: {lib}")
            logging.info(f"Successfully installed: {lib}")
        except subprocess.CalledProcessError as E:
            print(f"There was an error installing: {lib} \n Please verify if all prerequisites are met. To do so, refer to the wiki.")
            input('Press enter to continue...')
            logging.critical(f"Error installing: {lib}, reason : {E} ")

