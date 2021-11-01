# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# # YTURL=input("Enter website URL: ")
# # y=YTURL[YTURL.index('=')+1::]
# # URL="https://www.y2mate.com/youtube/"+y
# # print(URL)


# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open Chrome
driver = webdriver.Chrome(r"C:\SeleniumDrivers\chromedriver")

# Open URL
driver.get('http://demo.automationtesting.in/FileDownload.html')

# Enter text
driver.find_element_by_id('textbox').send_keys("Hello world")

# Generate Text File
driver.find_element_by_id('createTxt').click()

# Click on Download Button
driver.find_element_by_id('link-to-download').click()


