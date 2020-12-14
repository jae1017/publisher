import zmq
import time
from multiprocessing import Process


class Server(object):

    def __init__(self):
        self.port = '5556'
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(f"tcp://*:{self.port}")
        print(f"Server started ...")

    def start(self):
        while True:
            message = self.socket.recv()
            print(f"Server received request: ", message)
            time.sleep(1)
            self.socket.send(str.encode("Status is OK"))

    def check_status(self):
        pass


class Publisher(object):

    def __init__(self):
        self.pub_topic = "outage"
        self.pub_port = "5557"
        self.pub_context = zmq.Context()
        self.pub_socket = self.pub_context.socket(zmq.PUB)
        self.pub_socket.bind(f"tcp://*:{self.pub_port}")
        print("Publisher started ...")

    def send_message(self, message):
        self.pub_socket.socket.send(str.encode(message))


class Subscriber(Publisher):

    def __init__(self):
        super().__init__()
        self.sub_port = "5558"
        self.sub_topic = "outage"
        self.sub_context = zmq.Context()
        self.sub_socket = self.sub_context.socket(zmq.SUB)
        # self.sub_socket.setsockopt(zmq.SUBSCRIBE, "Child:")
        self.sub_socket.bind(f"tcp://*:{self.sub_port}")
        print("Subscriber started ...")

    def start(self):
        while True:
            
