# SG Assessment

## Description
Data Analysis Assessment for SG the **Data Scientist** role.

## Tech
* Python 3.9
* Conda 22.9.0
* Jupyter

## Tools
* IDE: Visual Studio Code


## How to run
 
 1. clone Repo
 2. Create conda environment
 ```
    conda env create -f environment.yml
 ```
 3. Run data_preprocessing.py file
 ```
    python data_preprocessing.py
 ```
 4. Run each notebook either using Jupyter Lab or from command line:
 ```
    cd notebooks
    ipython -c "%run part1.ipynb"
```

## Folder Structure

```
├── ...
├── data_preprocessing.py               # file that will preprocess the raw dataset that is given as input    
├── data            
│   ├── assignment_preprocessed.csv     # dataset after being preprocessed in data_preprocessing.py
│   └── assignment_rev2.csv             # raw dataset
├── notebooks                           # jupyter notebooks - one for each assignment part
│   ├── part1.ipynb     
│   ├── part2.ipynb
│   ├── part3.ipynb 
│   └── statistics_visualization.ipynb  # jupyter notebook with some basic stats from the preprocessed dataset

```