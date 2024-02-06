# pdf-merger
## Purpose
A simple command line script that can merge multiple pdf files together into a single pdf file. Helpful for those who would like to quickly combine files for emails, jobs applications, assignments, etc., without having to use clunky web services or download heavy software.

## Usage
Open the terminal, navigate to directory containing this script, and run
```
python3 merge_pdf.py /your/destination/directory/ /your/pdf/path1.pdf/ /yourpdf/path2.pdf/ ...
```
Note that the destination directory can either already exist or be created automatically using the script.

## Dependencies
- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/)
