import glob
import os

def counts(path="."):
    file_extension_counts = {}
    for file in glob.iglob(os.path.join(path,"*")):
        if os.path.isfile(file):
            if os.path.basename(file).find(".") == -1:
                extension = ""
            else:
                extension = os.path.basename(file).split(".").pop()
            if extension not in file_extension_counts:
                file_extension_counts[extension] = 1
            else:
                file_extension_counts[extension] += 1
    return file_extension_counts
        
if __name__ == "__main__":
    extension_count = counts(".")
    print(os.getcwd())
    print(extension_count)
    