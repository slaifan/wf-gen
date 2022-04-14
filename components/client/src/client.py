import time
from selenium import webdriver
 
from abc import ABC, abstractmethod

class ClientFactory:
    def getClient(mode):
        if mode == 'chrome' or mode == 'firefox':
            return SeleniumClient(mode)
            

class Client(ABC):
    @abstractmethod
    def getPage(self, url):
        pass

class SeleniumClient(Client):
    def __init__(self, mode):
        if mode == 'chrome':
            self.driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.

            options = webdriver.ChromeOptions()
            options.add_argument("--no-proxy-server")
            options.add_argument("--enable-quic")
            options.add_argument("--origin-to-force-quic-on=www.google.com:443")
            options.add_argument("no-proxy-server")

        elif mode == 'firefox':
            self.driver = webdriver.Firefox()

    def getPage(self, url):
        self.driver.get(url)
        time.sleep(2) 
        self.driver.quit()
        