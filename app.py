from tkinter import * 
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry('400x300')
root.resizable(0, 0)
root.config(bg = '#45B39D')
root.title('Text To Speech')

Label(root, text = 'Convert text to speech', font='arial 20 bold', fg = '#fff', bg = '#000').pack()
Label(root, text = 'Enter your text here', font='arial 14 bold', fg = '#fff', bg = '#000').place(x=20, y=70)

Msg = StringVar()

entry_field = Entry(root, textvariable = Msg, width = '59')
entry_field.place(x=20, y=100)

def Text_to_speech():
    message = entry_field.get()
    speech = gTTS(text = message)
    speech.save('python_py.mp3')
    playsound('python_py.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set(" ")   

#Button  

Button(root, text = "Play", font = 'ariel 14 bold', command = Text_to_speech, fg = '#fff', bg = '#2980B9', width = 5).place(x=20, y=140)       
Button(root, text = "Reset", font = 'ariel 14 bold', command = Reset, fg = '#fff', bg = '#F39C12', width = 5).place(x=169, y=140)       
Button(root, text = "Exit", font = 'ariel 14 bold', command = Exit, fg = '#fff', bg = '#C0392B', width = 5).place(x=307, y=140)       

root.mainloop()