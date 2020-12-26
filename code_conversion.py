#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:25:24 2020

@author: harinee
"""

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image,ImageOps

def to_Binary():      #decimal to binary 
    d=deci1.get()
    common_ans.set("")
    for i in d: #for loop is for checking the valid input if the input is invalid it will show warning
        if ord(i)>=48 and ord(i)<=57:
            continue
        else:
            messagebox.showwarning("warning", "Invalid Input!") 
            deci1.set("")
            common_ans.set("")
            return
    n=int(d)    
    binary=[]
    #conversion from decimal to binary
    if n==0:
        binary.append('0')
    while n>=1:
        binary.append(str(n%2))
        n=n//2    
    common_ans.set("".join(binary)[::-1])

def binary_to_Decimal():#binary to decimal
    bvalue=b2.get()
    deci2.set("")
    for i in bvalue:#for loop is for checking the valid input if the input is invalid it will show warning
        if ord(i)==48 or ord(i)==49:
            continue
        else:
            messagebox.showwarning("warning", "Invalid Input!") 
            b2.set("")
            deci2.set("")
            return
    bvalue=bvalue[::-1]
    d=0
    for i in range(len(bvalue)):#conversion from binary to decimal
        d+=(int(bvalue[i])*(2**i))
    deci2.set(str(d))    

def to_Octal():#decimal to octal
    d=deci1.get()
    common_ans.set("")
    for i in d:#for loop is for checking the valid input if the input is invalid it will show warning
        if ord(i)>=48 and ord(i)<=57:
            continue
        else:
            messagebox.showwarning("warning", "Invalid Input!") 
            deci1.set("")
            common_ans.set("")
            return
    n=int(d)
    octal=[]
    #conversion from decimal to octal
    if n==0:
        octal.append('0')
    while n>=1:
        octal.append(str(n%8))
        n=n//8
    common_ans.set("".join(octal)[::-1])    

def octal_to_Decimal():#octal to decimal
    ovalue=oct4.get()
    deci4.set("")
    for i in ovalue:#for loop is for checking the valid input if the input is invalid it will show warning
        if ord(i)>=48 and ord(i)<=57:
            continue
        else:
            messagebox.showwarning("warning", "Invalid Input!") 
            oct4.set("")
            deci4.set("")
            return
    ovalue=ovalue[::-1]
    d=0
    for i in range(len(ovalue)):#conversion from octal to decimal
        d+=(int(ovalue[i])*(8**i))
    deci4.set(str(d))

def to_Hexa():#decimal to hexadecimal
    d=deci1.get()
    common_ans.set("")
    for i in d:#for loop is for checking the valid input if the input is invalid it will show warning
        if ord(i)>=48 and ord(i)<=57:
            continue
        else:
            messagebox.showwarning("warning", "Invalid Input!") 
            deci1.set("")
            common_ans.set("")
            return
    n=int(d)
    hexa=[]
    #conversion from decimal to hexa 
    if n==0:
        hexa.append('0')
    while n>=1:
        x=str(n%16)
        if x=='10':
            x='A'
        elif x=='11':
            x='B'
        elif x=='12':
            x='C'
        elif x=='13':
            x='D'
        elif x=='14':
            x='E'
        elif x=='15':
            x='F'
        hexa.append(x)
        n=n//16
    common_ans.set("".join(hexa)[::-1])

def hexa_to_Decimal():#hexadecimal to decimal
    hexavalue=hexa6.get()
    deci6.set("")
    for i in hexavalue:#for loop is for checking the valid input if the input is invalid it will show warning
        if (ord(i)>=48 and ord(i)<=57)or(ord(i)>=65 and ord(i)<=70):#each character must be a number or ['A' or 'B' or 'C' or 'D' or 'E' or 'F']
            continue
        else:
            messagebox.showwarning("warning", "Invalid Input!")
            hexa6.set("")
            deci6.set("")
            return
    hexavalue=hexavalue[::-1]
    d=0
    for i in range(len(hexavalue)):#conversion from hexa to decimal
        x=hexavalue[i]
        if x=='A':
            x='10'
        elif x=='B':
            x='11'
        elif x=='C':
            x='12'
        elif x=='D':
            x='13'
        elif x=='E':
            x='14'
        elif x=='F':
            x='15'
        d+=((int(x))*(16**i))
    deci6.set(str(d))

root=Tk()  
root.title("CODE CONVERTER APP  =)")
root.geometry('700x700')
C = Canvas(root, bg ="lightgreen", 
           height = 700, width = 700)  #making window to lightgreen color

img = Image.open('/home/harinee/Desktop/logo.jpg') #setting "logo.jpg" as background 
img1= img.resize((700,700), Image.ANTIALIAS) #resizing logo.jpg to 700x700
img1 = ImageTk.PhotoImage(img1) 
panel = Label(root, image = img1)
panel.image = img1
panel.place(x=0,y=70)  #placing at x=0 y=70

deci1=StringVar() #declaring variable for storing decimal value entry
common_ans=StringVar()  #declaring variable for storing the result 
lbl=Label(root,text="Welcome To Harinee's Code Converter!!!",justify="center").place(x=200,y=30) 
decimal_lbl1=Label(root,text="DecimalValue").place(x=10,y=125) #label to indicate decimal value entry
decimal_entry1=Entry(root,width=20,textvariable=deci1).place(x=100,y=125) #entry for giving decimal value as input
from_dec_ans_entry=Entry(root,width=20,textvariable=common_ans).place(x=370,y=125) #entry to store the result of binary value

#button when pressed will change the decimal value to binary
to_btn1=Button(root,text="To Binary ",command=lambda:to_Binary(),bg='pink',bd='3').place(x=260,y=95) 
#button when pressed will change the decimal value to octal
to_btn3=Button(root,text="To Octal  ",command=lambda:to_Octal(),bg='pink',bd='3').place(x=260,y=125) 
#button when pressed will change the decimal value to hexadecimal
to_btn5=Button(root,text="To Hexa   ",command=lambda:to_Hexa(),bg='pink',bd='3').place(x=260,y=155) 


deci2=StringVar() #declaring variable for storing decimal value entry
b2=StringVar()#declaring variable for storing the result ie. binary value
binary_lbl2=Label(root,text="BinaryValue").place(x=10,y=220) #label to indicate binary value entry
binary_entry2=Entry(root,width=20,textvariable=b2).place(x=100,y=220) #entry for giving binary value as input
to_btn2=Button(root,text="To Decimal",command=lambda:binary_to_Decimal(),bg='pink',bd='3').place(x=260,y=215) #button to convert to decimal value once it is clicked
decimal_ans_entry2=Entry(root,width=20,textvariable=deci2).place(x=370,y=220) #entry to store the result 


deci4=StringVar() #declaring variable for storing decimal value entry
oct4=StringVar()#declaring variable for storing the result ie. octal value
octal_lbl4=Label(root,text="OctalValue").place(x=10,y=250) #label to indicate octal value entry
octal_entry4=Entry(root,width=20,textvariable=oct4).place(x=100,y=250) #entry for giving octal value as input
to_btn4=Button(root,text="To Decimal",command=lambda:octal_to_Decimal(),bg='pink',bd='3').place(x=260,y=245) #button to convert to decimal once it is clicked
decimal_ans_entry4=Entry(root,width=20,textvariable=deci4).place(x=370,y=250) #entry to store the result of binary value


deci6=StringVar()#declaring variable for storing decimal value entry
hexa6=StringVar()#declaring variable for storing the result ie. hexadecimal value
hexa_lbl6=Label(root,text="HexaValue").place(x=10,y=280) #label to indicate hexadecimal value entry
hexa_entry6=Entry(root,width=20,textvariable=hexa6).place(x=100,y=280) #entry for giving hexadecimal value as input
to_btn6=Button(root,text="To Decimal",command=lambda:hexa_to_Decimal(),bg='pink',bd='3').place(x=260,y=275) #button to convert to decimal value once it is clicked
decimal_ans_entry6=Entry(root,width=20,textvariable=deci6).place(x=370,y=280) #entry to store the result 

C.pack()
root.mainloop()

   
    
        
        

