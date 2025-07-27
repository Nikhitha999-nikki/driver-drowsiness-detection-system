# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:04:42 2019

@author: Lenovo
"""

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Style
import subprocess    

def blink():
    try:
        subprocess.call(["python", "face-try.py"])
    except Exception as e:
        messagebox.showerror("Error",f"Failed to run face detection:\n{e}")
    
def lane():
    try:
        subprocess.call(["python", "blinkDetect.py"])
    except Exception as e:
        messagebox.showerror("Error",f"Failed to run blink detection:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x500')
    root.title("Driver Drowsiness Detection System")
    root.resizable(0, 0)

    root.configure(bg="#e8eef1")

    style = Style()
    style.configure('TButton', font =('calibri', 18, 'bold'), borderwidth = '2')

    frame = tk.Frame(root,bg="#e8eef1")
    frame.pack()

    button1 = tk.Button(frame, text="Face Detection", fg="white", bg="#0078D7",activebackground="#005A9E", activeforeground="white", command=blink,relief="raised", bd=3, padx=10, pady=5)
    button1.pack(side=tk.LEFT,padx=20,pady=10)

    button2 = tk.Button(frame, text="Blink Detection",fg="white", bg="#2D7D46",activebackground="#1B4F23", activeforeground="white",command=lane,relief="raised", bd=3, padx=10, pady=5)
    button2.pack(side=tk.RIGHT,padx=20,pady=10)

    button3 = tk.Button(frame, text="Quit", fg="white", bg="#E81123",activebackground="#A80000", activeforeground="white",command=root.destroy,relief="raised", bd=3, padx=10, pady=5)
    button3.pack(side=tk.BOTTOM,pady=30)

    root.mainloop()