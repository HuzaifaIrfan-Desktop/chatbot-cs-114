#!/usr/bin/env python
from cpp_bot import cpp_bot
from colorama import Fore
import random
import json


from flask import Flask, render_template, session, request,jsonify, send_from_directory, \
copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
import datetime



port=3098

def time():
    now = f"{datetime.datetime.now()}"
    return now



users={}
logs=[]



async_mode = None

app = Flask(__name__, static_url_path='')
import logging
logss = logging.getLogger('werkzeug')
logss.disabled = True

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/public/<path:path>')
def send_file(path):
    #print(path)
    return send_from_directory('public', path)

@app.route('/')
def index():
    return send_from_directory('public', "index.html")
    # return render_template('index.html', async_mode=socketio.async_mode)


@app.route('/log')
def logf():
    return jsonify(logs)

@app.route('/obj')
def objf():
    tempobj=users.copy()
    templst=tempobj.values()
    lst=[]
    for temp in templst:
        temp["bot"]=None
        lst.append(temp)
    return jsonify(lst)



@socketio.on('sendinp', namespace='/app')
def gotinp(inp):
    res="NF"
    user=users[request.sid]
    bot=user["bot"]
    bot.reset()
    bot.setinput(inp)
    bot.tokenize()
    bot.similartokens()
    bot.searchresponse()
    res=bot.getanswer()



    query={"input":inp,"response":res,"time":time()}
    user["queries"].append(query)

    emit("response",res)
    log=f"id: '{request.sid}', name: '{user['username']}', input: '{inp}', response: '{res}', time: '{time()}' "
    logs.append(log)
    print(log)




@socketio.on('Connection', namespace='/app')
def Connection(username):
    users[request.sid]={}
    user=users[request.sid]
    user["sid"]=request.sid
    user["username"]=username
    user["queries"]=[]
    user["connection"]="connected"
    user["connectiontime"]=time()
    user["bot"]=cpp_bot();
    bot=user["bot"]
    bot.setup()
    log=request.sid +" " +username + " Connected "+ time()
    logs.append(log)
    print(log)








@socketio.on('disconnect', namespace='/app')
def disconnect():
    user=users[request.sid]
    username=user["username"]
    user["connection"]="disconnected"
    user["disconnectiontime"]=time()
    log=request.sid +" " +username + " Disconnected " +time()
    logs.append(log)
    print(log)
    #print(users)




if __name__ == '__main__':
    log="Web Server started on port "+f"{port}"+" at :"+time()
    logs.append(log)
    print(log)
    socketio.run(app,host='0.0.0.0', port=port, debug=False)
