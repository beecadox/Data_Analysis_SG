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
 2. Examples of running the scripts: 
 default [raw data to be preprocessed + part1]:
```
python main.py
python main.py --no-preprocess --part 1
```
[preprocessed data + another part]
```
python main.py --preprocess --part 3
```

## Folder Structure

```
app
├── ...
├── __init__.py     
├── main.py                 # main RESTful API File - on startup event
├── config.py               # FastAPI Settings
├── data
│    └── data               # our 'data' in the form of a yaml file
├── routes             
│   ├── __init__.py     
│   └── api.py              # APIRouter file for endpoints
├── src             
│   ├── endpoints           # contains all our endpoints
│   │   ├── __init__.py       
│   │   ├── attribute.py    
│   │   ├── datatype.py 
│   │   ├── mo_class.py 
│   │   └── random.py
│   ├── models              # contains our Pydantic Models
│   │   ├── __init__.py       
│   │   └── managed_objects.py 
│   ├── utils               # some utils used 
│   │   ├── __init__.py       
│   │   ├── regex.py        # for regex matching
│   │   └── data.py         # data initilization
```