#PENTRN Practice

# Change the FONT
# Make the font bigger
# Edit PENTRN.py so it targets the new CIDST resource
#    don't forget to categorize and import the old master data to the new procs
#    How to maintain a consistency, and remind the Operative where they are in the procedures
#    Module needs a feature to add/edit resource content.  This way, any records that contain a NULL value can be
#		populated as they are learned or researched. 
#	 Module also needs a button to copy the content in the syntax field to the clipboard
# Todo:
# Display Pictures -- maybe a slideshow of procedures or layouts or mindmaps
# Import BlackHat Go source
# Import Blackhat Rust Source
# Convert XLS to XML that interfaces the same with the UI
#  encrypt the XML and embed it within the application so it' all-in-one
# Continue to import OSEP
# Continue to import PTX
# XDS Techniques / toolbox collection
# Ability to store images and view them as a slideshow
# Hide extra Tk() window
# Rename application to something better
#

import tkinter as tk
import pentrn_red
#import sets
import string
import csv
import time

mode = "Index"
index = ''
appStatus = ""
global notebookIndexText
netbookIndexText = ""

#buffer_filename = ("buffer.csv")
#buff = open(buffer_filename, 'wb')

#notebook_filename = ("CIDST_Notebook.csv")
#noteBook = open(notebook_filename)
NOTE_MODE = 0
SEARCH_MODE = 0
#writer = csv.writer(noteBook)
#reader = csv.reader(buffer)

#GUI Settings 
root = tk.Tk()
#root.wm_attributes('-topmost', 1)
root.resizable(width='False', height='False')
root.title("Adversarial Informatics Combat Module v2.0") 
root.geometry("1070x570+330+90")
s = "Choose a selection"

notebook_buffer = []

def copyDescription():
	r = tk.Tk()
	r.withdraw()
	r.clipboard_clear()
	text = descriptionBox.get('1.0', tk.END)
	clipboard_text = text[:-1]
	r.clipboard_append(clipboard_text)
	r.destroy()


def run_notebook():
	#turn Description Green
	global NOTE_MODE
	if NOTE_MODE == 0:	# If NOTE_MODE is off... enter NOTE_MODE...
		NOTE_MODE = 1
		descriptionBox.config(bg='#CCFFCC', fg='black')   #Turn description green
		reader = csv.reader(notebook_filename)				#Open the reader handler to the notebook
		for row in reader:
			if row[0] == notebookIndexText:					#if the current IndexText is found in the notebook..
				descriptionBox.delete('1.0', '40.0')		#clear it out
				descriptionBox.insert('1.0', row[2])		#insert the coresponding text
			else:											#if the current IndexText is not found in the notebook..
				descriptionBox.delete('1.0', '40.0')				
	elif NOTE_MODE == 1:   #If NOTE_MODE is on... save notes and exit NOTE_MODE...
	# Write whatever is in the descriptionBox to the buffer file
		NOTE_MODE = 0
		descriptionBox.config(bg='#FFFFFF', fg='black')
		notebookIndexText = techniqueBox.get(index)
		data = [notebookIndexText,
				time.ctime(),
				descriptionBox.get('1.0', tk.END)]
		with open(notebook_filename, 'wb') as csv_file:
			writer = csv.writer(csv_file)#, delimiter=',')
			writer.writerow(data)
		get_syntax
		#	for line in string.split(data, " "):
		#		writer.writerow(5,5, line)
				
				
				
def run_notebook_old():
	global NOTE_MODE
	test = NOTE_MODE
	if test == 0:
		print("Notebook mode is off... turning on.")
		NOTE_MODE = 1
	elif test == 1:
		print ("Notebook is on... turning off.")
		NOTE_MODE = 0
	
def toggle_notebook_mode():
	#
	pass
	

def get_list(event):
    NOTE_MODE = 0	#turn off note_mode
    syntaxBox.delete(0, tk.END)					#clears out the syntax box
    descriptionBox.delete('1.0', '420.0')
    try:										#grabs the index number for the cursor selection
        index = techniqueBox.curselection()[0]	#What number in the techinique array is the selection?
    except:
        pass
    seltext = techniqueBox.get(index)			#makes sure it has the right stuff
    print(seltext)    #Prints the selection to console
    try:
        statusLabel.config(text='                            PENTRN> '+seltext)
    except:
        pass
    if SEARCH_MODE != 0:
        indexFinder = instance.sArray.index(seltext)	# change the column to search if SEARCH MODE is on
    else:
        indexFinder = instance.tArray.index(seltext)	# if search mode off, do it the old way
    text = str(instance.sArray[indexFinder])
    descript = str(instance.dArray[indexFinder])
    notebookButton.config(bg='white')
    print (text.split("\n"))
    print (text)
    print (len(text))
    for item in text.split("\n"):
        syntaxBox.insert(0, "[+] "+item)
    descriptionBox.insert('1.0', descript)


