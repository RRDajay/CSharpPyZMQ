// A C# Program for Server 
using System; 
using System.Threading;
using NetMQ;
using NetMQ.Sockets;

namespace Publisher { 

    class Publisher { 

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
