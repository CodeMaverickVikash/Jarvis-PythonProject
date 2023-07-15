import pyttsx3 #pip install pyttsx3
import datetime
import time
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
# import cv2
import random
import requests
import pywhatkit
import pyjokes
import pyautogui
import PyPDF2 # working on pdf files
import windowsapps
# from chatbot import chatbot1
import wolframalpha

# Playing with social media
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui

# Gui
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QTimer, QTime, QDate, Qt, QThread
from PyQt5.QtCore import *
# from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

from ui.jarvisGui import Ui_MainWindow

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 100)

# voice to text
def takeCommand(msg):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening.....")
        print(f"{msg} Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        # speek("Please wait, Recognizing your task")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.....")
        query = takeCommand(msg)
    return query

# text to voice
def speek(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    # ui = Ui_MainWindow()
    # ui.output()
    boss = "Welcome back boss"
    if hour >= 0 and hour < 12:
        speek(f"{boss} Good Morning, its {current_time}")

    elif hour >= 12 and hour < 18:
        speek(f"{boss} Good Afternoon, its {current_time}")

    else:
        speek(f"{boss} Good Evening, its {current_time}")

    speek("Let me introduce myself, I am jarvis your personal assistance. Please tell me how may I help you")

# task - send a pdf/text file through email using python 
def sendEmail(receiver_mail, msg):
    sender_mail = "example@gmail.com"
    sender_pass = "example_password"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_mail, sender_pass)
    server.sendmail(sender_mail, receiver_mail, msg)
    server.close()

# New API
def news():
    try:
        country = 'in'
        apiKey = 'f684d2873c9c4016bd0a221f4e0bddf1'

        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={apiKey}"
        json = requests.get(url).json() # converted into dict
        # print(json)
        
        if json:
            articles = json['articles']
            # print(articles)

            head = [] # Contains all the title/headline
            for articleObject in articles:
                head.append(articleObject['title'])
            
            # print(head)
            # print(len(head))

            # numberOfNews = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
            numberOfNews = ['first', 'second', 'third']
            for i in range(len(numberOfNews)):
                # print(f"{numberOfNews[i]} news is: {head[i]}")
                speek(f"{numberOfNews[i]} news is: {head[i]}")
        else:
            print("Poor network! Try again.......")
    except:
        print("Server error! Try again later")
        
def pdf_redder():
    book = open('Machine_learning.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speek(f"total number of pages in this book {pages}")
    speek("enter pages number for reading")
    pg = int(input("Please enter page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speek(text)


def facebook():
    try:
        browser = webdriver.Chrome()
        browser.get('https://www.facebook.com/')

        username = "example@gmail.com"
        password = "example_password"

        enter_username = WebDriverWait(browser, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'email')))
        enter_username.send_keys(username)

        enter_password = WebDriverWait(browser, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'pass')))
        enter_password.send_keys(password)

        # press enter after sending password
        enter_password.send_keys(Keys.RETURN)
        time.sleep(20)


        # Message section
        WebDriverWait(browser, 2).until(expected_conditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/span/div/div[1]'))).click()


        message = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]')


        # Friend request
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[1]/span/span/div/a').click()
        time.sleep(3)
        for noti in browser.find_elements(By.TAG_NAME, 'strong'):
            speek(f"You have new friend request from {noti.text}")

        time.sleep(5)
        speek("Vikash, do you to post something")
        query = takeCommand("Facebook").lower()
        if 'yes' in query:
            # FB post
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span').click()
            msgs = takeCommand("Facebook Post").lower()
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div').send_keys(msgs)

            # Click on post
            browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span').click()
    except:
        speek("internet is slow, Try again later!!")

