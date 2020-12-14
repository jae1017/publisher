import zmq
from multiprocessing import Process


def client():
    port = "5558"
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.connect(f"tcp://localhost:{port}")

    for request in range(1, 10):
        print(f"Sending request {request}")
        socket.send(b"Hello")
        message = socket.recv()
        print(f"Received reply {request} [ {message} ]")


if __name__ == '__main__':
    p1 = Process(target=client, args=(1,))
    p2 = Process(target=client, args=(2,))
    p1.start()
    p2.start()
