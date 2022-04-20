from http import client
import sys
from client import Client, ClientFactory

# MODE = sys.argv[1]
# URL = f'https://www.{sys.argv[2]}'


MODE = 'chrome'
URL = f'https://www.google.com'
NUM_REP = 3
for _ in range(NUM_REP):
    print("*********** STARTED ***********")
    print(f'{MODE} mode, url: {URL}')

    client = ClientFactory.getClient(MODE)

    print("*********** is getting page ***********")

    client.getPage(URL)


