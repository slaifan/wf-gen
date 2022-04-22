from http import client
import sys
import time
from tkinter import BROWSE
from client import Client, ClientFactory
import os

BROWSER = os.environ['BROWSER']
MODE = os.environ['MODE']
URL = f"https://www.{os.environ['URL']}"
NUM_REP = int(os.environ['REPEAT'])

for _ in range(NUM_REP):
    print("*********** STARTED ***********")
    print(f'{BROWSER} {MODE} mode, url: {URL}')

    client = ClientFactory.getClient(BROWSER, MODE)

    print("*********** is getting page ***********")

    client.getPage(URL)
    time.sleep(20)


