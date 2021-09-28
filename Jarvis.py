import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
from speedtest import main
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import operator 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');

engine.setProperty('voices', voices[len(voices) - 1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query




def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am jarvis sir. please tell me how may i help you")

"""    
#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR EMAIL ADDRESS', 'YOUR PASSWORD')
    server.sendmail('YOUR EMAIL ADDRESS', to, content)
    server.close()
 """
 
 




if __name__ == "__main__": 
    wish()
    while True:
   

        query = takecommand().lower()
            

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            
        elif 'Hello' in query or 'hello' in query:
            speak('Hello sir')
        
        elif "open adobe reader" in query:
            apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            speak("playing music")
            music_dir = "C:\\Users\\DIPTABHANU\\Music\\Most fav"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                     os.startfile(os.path.join(music_dir, song))



        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
           

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
        
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")


        elif "open whatsapp" in query:
            speak("opening whatsapp")
            whatsapppath = "C:\\Users\\DIPTABHANU\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapppath)
        
        elif "open code" in query:
            codepath = "C:\\Users\\DIPTABHANU\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif "open bandicam" in query:
            campath = "C:\\Program Files (x86)\\Bandicam\\bdcam.exe"
            os.startfile(campath)

        elif "open photoshop" in query:
            photopath = "C:\\Program Files (x86)\\Adobe\\Photoshop 7.0\\Photoshop.exe"
            os.startfile(photopath)
        
        elif "how are you" in query:
            speak("I am fine sir, What about you ")
            cm = takecommand().lower()
            speak("Thats good")
            speak("Can I do some thing for you?")
            cm = takecommand().lower()
            speak("ok sir")
            speak("just tell me")
        

        elif "who are you" in query:
            speak("I am jarvis and I am also a vartual assistent")
            speak("I was made by Diptabhanu Senapati")
        
        elif "what is your coding language" in query:
            speak("Python is my coding language")
                   
        
        
       
       
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')


        elif "songs on youtube" in query:
            kit.playonyt("Dynamite")
            
        elif 'timer' in query or 'stopwatch' in query:
            speak("For how many minutes?")
            timing = takecommand()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')
        
        
            time.sleep(timing)
            speak('Your time has been finished sir')
            """
            elif "email to avinash" in query:
                try:
                    speak("what should i say?")
                    content = takecommand().lower()
                    to = "EMAIL OF THE OTHER PERSON"
                    sendEmail(to,content)
                    speak("Email has been sent to avinash")
                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this mail to avi")
                    
                """

       
       


        
        elif "set alarm" in query: 
            nn = int(datetime.datetime.now().hour)   
            if nn==22:
                    music_dir = "C:\\Users\\DIPTABHANU\\Music\\Most fav"
            
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir, songs[0]))       

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")







        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
                   

       

        elif "email to Chikun" in query:
               
            speak("sir what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'your@gmail.com' 
                password = 'your_pass'
                send_to_email = 'To_person@gmail.com' 
                speak("okay sir, what is the subject for this email")
                query = takecommand().lower()
                subject = query  
                speak("and sir, what is the message for this email")
                query2 = takecommand().lower()
                message = query2  
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("please enter the path here")    

                speak("please wait,i am sending email now")
            
            
           
            

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

               
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to avinash")

            else:                
                email = 'your@gmail.com' 
                password = 'your_pass' 
                send_to_email = 'To_person@gmail.com' 
                message = query 

                server = smtplib.SMTP('smtp.gmail.com', 587) 
                server.starttls() 
                server.login(email, password) 
                server.sendmail(email, send_to_email , message) 
                server.quit() 
                speak("email has been sent to avinash")
        
    
    
        elif "exit" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()