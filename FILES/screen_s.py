from blinker import receiver_connected
from vidstream import StreamingServer
import threading

def start_server():
    receiver = StreamingServer('192.168.1.194', 5252)
    receiver.start_server()

t = threading.Thread(target=start_server)
t.start()

while input("") != 'STOP':
    continue

receiver_connected.stop_server()
