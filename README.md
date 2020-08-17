# Chat-Bot
## This is a Simple ChatBot not Machine learning and stuff involved. 
#### This Bot answers queries related to c++ only
#### This is the Git repository for semester project of CS-114


<!-- ## Setting up the Environment: -->

 ### Installing Python 
 Get Python for your Operating System from the download Page.


 Install and add to PATH. 

 For Windows User This Option is in python setup installation.

 
[Python Download Page](https://www.python.org/downloads/)
* python 3.6.8 or higher
* pip 19.3.1 or higher

### Open Terminal / Bash / CMD / Powershell in the project directory 

### Setting up the virtual environment* 
*Recommended but not required except if some errors in the user base environment

#### Installing virtualenv
>pip install virtualenv

#### Creating new Virtual Environment
In the project Directory
> virtualenv env

#### Activating your Virtual Environment

##### For Windows
> start env\Scripts\activate.bat
#####  For Mac / Linux (Bash / Terminal)
> source env/bin/activate


### Installing Dependencies
> pip install -r requirements.txt 

### Running the app (CLI/TUI)
> python main.py

### Running the app (WEB GUI)
> python web.py


## TUI View of ChatBot Developed in C++
![CPP-Version](/img/chatbot-cppversion.png)

## TUI View of ChatBot Developed in Python
![Python-TUI-Version](/img/tui-chatbot.png)

## WEB GUI View of ChatBot Developed in Python
![Python-GUI-Version](/img/web-chatbot.png)



## Setting up your own Bot

- Create an instance of Bot Class
- Set up your json database file in following format

```
    {
        "synonyms":[
        {"tag":"aoa","keywords":["asalaam","salam","assalaam","asalam"]}
        ],
        "queries":[
            {"name":"quit","match":[["quit"]],"res":["Bye","Good Bye","See you soon","See ya","See you again"]}
        ]
    }
```
- The [synonyms] list shows similar words that means similar so that single word is being used in [queries] list
- In queries Random response form res list is displayed.
- if any of single object in [match] list found in the input, chat bot returns that response.
- the object in [match] list must be a list of words. if all objects in one of the list matches, returns the response.
- the nested queries must be on top if that includes in the query so that correct response is given.
- Example of json format is show in /db/cpp.json file

### Contact
* Email : [huzaifairfan2001@gmail.com](mailto:huzaifairfan2001@gmail.com)
* Facebook : [huzaifairfan2001@facebook](https://www.facebook.com/huzaifairfan2001)


<div>
 CS-114 Semester Project
 <br>
Start : 9 Nov 2019
 <br>
 Completion : 14 Nov 2019
 <br>
 By Huzaifa Irfan
 <br>
 ME-11 (C)
 <br>
 SMME, 
 NUST, Islamabad
 </div>




