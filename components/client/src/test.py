import time
import requests
i = 0
while i < 5:
    print(i)
    time.sleep(5)
    r = requests.get("https://www.google.org")
    print(f"hello {r.headers['Content-Type']} ")
    i += 1
    
while i < 20:
    time.sleep(5)
    i += 1