def instagram():
    try:
        browser = webdriver.Chrome()
        base_url = 'https://www.instagram.com/'

        username = "lazyboy73738"
        password = "Lazyboy@123"

        # username = "_sid.1102"
        # password = "prakash@1102"
        
        browser.get(base_url)
        
        # ENTERING THE USERNAME FOR LOGIN INTO INSTAGRAM
        enter_username = WebDriverWait(browser, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(username)
        
        # ENTERING THE PASSWORD FOR LOGIN INTO INSTAGRAM
        enter_password = WebDriverWait(browser, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(password)
    
        # RETURNING THE PASSWORD and login into the account
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        # first pop-up box
        # browser.find_element_by_xpath(
        #     '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        # ui.WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".sqdOP.yWX7d.y3zKF"))).click()

        # second pop-up box
        ui.WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
        time.sleep(20)
    except:
        speek("internet is slow, Try again later!!")

def whatsapp():
    browser = webdriver.Chrome()
    browser.get("https://web.whatsapp.com/")

    time.sleep(20)

# Main application
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    # It will automatically call
    def TaskExecution(self):
        wishMe()
        
        while True:
        # if 1:
            self.query = takeCommand("Jarvis").lower()

            # Getting information of any person from Wikipedia
            if 'wikipedia' in self.query or 'wiki' in self.query:
                speek("Searching wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speek("According to wikipedia")
                speek(results)

            # Opening system installed app and searching on google chrome
            elif self.query.find('open') != -1:
                self.ok = self.query.replace('open ', '')
                try:
                    self.name, self.appid = windowsapps.find_app(f'{self.ok}')
                    if self.name:
                        if self.name == 'Google Chrome':
                            speek('Sir, what should i search on google')
                            cm = takeCommand("App open").lower()
                            # webbrowser.open(f'{cm}')
                            search_string = cm.replace('jarvis', '')
                            search_string = search_string.replace(' ', '+')
                            browser = webdriver.Chrome() 
                            for i in range(1):
                                matched_elements = browser.get("https://www.google.com/search?q=" +
                                                                search_string + "&start=" + str(i))
                            
                        else:
                            speek(f"Launching, {self.ok} for you sir")
                            windowsapps.open_app(f'{self.ok}')
                    else:
                        print("There is No app to open, Please confirm once, back again")
                except:
                    speek("There is some problem, activating jarvis mode")
                    # speek("Please tell me full name " + self.query)

            # Introduction
            elif "what can you do for me" in self.query:
                speek("As you know i programmed with some fuctionality to make your life easier, i can do wikipeadia search, Read headlines of news, i can play song on youtube and system, tell about your location, you can ask some generic question, Opening all system installed application, Google search based on your query, social media info etc.")

            # Jarvis i have question for you
            elif "question" in self.query or "ask" in self.query or "question mode" in self.query or "question answer mode" in self.query:
                try:
                    speek(f"Sure boss, we are at question answer mode, what do you want to ask?")
                    con = 1
                    while True:
                        que = takeCommand("Que").lower()
                        app_id = 'JY2Y4Y-HGTLQRJ52X'
                        client = wolframalpha.Client(app_id)
                        res = client.query(que)
                        answer = next(res.results).text
                        speek(answer)
                        speek("Do you have another question for me")
                        tf = takeCommand("Que").lower()
                        if "no please" in tf:
                            con = 0
                        elif "yes" in tf:
                            continue
                        elif "thanku" in tf or "thanks" in tf:
                            con == 0 
                        if con == 0:
                            speek("Ok, always ready for you")
                            break
                except:
                    speek("Your internet is slow, so taking to you at jarvis mode")

            # Check where are you
            elif "where i am" in self.query or "where we are" in self.query:
                speek("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json() # in the form of dictonary
                    # print(geo_data)
                    city = geo_data['city']
                    country = geo_data['country']
                    speek(f"sir i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speek("sorry sir, Due to network issue i am not able to find where we are")

            # jarvis can you check my social media before start
            elif "social media" in self.query or "social account" in self.query:
                speek("Sure sir, what should i check")
                social_media = takeCommand("Social media").lower()
                if "facebook" in social_media:
                    facebook()
                elif "instagram" in social_media:
                    instagram()
                elif "whatsapp" in social_media:
                    whatsapp()
                
            # Playing with social media like facebook, instagram, whatsapp
            # elif 'whatsapp' in self.query:
            #     try:
            #         # pywhatkit.sendwhatmsg("+919752004079", "how are you", 22, 28)
            #         # speek("Your message has been sent")

            #         # pywhatkit.search("How to make jarvis")
            #         pass
            #     except:
            #         print("An Unexpected Error!")
            
            # You can play song on youtube
            elif 'play song online' in self.query:
                speek("What song  do you want to play")
                song = takeCommand("Song ytb").lower()
                pywhatkit.playonyt(song)

            # playing with email
            elif 'send email' in self.query:
                try:
                    speek("What should I say?")
                    content = takeCommand("Email").lower()
                    to = "example@gmail.com"
                    sendEmail(to, content)
                    speek("Email has been sent!")
                except Exception as e:
                    print(e)
                    speek("Sorry my friend vikash bhai. I am not able to send this email")

            # Getting jokes
            elif "jokes" in self.query:
                joke = pyjokes.get_joke()
                speek(joke)
            
            # Shutdown computer
            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")
            
            # Restart computer
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            
            # Play song on system
            elif 'music' in self.query or 'song' in self.query:
                speek("Sure sir")
                music_dir = 'C:\\Users\VIKASH\Desktop\Python\JarvisProject\mp3songs'
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                # print(songs)
                # os.startfile(os.path.join(music_dir, songs[0]))
                os.startfile(os.path.join(music_dir, rd))

            # System time
            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speek(f"Sir, the time is {strTime}")

            # elif 'open camera' in self.query:
            #     cap = cv2.VideoCapture(0) # 0 mean default camera
            #     while True:
            #         ret, img = cap.read()
            #         cv2.imshow('webcam', img)
            #         k = cv2.waitKey(50)
            #         if k == 27:
            #             break
            #     cap.release()
                # cv2.destroyAllWindows()

            # elif 'lets talk' in self.query or 'can we talk' in self.query:
            #     speek("why not.")
            #     chatbot1.conversation()

            # Switching windows
            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            
            # Speaking news
            elif "news" in self.query:
                speek("please wait sir, fetching the latest news")
                news()    
            
            # Screenshot
            elif "screenshot" in self.query:
                speek("sir, please tell me the name of this screenshot file")
                name = takeCommand("Screenshot").lower()
                speek("please sir hold the screen few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speek("i am done sir, the screenshot is saved in our main folder. now i am ready for take new command")

            # audiobook using python
            elif "read pdf" in self.query:
                pdf_redder()

            # to hide files and folder
            # elif "hide all files and folder" in self.query or "make it visible for everyone" in self.query:
            #     speek('sir please tell me what you want "hide" or "visible"')
            #     condition = takeCommand().lower()
            #     if "hide" in condition:
            #         os.system('attrib +h /s /d')
            #         speek('sir, all files in this folder are now hidden')
            #     elif "visible" in condition:
            #         os.system('attrib -h /s /d')
            #         speek('sir, all files in this folder are now visible to everyone')
            #     elif "leave it" in condition or "leave it now" in condition:
            #         speek('ok sir')

            # Close window
            elif "close" in self.query or "exit" in self.query or "sleep" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("f4")
                time.sleep(1)
                pyautogui.keyUp("alt")



# instance of mainthread
startExecution = MainThread()      

# pyqt5
class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(1400)
        self.setFixedHeight(900)

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.startTask()
        # self.ui.pushButton.clicked.connect(self.startTask)
        # self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        # Running GIF
        self.ui.movie = QtGui.QMovie("C:\\Users\VIKASH\Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        # timer
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)

        # set text to gui
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())