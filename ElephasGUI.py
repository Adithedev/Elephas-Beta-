from tkinter import *
from traceback import print_stack
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess

root = Tk()
root.geometry("500x500") 
root.configure(bg='ghost white')
root.title("Elephas.exe")

Label(root, text = "Elephas", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="Adithegeek", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Terminal", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

print_panel = StringVar()
print_panel.set("I am Listening what's up Sir...")

def Voice():
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 125)

def speak():
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate", 150)

    def talk(text):
        engine.say(text)
        engine.runAndWait()

    def take_command():
        try:
            with sr.Microphone() as source:

                print_panel.set("I am Listening what's up Adi...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'elephas' in command:

                    command = command.replace('elephas', '')
                    print_panel.set(command)
        except:
            pass
        return command

    def run_alexa():

        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            print_panel.set('playing ' + song)
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print_panel.set('Current time is ' + time)
            talk('Current time is ' + time)
        
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print_panel.set(info)
            talk(info)

        elif 'what is' in command:
            place_thing = command.replace('what is', '')
            info = wikipedia.summary(place_thing, 1)
            print_panel.set(info)
            talk(info)
        elif 'who are you' in command:
            talk('Hello i am Elephas, A self coded bot by Adi')
            print_panel.set('Hello i am Elephas, A self coded bot by Adi')
        
        elif 'what do you think of adi' in command:
            talk('he is so kind hearted because he was one who brought me to life!')
            print_panel.set('he is so kind hearted because he was one who brought me to life!')
        
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            print_panel.set(joke)
        
        elif "iphone" in command:
            talk("Iphone is the best and cheapest phone.Lol Just kidding but its worth buying!")
            print_panel.set("Iphone is the best and cheapest phone. Lol Just kidding but its worth buying!")

        elif "hacking" in command:
            talk("OMG hacking is illegal! wait let me call the cops!")
            print_panel.set("OMG hacking is illegal! wait let me call the cops!")

        elif "good night" in command:
            talk("Good Night sir i will meet you tommorow morning!")
            print_panel.set("Good Night sir i will meet you tomm morning!")
            root.destroy()

        elif "good morning" in command:
            talk("Welcome back sir! Check you Notion app to check your todays goals.")
            print_panel.set("Welcome back sir! Check you Notion app to check your todays goals.")

        elif "notepad" in command:
            talk("Oppening Notepad!")
            print_panel.set("Oppening Notepad!")
            subprocess.call("notepad.exe")

        # elif "command" in command:
        #     talk("Oppening Command prompt!")
        #     print_panel.set("Oppening Command prompt!")
        #     subprocess.call("cmd.exe")

        elif "calculator" in command:
            talk("Oppening Calculator!")
            print_panel.set("Oppening Calculator!")
            subprocess.call("calc.exe")

        
        elif "bye" in command:
            root.destroy()
        else:
             talk('I am afraid i cant understand sir...')
             print_panel.set('I am afraid i cant understand sir...')

    run_alexa()

def EXIT():
    root.destroy()

Button(root,text = "Quit", font = "ColonnaMT", command = EXIT, bg= "Red").place(x=425, y=400)
Button(root,height= 3, width=5,text = "Speak", font = "ColonnaMT", command = speak, bg= "LightGreen",).place(x=225, y=250)
Entry(root,width=54,textvariable = print_panel, font = ("Arial", 10 ), bg = "LightGreen").place(x=5,y=100,height=100)
root.mainloop()