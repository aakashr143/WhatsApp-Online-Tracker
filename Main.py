from selenium import webdriver
from time import sleep
import datetime
from playsound import playsound

driver = webdriver.Chrome(
    executable_path='/Users/aakashrathee/Desktop/PythonBots/chromedriver')
driver.get("https://web.whatsapp.com/")

username = "Lara Faulstich"  # Add the person's name you want to tracker

sleep(10)  # Time for the user to login via phone before an error occurs and the programs crashes

user = driver.find_elements_by_xpath('//span[@title="{}"]'.format(username))
user[0].click()  # Bot has reached the desired person's chat
sleep(2)

audioPlay = False
userOnline = False
secOnline = 0

while True:  # Checking if the person is online
    currentDate = datetime.datetime.now()

    try:
        checkOnline = driver.find_elements_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
        print(currentDate.strftime("%Y-%m-%d %H:%M:%S") + "; " + checkOnline[0].text + "; " + "CurrentOnlineDuration : " + str(round(secOnline/60),2) + " min")
        userOnline = True
        if audioPlay: # plays beep only once, at the start of the session
            playsound('Beep.mp3')
            audioPlay = False
        if userOnline:
            secOnline = secOnline + 1
    except IndexError:
        print("offline")
        audioPlay = True
        userOnline = False
        secOnline = 0
    sleep(1)  # change this value to change the update time

# To see weather the person is online or not the data will be on the console
# The data is updated every second
