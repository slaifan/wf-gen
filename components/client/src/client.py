import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


import socket   

hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)
 
from abc import ABC, abstractmethod

class ClientFactory:
    def getClient(browser, mode):
        return SeleniumClient(browser, mode)
            

class Client(ABC):
    @abstractmethod
    def getPage(self, url):
        pass

class SeleniumClient(Client):
    def __init__(self, browser, mode):
        time.sleep(2)
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--no-proxy-server")
            if mode == 'quic':
                options.add_argument("--enable-quic")
            else:
                options.add_argument("--disable-quic")         
            options.add_argument("--headless")

            print("options added, starting driver")
            
            self.driver = webdriver.Remote(
                    command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.CHROME,
                    options=options,
                )

        elif browser == 'firefox':
            fp = webdriver.FirefoxProfile()
            options = webdriver.FirefoxOptions()
            if mode == 'quic':
                fp.set_preference("network.http.http3.enabled", False)
            else:
                fp.set_preference("network.http.http3.enabled", True)
            self.driver = webdriver.Remote(
                    command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.FIREFOX,
                    options=options,
                )

        elif browser == 'edge':
            options = webdriver.EdgeOptions()
            if mode == 'quic':
                options.add_argument("QuicAllowed=1")
            else:
                options.add_argument("QuicAllowed=0")
            self.driver = webdriver.Remote(
                    command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=DesiredCapabilities.EDGE,
                    options=options,
                )
    def getPage(self, url):
        time.sleep(1) 
        self.driver.get(url)
        self.driver.save_screenshot('/src/test.png')
        time.sleep(5) 
        self.driver.quit()
        
