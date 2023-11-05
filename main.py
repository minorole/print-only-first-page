
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
