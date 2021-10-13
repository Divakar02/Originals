# /html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Autolog:
    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\SeleniumDrivers\chromedriver")

    def login(self):
        self.driver.get("https://www.google.com/")
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.click()
        searchentry=self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        searchentry.send_keys('ncr')
        searchentry.send_keys(Keys.ENTER)
        ncr=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div[1]/a/h3')
        ncr.click()
        ncr2=self.driver.find_element_by_xpath(('//*[@id="page-bdc0579887"]/div[3]/div/div[1]/header/div[1]/div[4]/div[1]/div/div[1]/section/div[1]/p/a'))
        ncr2.click()
        ncr3=self.driver.find_element_by_xpath('//*[@id="page-bdc0579887"]/div[3]/div/div[1]/header/div[1]/div[4]/div[1]/div/div[1]/section/form/div/input')
        ncr3.click()

bot = Autolog()
bot.login()


