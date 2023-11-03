import typer
from typing import Optional
import csv
from zipfile import ZipFile


def main(csv_file: typer.FileText, placeholder_txt_file: typer.FileText, zip_filename: Optional[str] = typer.Argument(None)):
    """
Generates text files based on a template text file and data in a CSV file.
The template contains placeholders that correspond to the columns of the 
CSV. Rows of the CSV correspond to the textfiles generated.

e.g.

---template with placeholders---\n
Dear [firstname],\n
    Your order number is [order].\n
---template with placeholders---\n
\n
---csv---\n
id,firstname,order\n
A.txt,Betty,1\n
B.txt,Carl,2\n
---csv---\n
\n
would result in a zip file containing:\n
\n
    ---A.txt---\n
Dear Betty,\n
    Your order number is 1.\n
---A.txt---\n
\n
and\n
\n
    ---B.txt---\n
Dear Carl,\n
    Your order number is 2.\n
---B.txt---\n
\n
For custom filenames, use the first column of the CSV to specify filenames with a column header of 'id'.
    """
    if zip_filename is None:
        zip_filename = "output.zip"

    # prepare files
    datafile = open(csv_file.name, 'r')
    placeholderfile = open(placeholder_txt_file.name, 'r')
    ptext = placeholderfile.read()
    reader = csv.DictReader(datafile)
    zip = ZipFile(zip_filename, 'w')
    
    # rows of csv 
    for filenum,row in enumerate(reader):
        # if first col is 'id', use col for filenames
        if list(row.keys())[0] == 'id':
            filename = f"{row['id']}"
        # otherwise use row numbers for filenames
        else:
            filename = f"{filenum}.txt"
        
        # find/replace any placeholders
        buffer = ptext
        for key,value in row.items():
            buffer = buffer.replace(f'[{key}]',value)
        zip.writestr(filename, buffer)

if __name__ == "__main__":
    typer.run(main)
