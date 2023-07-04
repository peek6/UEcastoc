# Python script to fix the paths in the manifest file generated by UECASTOC so that UECASTOC can pack the files.
# This script should be installed and run from the "cpp" directory of a UECASTOC ( https://github.com/gitMenv/UEcastoc/tags ) installation

# Caveats:
#  - The filenames in each mod must be unique.  In other words, a specific mod should not have files with the same name in different folders.
#  - Mod names should not have spaces or other strange characters (like /, \, or . )

# Usage:
#   - Download UECASTOC from https://github.com/gitMenv/UEcastoc/tags
#   - Copy this script into the cpp directory
#   - Point the manifest_file variable below to the manifest file generated by UECASTOC when you unpacked
#   - Point directory_to_pak to the directory you want to pack
#   - The directory structure should be the usual structure we are used to from before IoStore (e.g., as used by FluffyQuack's UnrealPak scripts).
#       For example, for Hogwarts Legacy, it should be z_your_mod_name_P\phoenix\Content\...  and you would then set directory_to_pak = 'z_your_mod_name_P'
#   - Run the script
#   - The script will attempt to find the files in the directory you want to pack, fix the manifest accordingly, and pack the files into packed/...

import os
import json
import pathlib
import shutil
from fix_manifest_and_pack_utils import fix_manifest_and_pack_iostore

##### SET THESE TO POINT TO YOUR MANIFEST FILE AND TO THE DIRECTORY YOU WANT TO PACK ###########
user_manifest_file = 'test_manifest.json'
user_manifest_dir = '.'
user_directory_to_pak = 'z_your_mod_name_P'
uecastoc_executable_path = '.'  # dir with uecastoc main.exe and castoc_x64.dll
#########################################################################################

def main():
    fix_manifest_and_pack_iostore(user_directory_to_pak, user_manifest_file, user_manifest_dir, uecastoc_executable_path)

main()