#str(string.split(text, "\n").index(item))+

def get_syntax(event):
    descriptionBox.delete('1.0', '100.0')
    print(event)
    try:
        index = syntaxBox.curselection()[0]
    except Exception as ex:
        print(str(ex))
    seltext = syntaxBox.get(index)				  #grabs text from syntax
    notebookIndexText = seltext
    notebookButton.config(bg='green') 		                  # Turn Notebook_Button to Green
    #indexFinder = archive_instance.sArray.index(seltext[4:])	  #grabs number of selected item in technique
    indexFinder = archive_instance.sArray.index(seltext[4:])
    text = str(archive_instance.dArray[indexFinder])		  #resolves text in dArray to indexFinder
    descriptionBox.insert('1.0', text)				  #inserts description text into descriptiobox
    print (event)
    copyDescription()

def get_popup_syntax(event):
    descriptionBox.delete('1.0', '100.0')
    print (event)
    try:
        index = popuplist.curselection()[0]
    except Exception as ex:
        print(str(ex))
    seltext = popuplist.get(index)				  #grabs text from syntax
    notebookIndexText = seltext
    notebookButton.config(bg='green') 		                  # Turn Notebook_Button to Green
    #indexFinder = archive_instance.sArray.index(seltext[4:])	  #grabs number of selected item in technique
    indexFinder = archive_instance.sArray.index(seltext)
    text = str(archive_instance.dArray[indexFinder])		  #resolves text in dArray to indexFinder
    descriptionBox.insert('1.0', text)				  #inserts description text into descriptiobox
    print (event)
    copyDescription()

def offsec_mode(event):
    #Create an instance of pentrn
    instance = pentrn_red.PenInstance("CI_Basic_Index_offsec.xls")
    sheet = instance.loadCurrentMode(mode)
    #syntax_sheet = instance.loadCurrentMode("Syntax")
    #techniqueBox.delete('1.0', '100.0')
    instance.populateData(sheet)
    for item in instance.CurrentModeData[0]:
        techniqueBox.insert(0, item)



def search():
	SEARCH_MODE = 1
	print ("Search string: ", searchBox.get())
	#Take the search string ^
	query = searchBox.get()					
	unique_search_items = []
	search_items = []
	search_results = instance.ci_search(query)
	print ("search_results count:", len(search_results))
	for item in search_results:
		search_items.append(item[0].split("\n"))
	#for item in search_results:
	#	unique_search_items.append(item)
	#for item in string.split(unique_search_items, "\n"):
	#	search_items.append(item)
	search_items.sort()
	for item in search_items:
		print(item)
	syntaxBox.delete(0, tk.END)
	for item in search_items:
		syntaxBox.insert(0, "[+] "+item[0])
	#Put everything from Syntax tab and put it in an array
	
	#Search for the string in the array, mark the index number
	#search_results = instance.ci_search(query)
	
	#for item in instance.CurrentModeData[0]:
	#	techniqueBox.insert(0, item)
		
	#for item in search_results:
	#	techniqueBox.insert(0,

	#Overlap the syntax and description field with a blue and white (fg) searh result popup
	
	#Populate the new blue popup with search results
	
	#upon double click

def popup_all(event):
    #boot = tk.Tk()
    #boot.wm_attributes('-topmost', 1)
    #popuplist = tk.Listbox(boot, height=40, width=60, bg='#236B8E', fg="white")
    popuplist.grid(row=1, column=1, sticky='n'+'s'+'w'+'e')
    yScroll = tk.Scrollbar(boot, orient=tk.VERTICAL)
    yScroll["command"] = popuplist.yview
    yScroll.grid(row=1, column=2, sticky='n'+'s')
    test = pentrn_red.PenInstance()
    sheet = test.loadCurrentMode("Syntax")
    test.populateData(sheet)
    test.CurrentModeData[1]
    all_techniques = []
    for item in test.CurrentModeData[1]:
        if len(item) > 0:
                    all_techniques.append(item)
    unique_techniques = set(all_techniques)
    u_techs = []
    for item in unique_techniques:
            u_techs.append(item)
    u_techs.sort()
    for item in u_techs:
        popuplist.insert(0, item)
    popuplist.bind('<ButtonRelease-1>', get_popup_syntax)
    popuplist.bind('<Up>', get_syntax)
    popuplist.bind('<Down>', get_syntax)



        
def searchResults(event):
	print(event)
	searchResultsBox = tk.Text(root, height=6, width=71, wrap='word', fg='black', bg='white')
	descriptionBox.grid(row=2, column=2, sticky='n'+'s')
	yscroll = tk.Scrollbar(command=descriptionBox.yview, orient=tk.VERTICAL)
	yscroll.grid(row=1, column=5, sticky='n'+'s')
	yscroll.grid(row=1, column=5, sticky='n'+'s')

