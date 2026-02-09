## Requirements
Python 3.12.3

### Packages/Frameworks

pytest 9.0.2

numpy 2.4.2

## Setup

### Step 1: Create virtual environment
**Only necessary to isolate packages from other environments. As long as both pytest and numpy are installed, scripts should work**
```
python3 -m venv venv_name --system-site-packages
```

### Step 2: Activate virtual environent
```
source venv_name/bin/activate
```

### Step 3: Install pytest & numpy
```
python3 -m pip install pytest
pip install numpy
```

## How To Execute Tests

### Step 1: From the cs4300 repository navigate into homework1 directory

```
cd homework1/
```


### Step 2: Execute tests by running pytest, configuration is pre-defined by the pyproject.toml file.

```
pytest
```

## How To Execute Code

### Step 1: From the cs4300 repository navigate into homework1 directory
**All scripts assume they are run from the homework1/ directory. This is relavent for task6.py which accesses a file 1 level from it's directory. If the file is executed from the src directory it will not execute properly.**

```
cd homework1/
```

### Step 2: Execute tasks 1 to 7 using python 3

``` 
python3 src/task1.py
python3 src/task2.py 
python3 src/task3.py 
python3 src/task4.py 
python3 src/task5.py 
python3 src/task6.py 
python3 src/task7.py 
```
