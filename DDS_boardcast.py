import json
import socket
import threading
import time

class DDS_Client:
    def __init__(self, name, topics, port=9999):
        self.name = name
        self.topics = topics
        self.data = None
        self.port = port

    def broad_cast(self, topic, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        if topic not in self.topics:
            print(f"Topic '{topic}' not in topics list.")
            return
        json_data = {
            "topic": topic,
            "data": message
        }
        try:
            sock.sendto(json.dumps(json_data, ensure_ascii=False).encode('utf-8'), ('<broadcast>', self.port))
            # print(f"broadcast successful: {message}")
        finally:
            sock.close()

    

class DDC_Subscriber:
    def __init__(self, topic, port=9999):
        self.topic = topic
        self.port = port
        self.data = None
        self.listen_thread = None
        self.running = False

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', self.port))
        while self.running:
            try:
                data, addr = sock.recvfrom(1024)
                json_data = json.loads(data.decode('utf-8'))
                if json_data['topic'] == self.topic:
                    self.data = json_data['data']
                    # print(f"Receive: {self.data}")
            except socket.error:
                if not self.running:
                    break
        sock.close()
    
    def start_listening(self):
        if self.listen_thread is None:
            self.running = True
            self.listen_thread = threading.Thread(target=self.listen)
            self.listen_thread.start()
        else:
            print("Listener is already running.")
    
    def stop_listening(self):
        if self.listen_thread is not None:
            print("Stopping listener...")
            self.running = False
            print("Listener stopped.")
            self.listen_thread = None
        else:
            print("Listener is not running.")