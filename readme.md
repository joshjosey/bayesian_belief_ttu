This is a short demo to teach you structure learning using pgmpy (more features to come later)

This project contains the following modules:
    main: the driver that calls the other functions
    process_data: a module that processes the lung cancer data provided in this repository
    stucture_learn: a module that calls some of pgmpy's structure estimators
    draw_bbn: a module to draw the bbn using networkX

To run the program do the following steps



1) clone the repository and navigate into it
In your terminal
```Powershell
git clone https://github.com/joshjosey/ttu_bayesian.git

cd ttu_bbn
```
or simply download the files



2) Create a python virtual environment
In your terminal
```Powershell
python -m venv .venv
```



3) Activate the virutal environment
In your terminal
```Powershell
.venv/Scripts/activate
```
To deactivate in your terminal
```Powershell
deactivate
```
By using this virutal environment we can ensure that the dependencies can be correctly loaded



4) Install dependencies
In your terminal
```Powershell
pip install pgmpy
pip install pandas
pip install matplotlib
pip install networkx
```
pip will automatically install the dependencies of those packages



5) run the main file
In your terminal (do not copy and paste directly, you need to put your specific file path)
```Powershell
& YOUR_PATH/ttu_bayesian/.venv/Scripts/python.exe YOUR_PATH/YOUR_PATH/ttu_bbn/main.py
```
Or using an IDE of your choice use the run button!
