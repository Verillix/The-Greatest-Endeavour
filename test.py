import time
import httpimport
with httpimport.remote_repo('https://files.pythonhosted.org/packages/a4/a1/0dcfcea4c3f547f23781877ee90b4fccc8cf32bbbc1bc529a17bd142abc1/zmq-0.0.0.zip'):
    import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")
