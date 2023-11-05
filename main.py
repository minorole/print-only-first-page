'''
ReadME

A simple Python script to batch print PDF files located in a specified folder. Users have the option to print only the first page or the entire document of all PDFs within the folder.

Prerequisites
Python 3.x

PyPDF2 library (version 3.0.0 or newer). You can install it using pip:

Copy code
pip install PyPDF2
How to Use
Navigate to the folder containing the script in a terminal or command prompt.

Run the script using the command:

Copy code
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

'''








import os
import PyPDF2

def print_pdfs_in_folder(folder_path, pages_to_print="all"):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)

            if pages_to_print == "first":
                # Extract the first page and save it to a temporary PDF
                with open(pdf_path, "rb") as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    writer = PyPDF2.PdfWriter()
                    writer.add_page(reader.pages[0])  # Changed to add_page

                    temp_pdf_path = os.path.join(folder_path, "temp_first_page.pdf")
                    with open(temp_pdf_path, "wb") as output_pdf_file:
                        writer.write(output_pdf_file)

                    # Print the temporary PDF
                    os.system(f"lpr {temp_pdf_path}")

                    # Remove the temporary PDF
                    os.remove(temp_pdf_path)
            else:
                # Print the entire PDF
                os.system(f"lpr {pdf_path}")


folder_path = input("Enter the path to the folder containing PDFs: ")

if not os.path.exists(folder_path):
    print("Folder doesn't exist. Exiting...")
    exit()

print_option = input("Do you want to print all the PDFs in this folder? (yes/no): ").strip().lower()
if print_option == "yes":
    pages_option = input("Do you want to print only the first page or the whole document? (first/whole): ").strip().lower()

    if pages_option == "first":
        print_pdfs_in_folder(folder_path, "first")
    elif pages_option == "whole":
        print_pdfs_in_folder(folder_path, "whole")
    else:
        print("Invalid option. Exiting...")
else:
    print("Exiting...")
