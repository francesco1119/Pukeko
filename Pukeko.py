#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import glob
import magic
import textract
import colorama
colorama.init()

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


HOT_WORDS = ["password", "admin", "S/N", "key", "administrator", "sysadmin"]

SUPPORTED_EXTENSIONS = (
	'.csv', '.doc', '.docx', '.eml', '.epub', '.gif', '.htm', '.html',
	'.jpeg', '.jpg', '.json', '.log', '.mp3', '.msg', '.odt', '.ogg',
	'.pdf', '.png', '.pptx', '.ps', '.psv', '.rtf', '.tff', '.tif',
	'.tiff', '.tsv', '.txt', '.wav', '.xls', '.xlsx'
)


def extract_text(path):
	"""Extract text from a file. Returns string or None if unsupported."""
	if path.lower().endswith(SUPPORTED_EXTENSIONS):
		raw = textract.process(path)
		return raw.strip().decode('utf-8')
	elif "text" in magic.from_file(path, mime=True):
		with open(path, "r", encoding='UTF8') as f:
			return f.read()
	return None


def find_files(path):
	"""Recursively yield all file paths under path."""
	if os.path.isfile(path):
		yield path
	elif os.path.isdir(path):
		for entry in glob.glob(os.path.join(path, "*")):
			if os.path.isfile(entry):
				yield entry
			elif os.path.isdir(entry):
				yield from find_files(entry)


def check_hotwords(text, filepath):
	"""Print lines containing hotwords."""
	for line_no, line in enumerate(text.splitlines()):
		if any(word.lower() in line.lower() for word in HOT_WORDS):
			print("\t", fg.CYAN, style.BRIGHT, line_no, ':', line, style.RESET_ALL)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-input',    dest='input',    help="input a directory or a file", metavar=None)
	parser.add_argument('-output',   dest='output',   help="output words into a file", metavar=None)
	parser.add_argument('-print',    dest='show',     action='store_true', help="show what Pukeko is reading")
	parser.add_argument('-hotwords', dest='hotwords', action='store_true', help="show rows that contains HotWords")
	parser.add_argument('-min',      dest='min',      default=4, type=int, help="Minimum word length (by default is 4)", metavar=None)
	parser.add_argument('-max',      dest='max',      default=20, type=int, help="Maximum word length (by default is 20)", metavar=None)

	args = parser.parse_args()

	if len(sys.argv) < 2:
		parser.print_help()
		sys.exit(1)

	output = args.output

	# Load existing wordlist into memory
	wordset = set()
	if os.path.exists(output):
		with open(output, "r", encoding='UTF8') as f:
			wordset = set(f.read().split())
		print(fg.RED, style.BRIGHT, len(wordset), style.RESET_ALL,
			  "in", output, "before being", fg.BLUE, style.BRIGHT, "Pukekoed", style.RESET_ALL)

	# Process all input files, accumulating words in memory
	input_path = os.path.normpath(args.input)
	for filepath in find_files(input_path):
		try:
			text = extract_text(filepath)
			if text is None:
				continue

			if args.show:
				print(text)

			new_words = set(text.split())
			size_before = len(wordset)
			wordset.update(new_words)
			added = len(wordset) - size_before
			print(fg.YELLOW, style.BRIGHT, "+", added, style.RESET_ALL, filepath)

			if args.hotwords:
				check_hotwords(text, filepath)

		except Exception as e:
			print("  Could not read the file", filepath, ":", e)

	# Filter by length, sort, then write once — safely
	filtered = sorted(
		[w for w in wordset if args.min <= len(w) <= args.max],
		key=len
	)

	with open(output, "w", encoding='UTF8') as f:
		for word in filtered:
			f.write(word + "\n")

	print(fg.GREEN, style.BRIGHT, len(filtered), style.RESET_ALL,
		  "in", output, "after being", fg.BLUE, style.BRIGHT, "Pukekoed" + style.RESET_ALL)


if __name__ == '__main__':
	main()
