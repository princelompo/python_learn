# Terminal emulator for Python

# execute the ls command and print the output

import subprocess
import os
import sys
import pathlib

def run(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        return output
    except subprocess.CalledProcessError as e:
        error_output = e.stderr.decode('utf-8')
        return f"An error occurred: {error_output}"

def search_all(extention):
    #search for all files with the given extension in all the home directories
    home_dir = pathlib.Path.home()
    files = []
    for root, dirs, filenames in os.walk(home_dir):
        for filename in filenames:
            if filename.endswith(extention):
                files.append(os.path.join(root, filename))
    return files

if __name__ == "__main__":
    # out1 = run("ls")
    # print(out1)

    out2 = search_all(".java")
    print("Searching for .java files in home directory....\n")
    for file in out2:
        print(f"=> {file} size: {os.path.getsize(file)} bytes")
    print("\nSearch completed.")
    print(f"\nTotal .java files found: {len(out2)}")

    max = max([os.path.getsize(file) for file in out2]) if out2 else 0
    min = min([os.path.getsize(file) for file in out2]) if out2 else 0

    for file in out2:
        if os.path.getsize(file) == max:
            print(f"\n Max size file : {file} size: {os.path.getsize(file)} bytes")
    for file in out2:
        if os.path.getsize(file) == min:
            print(f"\n Min size file : {file} size: {os.path.getsize(file)} bytes")



