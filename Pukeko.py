#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import argparse
import sys
import glob
import magic
import textract
import colorama
colorama.init()

# Argparse starts here
parser = argparse.ArgumentParser()	
							
parser.add_argument('-input', dest='input',help="input a directory or a file",metavar=None)
parser.add_argument('-output', dest='output',help="output words into a file",metavar=None)
parser.add_argument('-print', dest='show', action='store_true',help="show what Pukeko is reading")	
parser.add_argument('-hotwords', dest='hotwords', action='store_true',help="show rows that contains HotWords")
parser.add_argument('-min', dest='min', default='4', type=int, help="Minimum word length (by default is 4)", metavar=None)
parser.add_argument('-max', dest='max', default='20', type=int, help="Maximum word length (by default is 20)", metavar=None)	
									
args = parser.parse_args()
# If user directory nothing print help
if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)
# Argparse ends here

# Terminal color definitions
class fg:
	BLACK   = '\033[30m'
	RED     = '\033[31m'
	GREEN   = '\033[32m'
	YELLOW  = '\033[33m'
	BLUE    = '\033[34m'
	MAGENTA = '\033[35m'
	CYAN    = '\033[36m'
	WHITE   = '\033[37m'
	RESET   = '\033[39m'

class bg:
	BLACK   = '\033[40m'
	RED     = '\033[41m'
	GREEN   = '\033[42m'
	YELLOW  = '\033[43m'
	BLUE    = '\033[44m'
	MAGENTA = '\033[45m'
	CYAN    = '\033[46m'
	WHITE   = '\033[47m'
	RESET   = '\033[49m'

class style:
	BRIGHT    = '\033[1m'
	DIM       = '\033[2m'
	NORMAL    = '\033[22m'
	RESET_ALL = '\033[0m'


output = args.output


if os.path.exists(output) == True:
	OutputFile = open(output, "r",encoding='UTF8')
	outputword = list(set(OutputFile.read().split()))
	OutputLenStart = len(outputword)
	print (fg.RED,style.BRIGHT, OutputLenStart, style.RESET_ALL, "in", args.output, "before being", fg.BLUE,style.BRIGHT, "Pukekoed", style.RESET_ALL)

HotWords = ["password", "admin","S/N","key","administrator","sysadmin"]

# Let's build how the lists are created
def buildList():
	count = 0
	
	if os.path.exists(output) == True:
		OutputFile = open(output, "r+",encoding='UTF8')
	elif os.path.exists(output) == False:
		OutputFile = open(output, "a+",encoding='UTF8')
	
	directoryword = list(set(directoryFile.split()))

	
	
	directoryLen = len(directoryword)
	#print (directoryword)
	outputword = list(set(OutputFile.read().split()))
	OutputLenBefore = len(outputword)
	mergedlist = list(set(directoryword + outputword))
	#OutputLenAfter = len(mergedlist)
	
	mergedlist.sort(key=len)

	OutputFile = open(output, "w+",encoding='UTF8')
	for word in mergedlist:
		if len(word) > args.max: 
			pass
		elif len(word) < args.min:
			pass
		else:
			OutputFile.write(word+"\n")
			count += 1
	OutputFile.close()
	print (fg.YELLOW,style.BRIGHT, "+", count-OutputLenBefore, style.RESET_ALL, i,  )
	
	# Search for Hotwords
	if args.hotwords:
		for line_no, line in enumerate(directoryFile.splitlines()):
			if any(word.lower() in line.lower() for word in HotWords):
				print ("	", fg.CYAN,style.BRIGHT, line_no, ':', line,style.RESET_ALL)
	
def LetsTry(p):
	#while True:
		try:	
			global directoryFile
			global GrabdirectoryFile
			
			if p.lower().endswith(('.csv', '.doc', '.docx', '.eml', '.epub', '.gif', '.htm', '.html', '.jpeg', '.jpg', '.json', '.log', '.mp3', '.msg', '.odt', '.ogg', '.pdf', '.png', '.pptx', '.ps', '.psv', '.rtf', '.tff', '.tif', '.tiff', '.tsv', '.txt', '.wav', '.xls', '.xlsx')):
				GrabdirectoryFile = textract.process(p)					
				directoryFile = GrabdirectoryFile.strip().decode('utf-8')					
				if args.show: 
					print (directoryFile)
					quit()
				buildList()	
				
			elif "text" in magic.from_file(p, mime=True):
				GrabdirectoryFile = open(p,"r",encoding='UTF8')					
				directoryFile = GrabdirectoryFile.read()
				if args.show:
					print (directoryFile)
				buildList()
	
		except:
			print ("  Could not read the file ",p)
			#raise
			pass

# Parse the files in -directory
def dirlist(path):

	global i
	
	if os.path.isfile(path):
		i = path
		LetsTry(path)
	elif os.path.isdir(path):
		
		for i in glob.glob(os.path.join(path, "*")):
			if os.path.isfile(i):
				LetsTry(i)
			
			elif os.path.isdir(i):
				dirname = os.path.basename(i)               
				dirlist(i)
			

path = os.path.normpath(args.input)
dirlist(path)		

OutputFile = open(output, "r",encoding='UTF8')
outputword = list(set(OutputFile.read().split()))
OutputLenEnd = len(outputword)
print (fg.GREEN,style.BRIGHT , OutputLenEnd , style.RESET_ALL,"in", args.output, "after being", fg.BLUE,style.BRIGHT, "Pukekoed"+ style.RESET_ALL)