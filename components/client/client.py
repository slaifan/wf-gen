from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions() 
options.add_argument("--enable-quic")
options.add_argument("--origin-to-force-quic-on=google.com https://www.facebook.com/")
options.headless

driver = webdriver.Chrome(r'c:\Users\F.K\Desktop\Honours project\code\client\drivers\chromedriver', options=options)

driver.get("https://www.facebook.com")