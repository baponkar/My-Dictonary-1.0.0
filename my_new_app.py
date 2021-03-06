#!/usr/bin/python

"""
Build Date : 18/01/2019.
Last Modification : 18/01/2019.
Author : Bapon Kar.
Name   : My Dictionary
Version : 1.0.0
Description : This is a english to english Dictionary 
              You can find the meaning and description of all english word by this app.
              Thank You for Downloading This application.
_______________________________________________________________________________________.
"""



import json
from difflib import *

data = json.load(open("data.json","r"))


def view(word,word_dict):
	res = []
	if word in word_dict:
		for i in word_dict[word]:
			if int(len(str(i))) > 150:
				res.append(str(i[1:100]))
				res.append(str(i[100:]))
				print(res)
			else:
				res.append(i)
	elif word.lower() in word_dict:
		word=word.lower()
		for i in word_dict[word]:
			res.append(i)
	elif close_matcher(word,word_dict) != "":
		res.append("Are You looking for? : " + close_matcher(word,word_dict))
	
	else:
		res.append("\tSorry no such type word exist!")
	return res

def close_matcher(word,word_dict):
	res = get_close_matches(word,word_dict)[0]
	return res 

	
	
def search_command():
	search_word=search_text.get()
	if search_word == '':
		lsb1.delete(0,END)
		lsb1.insert(END,"\n\n\tSorry You Did not entered anything!")
	list_view = view(search_word,data)
	lsb1.delete(0,END)
	for i in view(search_word,data):
		lsb1.insert(END,i)
		
	return list_view


def about_command():
	lsb1.delete(0,END)
	for i in __doc__.split('\n',10):
		lsb1.insert(END,i)
	

from tkinter import *
root = Tk()
root.geometry("600x500")

root.title("My Dictionary")
root.configure(background="#C3D3C3")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
 
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...",command=about_command)
menubar.add_cascade(label="Help", menu=helpmenu)
 
root.config(menu=menubar)







l1 = Label(root,text="           My Dictionary ")
l1.grid(row=0,column=1)

l2 = Label(root,text=" Enter Your word ")
l2.grid(row=2,column =0)

b1 = Button(root,text="Search",width=12,command=search_command,bg="#1FC3DC")
b1.grid(row=2,column=3)


search_text = StringVar()
e1 = Entry(root,textvariable=search_text,width=30)
e1.grid(row=2,column=1,columnspan=2)


lsb1 = Listbox(root,height=30,width=80)
lsb1.grid(row=3,column=0,rowspan=7,columnspan=5)


root.mainloop()

