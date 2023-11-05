# print-only-first-page
this python script will print only the first page of all the pdfs under a folder under Mac OS

ReadME

A simple Python script to batch print PDF files located in a specified folder. Users have the option to print only the first page or the entire document of all PDFs within the folder.

Prerequisites
Python 3.x

PyPDF2 library (version 3.0.0 or newer). 

You can install it using pip:

pip install PyPDF2

How to Use
Navigate to the folder containing the script in a terminal or command prompt.

Run the script using the command:

python3 your_script_name.py

Replace your_script_name.py with the actual name of the script if you've named it differently.

Follow the on-screen prompts:

Enter the path to the folder containing the PDFs.
Choose whether you want to print the PDFs.
If you decide to print, specify whether you want to print only the first page or the entire document.
Features
Batch Printing: The script allows for automated printing of multiple PDFs without manual intervention.
Selective Printing: Users can opt to print only the first page of each PDF, useful for preview or cover-page printing.
User-friendly Prompts: Guided prompts ensure users know what options they're selecting.
Notes
The script uses the lpr command, making it tailored for macOS and UNIX-like systems. Adjustments might be needed for other operating systems.
Temporary files (temp_first_page.pdf) are created in the process but are deleted immediately after printing.
Future Enhancements
Support for other operating systems.
Options to select page ranges (e.g., print pages 1-3).
Enhanced error handling and logging capabilities.
