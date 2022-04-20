import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


import socket   

hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)
 
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
        time.sleep(5)
        if mode == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--no-proxy-server")
            options.add_argument("--enable-quic")
            options.add_argument("--origin-to-force-quic-on=www.google.com:443")
            options.add_argument("--headless")
            options.add_argument("--disable-dev-shm-usage")

            print("options added, starting driver")
            
            self.driver = webdriver.Remote(
                    command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.CHROME,
                    options=options,
                )

        elif mode == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference("network.http.http3.enabled", True)
            self.driver = webdriver.Remote(
                    command_executor='http://selenium:4445/wd/hub',
                    desired_capabilities=DesiredCapabilities.FIREFOX,
                    options=options,
                )

    def getPage(self, url):
        print(f'ip address is : {IPAddr}')
        time.sleep(1) 
        self.driver.get(url)
        self.driver.save_screenshot('/src/test.png')
        self.driver.quit()
        
