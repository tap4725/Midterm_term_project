This project folder contains:
i) datasets in data folder.
ii) report in jupyter-notebook
iii) PDF of same report.
iv) source.py containing the apriori class module and cli in wrapped in **main**
v) tap47.ipynb containing part 4 of the project which compares the algorithm to external packages.
vi) **init**.py
vii) README.txt

CLI:

A virtual environment is RECOMMENDED to run the project.

1. in order to run the interface for apriori algorithm first install the requirements which are listed in requirements.txt using cmd.

Command: pip install -r requirements.txt

2. run the source.py for interactive cli.

Command: python source.py

NOTE: with low min_sup or low min_conf, you may get runtime warnings, which are not errors. code will generate the output but may take more time to generate.
