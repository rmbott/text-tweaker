# text-tweaker
Generates text files based on a template text file and data in a CSV file. The template contains placeholders that correspond to the columns of the CSV. Rows of the CSV correspond to the textfiles generated.

---
**Installation**

move to a folder where you like to keep projects, then clone the repo with:

// clone repo

git clone https://github.com/rmbott/text-tweaker.git

cd text-tweaker


// install poetry (to handle dependencies)

curl -sSL https://install.python-poetry.org | python3 -

// add poetry to your PATH 

(see https://python-poetry.org/docs/ for your OS) 

// run the following to make poetry install project dependencies

poetry install

---

**Usage**

// In the project folder, run the following to drop into the virtual environment where the project dependencies were installed

poetry shell

// run the program

python3 main.py --help
