import psutil
import time
from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO
import pandas as pd
import numpy as np

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
 
def background_thread():
    count = 0
    while True:
        i=0
        df = pd.read_csv('../falsk.csv')
        df2 = np.array(df)#np.ndarray()
        df=df2.tolist()#list
        while i<5:
            socketio.sleep(1)
            count += 1
            t = time.strftime('%M:%S', time.localtime())        
            label=df[i][0]
            temp=df[i][1]
            ECG=df[i][2]
            socketio.emit('server_response',{'data': [t, temp,label,ECG], 'count': count},namespace='/test')
            i=i+1
 
 
@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)
 
@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)
 
if __name__ == '__main__':
    socketio.run(app, debug=True)