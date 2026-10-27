Build Your First Python + FastAPI Backend on Windows — Step by Step
We're going to create an Employee Management API from scratch on your computer, run it locally, and test it through Postman.

By the end, you'll have four working operations:
Method	API	Purpose
GET	/employees	Get all employees
GET	/employees/101	Get employee by ID
POST	/employees	Add an employee
PUT	/employees/101	Update an employee
DELETE	/employees/101	Delete an employee

We'll use your existing Python 3.12.5 installation. MongoDB isn't needed yet; we'll store employees in a Python dictionary.
Step 1 — Verify Python is installed
Open Windows Command Prompt (Win + R → type cmd → Enter).

Run:
python --version


You previously got:
Python 3.12.5


Now run:
py -3.12 --version


Expected:
Python 3.12.5


Step 1 complete: Python 3.12 is available on your computer.

You do not need to uninstall Python 3.14.2.
Step 2 — Open VS Code
If you already have VS Code, open it. Otherwise, install it from the official VS Code website.

Inside VS Code:
1. Open the Extensions panel using Ctrl + Shift + X.
2. Search for Python.
3. Install the Python extension published by Microsoft.
This provides Python syntax support, debugging, autocomplete, and interpreter selection. 
Visual Studio Code

Step 3 — Create your project folder
Go back to Command Prompt and run:
cd /d %USERPROFILE%
mkdir employee-api
cd employee-api


Your terminal should now look similar to:
C:\Users\vaish\employee-api>


This is the folder where your backend code will live.

Now open this folder in VS Code:

File → Open Folder → employee-api → Select Folder
Step 4 — Open the VS Code terminal
Inside VS Code, select:

Terminal → New Terminal

VS Code may open PowerShell by default. To follow these instructions exactly, select Command Prompt:
1. Click the dropdown arrow next to the + button in the terminal panel.
2. Select Command Prompt.
3. Confirm that it shows the employee-api folder.
Your prompt should look approximately like:
C:\Users\vaish\employee-api>


Step 5 — Create a virtual environment
In the project terminal, run:
py -3.12 -m venv .venv


What does this command do?
- py -3.12 selects Python 3.12.
- -m venv runs Python's virtual environment creation module.
- .venv is the folder where the environment is created.
VS Code should now show:
employee-api/
└── .venv/


This environment has its own Python executable and package installation location. 
Python 3.12.16 documentation

Step 6 — Activate the virtual environment
In the same Command Prompt terminal, run:
.venv\Scripts\activate.bat


Your terminal should change to:
(.venv) C:\Users\vaish\employee-api>


The (.venv) prefix indicates the environment is active.

Now verify:
python --version


Expected:
Python 3.12.5


Run:
where python


The first path should point inside your project, similar to:
C:\Users\vaish\employee-api\.venv\Scripts\python.exe


This confirms that your terminal is using the virtual environment's Python.

In VS Code, also press Ctrl + Shift + P, choose Python: Select Interpreter, and select the interpreter from employee-api\.venv\Scripts\python.exe. This keeps the editor and project environment consistent. 
Visual Studio Code
