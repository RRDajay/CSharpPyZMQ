import zmq, json, time

def send():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.connect("tcp://localhost:5555")
    while True:
        publisher.send_string( "hello world" )
        time.sleep(1)

send()

