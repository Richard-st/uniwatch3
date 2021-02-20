from app import app, socketio

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', "Emit from Server", callback=messageReceived)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!') 

def sendMessageToAllCllients():
    socketio.emit('my response', "File Change Detected", callback=messageReceived)