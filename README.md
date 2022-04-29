#  1. **sample-flask-htmlx**
Sample flask + htmx implementation 

**Table of contents**
- [1. **sample-flask-htmlx**](#1-sample-flask-htmlx)
  - [1.1. **Prerequisites**](#11-prerequisites)
  - [1.2. **Installation**](#12-installation)
  - [1.3. **Running the application**](#13-running-the-application)


## 1.1. **Prerequisites** 
To get started with the application in the machine

  1. Python3 - Make sure python3 and highr=er is installed on your system before proceeding to installation instructions.
  2. Git - Download and install Git.OSX and linux comes preinstalled with Git. Download and install Git in your windows machine if not installed yet.
  3. Pip - We will use pip to install required packages to be used in the project. 
   

## 1.2. **Installation**
**cloning the repository.**

open terminal or command prompt and enter the following command.

``` 
$ git clone git@github.com:app-generator/sample-flask-htmlx.git

 ```

 or use https:

 ```
 $ git clone https://github.com/app-generator/sample-flask-htmlx.git
 ```

**Installation instructions.**

Create a virtual environment before installing the packages. 

```
$ virtualenv env 

```

Activate the virtual environment

For unix users:

```
$ source env/bin/activate 

```

For windows users:

``` 
C: \Users\username\path to project > env\Scripts\activate 

```

Migrate the database using python console from terminal or command prompt.

``` 
$ python 
```
 or 

```
 $ python3 
```

``` 
>>> from app import create_app,db,models 

>>> db.create_all(app=create_app()) 
```


## 1.3. **Running the application**
With all the bove steps done its time to run the application. The application is run with the command:

```
$ python app.py 

```
or

``` 
$  python3 app.py 

```

Flask server will run on port ``` 5000 ```

open the browser and enter the url ``` http://localhost:5000/ ```
