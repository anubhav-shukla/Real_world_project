from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry('400x200+100+200')   
root.configure(bg='Pink')
root.title("Anubhav - TEXT TO SPEECH")

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="Anubhav shukla", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable = Msg ,width ='50',fg='blue',highlightbackground='yellow')
entry_field.place(x=20,y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('anubhav.mp3')
    playsound('anubhav.mp3')

def Exit():
    root.destroy()
def Reset():
    Msg.set("")   

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)


root.mainloop()