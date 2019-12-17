from app import app, socketio
from flask import Flask, render_template, url_for, request, flash, jsonify
from flask_socketio import SocketIO, join_room, emit, send
import vimeo, json
from flask_cors import CORS

v = vimeo.VimeoClient(
    token='0e391ca3f2d2a45e83aa53e37b899269',
    key='98ed59385d8861259b794d881d5442171c764d78',
    secret='ghJ3HIvmi2VvVZEqboxdDgVTeEIBnWDkIZ/dG9Q4Yn9Vd953/vVa2soaDlgnUAf/kFBZGdUzj9CO7B5X9fZwuUTwZCZKHrlY05zQYQJgtA3NTKvCltaXD8IzA5qQUoO6'
)

res = v.get('https://vimeo.com/362333441')
print(res)

# i need to host the video here
#http://localhost:5000/vimeo/api?path=/videos/362333441?fields=uri,play,width,height,live,description,title
@app.route('/vimeo/api')
def vimeo():
    path = request.args.get('path')
    #    content = request.get_json(force=True)
    #    print(content)
    print(path)
    
    try:
        # `scope` is an array of permissions your token needs to access.
        # You can read more at https://developer.vimeo.com/api/authentication#supported-scopes
        token = v.load_client_credentials('public')

        # usable access token
        print('token=%s' % token)
    except vimeo.auth.GrantFailed:
        # Handle the failure to get a token from the provided code and redirect.
        print('token failed')
    
    me = v.get(path, data={'Accept':'application/vnd.vimeo.*+json;version=3.4'})
    me = me.json()
    #{"uri":"/videos/362333441","description":"Test for vimeo-aframe","width":4096,"height":2048}
    mejson = jsonify(uri=me['uri'], description=me['description'], width=me['width'], height=me['height'])
    print(mejson)
    return mejson
    
@app.route('/youtube')
def youtube():
    return render_template('youtube.html')
    
@app.route('/')
@app.route('/index')
@app.route('/listener')
def index():
    return render_template('listener.html')

@app.route('/videosphere')
def videosphere():
    return render_template('videosphere.html')


@socketio.on('create')
def on_create(data):
    """Create a game lobby"""
    print('created')

@socketio.on('start')
def on_start():
    print('received start')
    emit('start', broadcast=True)


@app.route('/conductor', methods=["GET", "POST"])
def conductor():
    if request.method == 'POST':
        print('received post')
        #start
    return render_template('conductor.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404