# CSharpPyZMQ

C# publisher and Python subscriber for data communication using ZMQ protocol. 

----------
## C# (publisher):

```CSharp
// A C# Program for Server 
using System; 
using System.Threading;
using NetMQ;
using NetMQ.Sockets;

namespace Publisher 
{ 
    class Publisher 
    { 
    // Main Method 
        static void Main(string[] args) 
        { 
            using (var publisher = new PublisherSocket())
            {
                publisher.Bind("tcp://127.0.0.1:5556");
                while (true)
                {
                    publisher.SendFrame("Hello World");
                }
            }
        } 
    } 
} 
```

## Python (subscriber):

```python
import zmq

def recv():
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect('tcp://127.0.0.1:5556')
    subscriber.setsockopt(zmq.SUBSCRIBE, b'')
    while True:
        print(subscriber.recv())

while True:
    recv()
```



