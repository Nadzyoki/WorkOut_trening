import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs

import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Привет, тут будет прога для контроля за отжиманиями с уведомлениями для одобрения твоей работы")
greeting.pack()
window.mainloop()