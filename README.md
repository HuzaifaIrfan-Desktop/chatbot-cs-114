<div align="center">
  <h1>ChatBot-CS-114</h1>
  <p><h3 align="center">CLI and WEB SocketIO Based Chatbot that answer queries related in database 🚀</h3>
  </p>
</div>

[Project Template](<Project Template.pdf>)
&nbsp;&nbsp;•&nbsp;&nbsp;
[Final Report](<ME11C_Group3 Chat Bot IEEE Report.pdf>)
&nbsp;&nbsp;•&nbsp;&nbsp;
[C++ Version](<c++ version>)
&nbsp;&nbsp;•&nbsp;&nbsp;


<hr>



## Specs
- Python CLI Chatbot
- Answer Queries in db file (related to c++ included)
- web based interface
- c++ version



### TUI View of ChatBot Developed in C++
![CPP-Version](/img/chatbot-cppversion.png)

### TUI View of ChatBot Developed in Python
![Python-TUI-Version](/img/tui-chatbot.png)

### WEB GUI View of ChatBot Developed in Python
![Python-GUI-Version](/img/web-chatbot.png)



## Libraries
- socketio
- flask
- nltk


# 🚀 Usage





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
```bash
pip install virtualenv
```



#### Creating new Virtual Environment
In the project Directory
```bash
virtualenv env
```

#### Activating your Virtual Environment

##### For Windows
```bash
start env\Scripts\activate.bat
```

#####  For Mac / Linux (Bash / Terminal)
```bash
source env/bin/activate
```

### Installing Dependencies
```bash
pip install -r requirements.txt 
```

### Running the app (CLI/TUI)
```bash
python main.py
```


### Running the app (WEB GUI)
```bash
python web.py
```







## Info

 CS-114 (Fundamentals of Programming) Semester Project 
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



## Setting up your own Bot

- Create an instance of Bot Class
- Set up your json database file in following format

```json
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






# 📝 Documentation

# 📚 References


# 🤝🏻 Connect with Me

[![GitHub](https://img.shields.io/badge/Github-%23222.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HuzaifaIrfan/)
[![Website](https://img.shields.io/badge/Website-%23222.svg?style=for-the-badge&logo=google-chrome&logoColor==%234285F4)](https://www.huzaifairfan.com)

# 📜 License

Licensed under the GPL3 License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)

Last Updated on 2019-11-14
