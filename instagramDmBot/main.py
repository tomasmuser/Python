from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from secret import username, password


class instaBot:
    def __init__(self):

        mobile_emulation = { "deviceName": "Nexus 5" }

        chrome_options = webdriver.ChromeOptions()

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])    
        chrome_options.add_argument("--start-maximized")


        # self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',\                          desired_capabilities = chrome_options.to_capabilities())   



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


        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(6)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Cancel')]")\
            .click()
        sleep(6)



    def acceptMessageRequest(self):        
        self.driver.get("https://www.instagram.com/direct/inbox/")
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(6)
        self.driver.get("https://www.instagram.com/direct/requests/")
        sleep(6)
        self.driver.find_element_by_xpath("//img")\
            .click()
        sleep(2) 
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div[2]/div[5]/button")\
            .click()
        self.driver.get("https://www.instagram.com/direct/requests/")
        

if __name__ == "__main__":
    msg_bot = instaBot()
    msg_bot.acceptMessageRequest()
    sleep(900)