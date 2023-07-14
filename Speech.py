import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import os
import webbrowser
import sys
import docx
import subprocess


        
listener = sr.Recognizer()
m = sr.Microphone()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def callback(listener, audio):
    command=listener.recognize_google(audio)
    print(command)
    return command
    
def juno():
    engine.say("Hey Harsh! How can I help?")
    engine.runAndWait()

def talk(command):
    engine.say(command)
    engine.runAndWait()
    
def authenticate():
    talk("What's my name?")
    with m as source:
        print("Speak Now :")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        initial = listener.recognize_google(voice,language = "en-en")
        if 'gravity' in initial.lower():
            juno()
            return 0
        else :
            talk("That's not my name. Failed to recognize user")
            return 1
            
def listen():
    with m as source:   
    
        print("Listening now :")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
            
        command = listener.recognize_google(voice,language = "en-en")
        print("Loading ...")
        return command
            
            
def background_search():
    i=0
    while (i==0):
        try:
            com=listen()
            
        except :
            continue   
            
        if len(com)>=0:
            j=first_search(com)
            i=i+j
        
        else:
            continue 
   
        
def first_search(com):
    i=0        
    try:
        if 'play' in com.lower():
            playcommand = com.replace('play',' ')
            print(com)
            talk('Playing' + playcommand)
            kit.playonyt(playcommand)
            i = i+0
                   
        elif 'search' in com.lower():
            print(com)
            playcommand = com.replace('search',' ')
            talk('Searching for' + playcommand)
            kit.search(playcommand)
            i = i+0   
                    
        elif ('open' in com.lower()) and ('word' in com.lower()): 
                       
            talk("Pick a name for your word file ")
            command = listen()
            saveas= command + ".docx"
            print(saveas)
            doc= docx.Document()
            doc.save(saveas)
            talk("Opening" + saveas)
            os.system("start " + saveas)
            i = i+0

            
        elif ('open' in com.lower()) and ('calculator' in com.lower()): 
            talk("opening Calculator")
            subprocess.Popen('C:\\Windows\\SysWOW64\\calc.exe')
            i = i+0   

        elif ('open' in com.lower()) and ('excel' in com.lower()):
                  
            talk("Pick a name for your excel file ")
            command = listen()
            saveas= command + ".xls"
            print(saveas)
            doc= docx.Document()
            doc.save(saveas)
            talk("Opening Excel file")
            os.system("start " + saveas)
            i = i+0       
                    
                    
        elif ('open' in com.lower()) and ('powerpoint' in com.lower()):
                    
            talk("Opening Powerpoint")
            os.system(powerpnt)
            i = i+0          
                        
        elif ('go to' in com.lower()): 
            playcommand = com.replace('go to','')
            url = "https:\\www." + playcommand.strip()
            talk("Opening" + playcommand )
            print(url)
            webbrowser.open(url,new = 1)
            i = i+0          
            
        elif ('stop' in com.lower()) or ('sleep' in com.lower()):
            talk("Okay, Bye!!")
            i=i+1
            
        elif ('launch' in com.lower() and ('counter-strike' in com.lower()) or 'cs' in com.lower()):
            talk('Okay. Get ready to school noobs')
            
            subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 730")
            talk('Have Fun!')
            i=i+1
                        
        else:
            talk('Looking for' + com + 'On google')
            kit.search(com)
            i = i+0
        
        
                   
    except:
        talk("Sorry, I didn't quite catch that")
      
    return i
                
                
                
        
        
        
        

    
try:
    k = authenticate()
    if k==0:
        background_search()
    elif k==1:
        talk("Exiting")
        exit()

except :
    talk("I'm Sick. Come back Later")

                   
                
    
        