#Popup Box Test
boot = tk.Tk()
boot.wm_attributes('-topmost', 0)
popuplist = tk.Listbox(boot, height=35, width=60, bg='#236B8E', fg="white")
	
#Technique Box Configuration
#techniqueBox = tk.Listbox(root, height=19, width=50, bg="#AAB3AA", fg='black')
techniqueBox = tk.Listbox(root, height=15, width=38, bg='#236B8E', fg='white', font=('Arial', 9, 'bold'))
techniqueBox.grid(row=1, column=0, rowspan=3, sticky='n'+'s')
techniqueBox.bind('<ButtonRelease-1>', get_list) #calls get_list to populate the syntax window
techniqueBox.bind('<Up>', get_list)
techniqueBox.bind('<Down>', get_list)
yscroll = tk.Scrollbar(command=techniqueBox.yview, orient=tk.VERTICAL)
yscroll.grid(row=1, column=1, sticky='n'+'s', rowspan=3)

#Syntax Box Configuration
syntaxBox = tk.Listbox(root, height=7, width=70, bg='#236B8E', fg='white', font=('Arial', 9, 'bold'))
#syntaxBox = tk.Listbox(root, height=14, width=100, bg="#AAB3AA", fg='black')
syntaxBox.grid(row=1, column=2, columnspan=4, sticky='n'+'s'+'e'+'w')
syntaxBox.bind('<ButtonRelease-1>', get_syntax)
syntaxBox.bind('<Up>', get_syntax)
syntaxBox.bind('<Down>', get_syntax)
yscroll = tk.Scrollbar(command=syntaxBox.yview, orient=tk.VERTICAL)
yscroll.grid(row=1, column=5, sticky='n'+'s')

#Description Box Configuration
descriptionBox = tk.Text(root, height=26, width=95, wrap='word', fg='black', bg='white')
descriptionBox.grid(row=2, column=2, sticky='n'+'s')
yscroll = tk.Scrollbar(command=descriptionBox.yview, orient=tk.VERTICAL)
yscroll.grid(row=2, column=5, sticky='n'+'s')

#Description Box Configuration

#command= lambda mode=item:change_mode(mode)

''' Taken out to clean up the status bar
clearButton = tk.Button(root, text="CLEAR")#, command=clear_forms)
clearButton.grid(row=4, column=1, sticky='w', columnspan=2)
'''
statusLabel = tk.Label(root, textvariable=appStatus)
statusLabel.grid(row=4, column=1, sticky='w', columnspan=2)

notebookButton = tk.Button(root, width=26, text="Notebook", command=run_notebook)#, bg='green', fg='black')
notebookButton.grid(row=4, column=2, sticky='e', columnspan=3)

copyButton = tk.Button(root, width=10, text="Copy", command=copyDescription)
copyButton.grid(row=4, column=1, sticky='w', columnspan=2)

searchBox = tk.Entry(root)
searchBox.grid(row=4, column=0, sticky='e'+'w')#, rowspan=1)

searchButton = tk.Button(root, text='SEARCH', command=search)
searchButton.grid(row=4, column=0, sticky='e', rowspan=2)

#Create an instance of pentrn
instance = pentrn_red.PenInstance()
sheet = instance.loadCurrentMode(mode)
#syntax_sheet = instance.loadCurrentMode("Syntax")
instance.populateData(sheet)
for item in instance.CurrentModeData[0]:
    techniqueBox.insert(0, item)

techniqueBox.itemconfig(0, {'fg': 'white'})
techniqueBox.itemconfig(1, {'fg': 'white'})
techniqueBox.itemconfig(1, {'fg': 'white'})

#Create another instance of pentrn
archive_instance = pentrn_red.PenInstance() #creating another instance for syntax searching
archive_sheet = archive_instance.loadCurrentMode("Syntax")
archive_instance.populateData(archive_sheet) #load up the archive sheet

#creates another instance for note keeping			taking this out because it's worthless
#noteTaking_instnce = pentrn_red.PenInstance()
#noteTaking_sheet = archive_instance.loadCurrentMode("Notes")

#Close out the GUI and finish off the mainloop
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

toolsmenu = tk.Menu(menubar, tearoff=0)
toolsmenu.add_separator()
toolsmenu.add_command(label="All Techniques", command= lambda mode=item:popup_all(mode))
menubar.add_cascade(label="Tools", menu=toolsmenu)

modemenu = tk.Menu(menubar, tearoff=0)
modemenu.add_separator()
modemenu.add_command(label="Offsec Mode", command= lambda mode=item:offsec_mode(mode))
menubar.add_cascade(label="Mode", menu=modemenu)
                    
root.config(menu=menubar)
root.mainloop()
