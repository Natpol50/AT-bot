import subprocess
import logging

# Function to install libraries
def libraries(lib_list):
    for lib in lib_list:
        try:
            subprocess.check_call(['pip', 'install', lib])
            print(f"Successfully installed: {lib}")
            logging.info(f"Successfully installed: {lib}")
        except subprocess.CalledProcessError:
            print(f"Error installing: {lib}")
            logging.critical(f"Error installing: {lib}")

