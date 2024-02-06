import PyPDF2
from sys import argv, exit
from os import path, mkdir

try:
    dest = argv[1]
    input_paths = argv[2:]
except IndexError:
    exit("Please specify your destination directory followed by pdf file paths...")

merger = PyPDF2.PdfFileMerger()
for file_path in input_paths:
    merger.append(file_path)

if not path.exists(dest):
    mkdir(dest)

merger.write(path.join(dest, 'merged.pdf'))
print("Successfully merged pdf files!")