import os
import pkg_resources
import sys
import subprocess
import folder_paths

supported_LLava_extensions = set(['.gguf'])

try:
    folder_paths.folder_names_and_paths["joytag"] = (folder_paths.folder_names_and_paths["joytag"][0], supported_LLava_extensions)
except:
    # check if joytag exists otherwise create
    if not os.path.isdir(os.path.join(folder_paths.models_dir, "joytag")):
        os.mkdir(os.path.join(folder_paths.models_dir, "joytag"))
        
    folder_paths.folder_names_and_paths["joytag"] = ([os.path.join(folder_paths.models_dir, "joytag")], supported_LLava_extensions)

# Define the check_requirements_installed function here or import it
def check_requirements_installed(requirements_path):
    with open(requirements_path, 'r') as f:
        requirements = [pkg_resources.Requirement.parse(line.strip()) for line in f if line.strip()]

    installed_packages = {pkg.key: pkg for pkg in pkg_resources.working_set}
    installed_packages_set = set(installed_packages.keys())
    missing_packages = []
    for requirement in requirements:
        if requirement.key not in installed_packages_set or not installed_packages[requirement.key] in requirement:
            missing_packages.append(str(requirement))

    if missing_packages:
        print(f"Missing or outdated packages: {', '.join(missing_packages)}")
        print("Installing/Updating missing packages...")
        subprocess.check_call([sys.executable, '-s', '-m', 'pip', 'install', *missing_packages])
    else:
        print("All packages from requirements.txt are installed and up to date.")

requirements_path  = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")
check_requirements_installed(requirements_path)


from .nodes.joytag import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

