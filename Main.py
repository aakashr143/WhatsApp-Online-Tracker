import selenium
from selenium import webdriver
from time import sleep
import datetime
from playsound import playsound
from tkinter import *


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
startTime = ""

root = Tk()
root.title("Tracker")
root.geometry("170x55")
root.configure(background="White")

timeLabel = Text(root, height=1, width=10)
timeLabel.pack()

startLabel = Text(root, height=1, width=20)
startLabel.pack()

while True:  # Checking if the person is online
    currentDate = datetime.datetime.now()
    try:
        checkOnline = driver.find_elements_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
        minOnline = round(secOnline/60, 2)
        print(currentDate.strftime("%Y-%m-%d %H:%M:%S") + "; " + checkOnline[0].text + "; " + str(minOnline) + " min")
        userOnline = True
        root.configure(background="Green")
        timeLabel.delete("1.0", "end")
        timeLabel.insert(END, str(minOnline))

        if audioPlay: # plays beep only once, at the start of the session
            print("============================================================")
            playsound('Beep.mp3')
            audioPlay = False
            startTime = currentDate.strftime("%Y-%m-%d %H:%M:%S")
            startLabel.delete("1.0", "end")
            startLabel.insert(END, startTime)

        if userOnline:
            secOnline = secOnline + 1
    except IndexError:
        root.configure(background="Black")
        startLabel.delete("1.0","end")
        timeLabel.delete("1.0", "end")

        audioPlay = True
        userOnline = False
        secOnline = 0
    except selenium.common.exceptions.StaleElementReferenceException:
        print("Value Error")

    sleep(1)  # change this value to change the update time
    root.update()

