#Programmer: Brent E. Chambers (q0m)
#Date: 3/28/2013
#Description: This program is a part of the CIDST training module.  
# Files needed: pentrn_red.py (Primary Access Class for the XLS Data)
#               pentrn-red.xls (Resource File [xls])
#               cidst.py (GUI front end)
#  Needed:
#  Still needs to be able to search through the Syntax list
#  Then it needs to split the Technique prefix and merge it with the Syntax entry
#  The Technique Prefix + Syntax
#
# Updates:
# 2/4/2022 -- Converting to Py3 and Updating the content to malware and exploit development only

import xlrd
import xlwt
import csv

class PenInstance:
	def __init__(self, filename="Becrevindex.xls"):
		self.tArray = []
		self.sArray = []
		self.dArray = []
		self.filename = filename
		self.book = xlrd.open_workbook(filename)
		self.CurrentModeData = (self.tArray, self.sArray, self.dArray) #Columns: Technique, Syntax, and Array.  A triplet item.  
		self.secMode = self.book.sheet_names() #sheet array #secMode is the legacy name for the sheetname
		self.sheetCount = len(self.book.sheet_names())
	
	def writeNote(self, noteText):
		noteSheet = self.book.sheet_by_name('Notes')
		data = noteText
		noteSheet.write(2, 2, data)
		
	def saveResourceFile(self):
		self.book.save(filename)
		noteSheet = xlwt

	def listDisciplines(self):
		"""Foo bar foo bar."""
		
		secMode = self.book.sheet_names()
		#for item in secMode:
		#	print item
			
	def loadCurrentMode(self, mode):
		sheet = self.book.sheet_by_name(mode) #set the sheet to the supplied mode
		return sheet
		

	def populateData(self, sheet):
		techniqueIndex = sheet.col_values(0)		#creates the first column data
		syntaxIndex = sheet.col_values(1)			#creates the second column data
		descriptionIndex = sheet.col_values(2)		#creates the third column daata
		self.CurrentModeData = [self.tArray, self.sArray, self.dArray]
		#print CurrentModeData
		for item in techniqueIndex:
			self.CurrentModeData[0].append(item)
		for item in syntaxIndex:
			self.CurrentModeData[1].append(item)
		for item in descriptionIndex:
			self.CurrentModeData[2].append(item)
				
	def createMasterList(self): 
		testy = []
		for item in self.secMode:
			testy.append(item)
		for item in testy:
			sheet = self.loadCurrentMode(item)
			self.populateData(sheet)
			masterList = self.CurrentModeData
		return masterList

	def dump_techniques(self):	
		masterList = self.createMasterList()
		all_technique_items = []
		for item in masterList[0]:
			all_technique_items.append(item)
		all_technique_items = set(all_technique_items)
		return all_technique_items
	
	def dump_syntax(self):
		masterList = self.createMasterList()
		all_syntax_items = []
		for item in masterList[1]:
			all_syntax_items.append(item)
		all_syntax_items = set(all_syntax_items)
		return all_syntax_items
	
	def dump_descriptions(self):
		masterList = self.createMasterList()
		all_description_items = []
		for item in masterList[2]:
			all_description_items.append(item)
		all_description_items = set(all_description_items)
		return all_description_items
		
	def newsearch(self, query):
		masterResults = []
		searchResults = []
		masterList = self.createMasterList()
		techniqueSearchResults = []
		techniqueSearchResults = [t for t in self.dump_techniques() if query in t]
		techniqueSearchResults = set(techniqueSearchResults) #removes all duplicatesn
		#First searches the technique Array for the search query
		for technique in techniqueSearchResults:
			technique_ref_Number = masterList[0].index(technique)
			searchResults.append([technique, 
								masterList[1][technique_ref_Number],
								masterList[2][technique_ref_Number]])
				
		#Then we check the syntax, looking for the tool mayhaps?
		syntaxSearchResults = []
		syntaxSearchResults = [s for s in self.dump_syntax() if query in s]
		syntaxSearchResults = set(syntaxSearchResults)
		for syntax in syntaxSearchResults:
			syntax_ref_Number = masterList[1].index(syntax)
			searchResults.append([masterList[0][syntax_ref_Number],
								syntax,
								masterList[2][syntax_ref_Number]])
		#Then look throught he description for stuff and roll with it -- ya heard?
		descrptionSearchResults = []
		descriptionSearchResults = [d for d in self.dump_descriptions() if query in d]
		descriptionSearchResults = set(descriptionSearchResults)
		for description in descriptionSearchResults:
			description_ref_Number = masterList[2].index(description)
			searchResults.append([masterList[0][description_ref_Number],
								masterList[1][description_ref_Number],
								description])
		
		print ("\n\nPENTRN Returned", len(searchResults), "results.\n\n")
		return searchResults
		
	def red_search(self, query):
		sheet = self.loadCurrentMode("Syntax")	#switch the searchable content to the Syntax datasheet
		self.populateData(sheet)				#populate the current instance with the Syntax data
		masterResults = []
		searchResults = []
		syntaxSearchResults = []

		#Dump the contents of the Syntax worksheet
		syntaxSearchResults = [t for t in self.dump_syntax() if query in t]
		unique_syntaxSearchResults = set(syntaxSearchResults)
		for item in unique_syntaxSearchResults:
			print(item)

	def ci_search(self, query):
		masterResults = []
		searchResults = []
		sheet = self.loadCurrentMode("Syntax")
		self.populateData(sheet)
		techniques = self.CurrentModeData[1]
		sytnax      = self.CurrentModeData[2]
		
		#unique_techniques = set(techniques)
		
		techniqueSearchResults = [t for t in techniques if query in t]
		#techniqueSearchResults.sort()
		print("\n")
		for item in techniqueSearchResults:
			technique_ref_number = techniqueSearchResults.index(item)
			technique_syntax = self.CurrentModeData[2][technique_ref_number]
			searchResults.append((item, technique_syntax))
			#print item
		uniqueResults = set(searchResults)
		print("\nQuery: ", query)
		print("Returned", len(uniqueResults), "items.")
		return uniqueResults
		
	
	
	
	'''
		pentrn_red.py  works a little bit differently than pentrn.py
		pentrn_red loads the first datasheet (Index), populating the Technique field with the first column
		it also loads the second column into the Description (formerly Syntax) field.  
		when an item in the Description field is selected, pentrn_red will grab the corresponding item from
		the second datasheet (Syntax) and populate the Syntax field with the third column
		
		The technique's all have a prefix (CYA, DSFCU, ENUM, etc)
			when a search is performed, the Technique is populated with the description results and the prefix
				example:  TOOLKIT - Obtain a certain kind of Event from Eventlog
				
		
		The search function needs to take a query

			search all entries in Syntax[B] (because it's a 1:1) and store them in a container with an index number
				if query in Syntax[B]:
					store the tuple in a 3D-Tuple with the Index[0] = Index[1]
			search all entries in Syntax[C] and store them in a container with an index number			
	'''
	
	
	
	
	
	
	
	
	
	
	
	
		
		
