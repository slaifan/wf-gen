from http import client
import sys
from client import Client, ClientFactory

MODE = sys.argv[1]
URL = f'https://www.{sys.argv[2]}'

client = ClientFactory.getClient(MODE)

client.getPage(URL)


