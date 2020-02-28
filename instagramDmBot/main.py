from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from secret import username, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class instaBot:
    def __init__(self):

        mobile_emulation = { "deviceName": "Nexus 5" }

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])    
        chrome_options.add_argument("--start-maximized")


        # self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',\
        #                           desired_capabilities = chrome_options.to_capabilities())   
        # mobile_emulation = {
        #     "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 1.0 },
        #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
        # chrome_options = Options()
        # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        self.driver = webdriver.Chrome(options = chrome_options)

        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(6)
        self.closeNotNow()
        sleep(6)
        self.closeCancel()
        

    def goToInbox(self):
        sleep(2)
        self.driver.get("https://www.instagram.com/direct/inbox/")
        try:
            sleep(4)
            self.closeNotNow()
        finally:
            return


    def closeNotNow(self):
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()


    def closeCancel(self):
        self.driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]")\
            .click()


    def acceptRequest(self):
        self.driver.find_element_by_xpath("//img")\
            .click()
        sleep(2) 
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div[2]/div[5]/button")\
            .click()
        self.acceptMessageRequest


    def driverClose(self):
        self.driver.close()


    def acceptMessageRequest(self):
        self.driver.get("https://www.instagram.com/direct/requests/")
        sleep(6)
        try:
            self.acceptRequest
        finally:
            pass


    def newMessage(self):
        try:
            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.CLASS_NAME, "KdEwV")))
            self.autoResponse()
            self.driver.get("https://www.instagram.com/")
        except:
            return


    def readMessage(self):
        # TODO finalizar
        self.goToInbox()
        self.driver.find_element_by_xpath("//div[contains(text(), 'german.santucho')]")\
            .click()
        sleep(4)        
        message = self.driver.find_element_by_xpath("//div[contains(class(), '_7UhW9   xLCgt      MMzan  KV-D4           p1tLr      hjZTB')]")
        print(message.text())
        pass


    def autoResponse(self):
        self.goToInbox()
        self.driver.find_element_by_xpath("//a/div/div[3]/div")\
            .click()
        self.driver.find_element_by_xpath("//textarea")\
            .send_keys("Mensaje Automatico")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]")\
            .click()
    

    def response(self):
        self.goToInbox()
        self.driver.find_element_by_xpath("//div[contains(text(), 'belen_molinari')]")\
            .click()
        sleep(4)
        cont = 0
        while cont < 200:
            self.driver.find_element_by_xpath("//textarea")\
                    .send_keys("Mensaje Automatico")
            self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]")\
                    .click()       
            cont +=1

if __name__ == "__main__":
    msg_bot = instaBot()
    msg_bot.response()
    while True:
        sleep(60)
        msg_bot.newMessage()
