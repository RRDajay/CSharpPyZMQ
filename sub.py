# simple_sub.py
import zmq

def recv():
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://127.0.0.1:5556')
    subscriber.setsockopt(zmq.SUBSCRIBE, b'')
    while True:
        print(subscriber.recv())

recv()
