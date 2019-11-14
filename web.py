#!/usr/bin/env python
from cpp_bot import cpp_bot
from colorama import Fore
import random


from flask import Flask, render_template, session, request, send_from_directory, \
copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
import datetime





def time():
    now = f"{datetime.datetime.now()}"
    return now

print("Web Server started on :",time())

users={}



async_mode = None

app = Flask(__name__, static_url_path='')
import logging
log = logging.getLogger('werkzeug')
log.disabled = True

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
    print(f"id: '{request.sid}', name: '{user['username']}', input: '{inp}', response: '{res}', time: '{time()}' ")




@socketio.on('Connection', namespace='/app')
def Connection(username):
    users[request.sid]={}
    user=users[request.sid]
    user["username"]=username
    user["queries"]=[]
    user["connection"]="connected"
    user["connectiontime"]=time()
    user["bot"]=cpp_bot();
    bot=user["bot"]
    bot.setup()
    print(request.sid +" " +username + " Connected", time())








@socketio.on('disconnect', namespace='/app')
def disconnect():
    user=users[request.sid]
    username=user["username"]
    user["connection"]="disconnected"
    user["disconnectiontime"]=time()
    print(request.sid +" " +username + " Disconnected" , time())




if __name__ == '__main__':
    socketio.run(app, port=3098, debug=False)
