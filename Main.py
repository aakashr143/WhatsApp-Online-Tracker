from selenium import webdriver
from time import sleep
import datetime


driver = webdriver.Chrome(
    executable_path='/Users/aakashrathee/Desktop/PythonBots/chromedriver')
driver.get("https://web.whatsapp.com/")

username = "Aakash Rathee"  # Add the person's name you want to tracker

sleep(10) # Time for the user to login via phone before an error occurs and the programs crashes

user = driver.find_elements_by_xpath('//span[@title="{}"]'.format(username))
user[0].click()  # Bot has reached the desired person's chat
sleep(2)


def sendMessage():
    message = "Hello, I'm a whatsapp bot"
    messageBox = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    messageBox[0].send_keys(message)
    sleep(2)
    sendButton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    sendButton[0].click()
    sleep(2)


while True:  # Checking if the person is online
    currentDate = datetime.datetime.now()
    try:
        checkOnline = driver.find_elements_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
        print(currentDate.strftime("%Y-%m-%d %H:%M:%S") + " " + checkOnline[0].text)
    except IndexError:
        print(currentDate.strftime("%Y-%m-%d %H:%M:%S") + " " + "offline")
    sleep(1) # change this value to change the update time


# To see weather the person is online or not the data will be on the console
# The data is updated every second