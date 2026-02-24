#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import glob
import magic
import textract
import whisper
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


HOT_WORDS = [
	"password", "passwd", "passphrase", "passkey",
	"admin", "administrator", "sysadmin",
	"user", "login", "credentials", "auth", "2fa", "otp", "pin",
	"key", "S/N", "api_key", "secret_key", "encryption_key", "client_secret",
	"secret", "token", "bearer", "oauth",
	"hash", "salt",
	"ssn", "credit_card",
	"confidential", "-----BEGIN",
]

# Handled by textract (documents, images)
TEXTRACT_EXTENSIONS = (
	'.csv', '.doc', '.docx', '.eml', '.epub', '.gif', '.htm', '.html',
	'.jpeg', '.jpg', '.json', '.log', '.msg', '.odt',
	'.pdf', '.png', '.pptx', '.ps', '.psv', '.rtf', '.tff', '.tif',
	'.tiff', '.tsv', '.txt', '.xls', '.xlsx'
)

# Handled by Whisper (audio and video)
AUDIO_VIDEO_EXTENSIONS = (
	'.mp3', '.wav', '.ogg', '.flac', '.m4a', '.aac', '.wma',
	'.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'
)


def extract_text(path, whisper_model):
	"""Extract text from a file. Returns string or None if unsupported."""
	if path.lower().endswith(AUDIO_VIDEO_EXTENSIONS):
		print(fg.MAGENTA, style.BRIGHT, "  transcribing...", style.RESET_ALL, end='\r')
		result = whisper_model.transcribe(path)
		return result['text']
	elif path.lower().endswith(TEXTRACT_EXTENSIONS):
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
	parser = argparse.ArgumentParser(
		description=(
			"Pukeko — tailored wordlist generator for breach assessment.\n"
			"Scans a file or directory, extracts every unique word from all supported\n"
			"formats, and saves a deduplicated, sorted wordlist. Use the resulting\n"
			"wordlist to assess whether passwords or sensitive data were exposed in a leak.\n"
		),
		epilog=(
			"supported formats:\n"
			"  documents/images : .csv .doc .docx .eml .epub .gif .htm .html .jpeg .jpg\n"
			"                     .json .log .msg .odt .pdf .png .pptx .ps .psv .rtf\n"
			"                     .tff .tif .tiff .tsv .txt .xls .xlsx\n"
			"  audio/video      : .mp3 .wav .ogg .flac .m4a .aac .wma\n"
			"                     .mp4 .avi .mkv .mov .wmv .flv .webm .m4v\n"
			"  plain text       : any file detected as plain text (scripts, configs, etc.)\n"
			"\n"
			"examples:\n"
			"  python Pukeko.py -input /leak/dump -output wordlist.txt\n"
			"  python Pukeko.py -input /leak/dump -output wordlist.txt -model medium\n"
			"  python Pukeko.py -input /leak/dump -output wordlist.txt -hotwords\n"
			"  python Pukeko.py -input /leak/dump -output wordlist.txt -min 6 -max 30\n"
			"  python Pukeko.py -input document.pdf -output wordlist.txt -print\n"
		),
		formatter_class=argparse.RawDescriptionHelpFormatter
	)
	parser.add_argument('-input',    dest='input',    help="path to a file or directory to scan", metavar='PATH')
	parser.add_argument('-output',   dest='output',   help="path to the output wordlist file", metavar='FILE')
	parser.add_argument('-print',    dest='show',     action='store_true', help="print the extracted text of each file to stdout")
	parser.add_argument('-hotwords', dest='hotwords', action='store_true', help="highlight lines containing sensitive keywords (passwords, tokens, keys, etc.)")
	parser.add_argument('-min',      dest='min',      default=4, type=int, help="minimum word length to include (default: 4)", metavar='N')
	parser.add_argument('-max',      dest='max',      default=20, type=int, help="maximum word length to include (default: 20)", metavar='N')
	parser.add_argument('-model',    dest='model',    default='small', choices=['tiny', 'base', 'small', 'medium', 'large'],
	                                                  help="Whisper model for audio/video transcription: tiny/base/small(default)/medium/large")

	args = parser.parse_args()

	if len(sys.argv) < 2:
		parser.print_help()
		sys.exit(1)

	output = args.output

	# Load Whisper model once
	print(fg.BLUE, style.BRIGHT, "Loading Whisper model:", args.model, style.RESET_ALL)
	whisper_model = whisper.load_model(args.model)

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
			text = extract_text(filepath, whisper_model)
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
