<p align="center">
<img alt="Pukeko" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Australasian_swamphen_%28Porphyrio_melanotus%29_Tiritiri_Matangi.jpg/1920px-Australasian_swamphen_%28Porphyrio_melanotus%29_Tiritiri_Matangi.jpg" />
<p align="center">
<a href="https://github.com/francesco1119/Pukeko/network"><img alt="network" src="https://img.shields.io/github/forks/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/stargazers"><img alt="stargazers" src="https://img.shields.io/github/stars/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/blob/master/LICENSE"><img alt="LICENSE" src="https://img.shields.io/github/license/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/commits/master"><img alt="last commit" src="https://img.shields.io/github/last-commit/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/watchers"><img alt="watchers" src="https://img.shields.io/github/watchers/francesco1119/Pukeko.svg"></a>
<img alt="python" src="https://img.shields.io/badge/python-3.x-blue.svg">
</p>
</p>

## Pukeko
#### Pukeko goes in the wild, create tailored wordlists and enumerate credentials from a local folder

Tired of using `sort input.txt | uniq > output.txt` I wanted to create a cross OS script that could read any possible file, take each word once, and list them all in a word-list. 

Requirements
======

#### Python packages (required)

| Package | Purpose | Install |
|---------|---------|---------|
| `python-magic` | Detect plain text files by content | `pip install python-magic` |
| `pyxtxt` | Extract text from all document and image formats | `pip install pyxtxt` |
| `openai-whisper` | Transcribe audio and video locally | `pip install openai-whisper` |
| `colorama` | Colour terminal output on all platforms | `pip install colorama` |

Install all at once:
```
pip install python-magic openai-whisper colorama pyxtxt
```

For broader format coverage install pyxtxt with optional extras:
```
pip install "pyxtxt[pdf,docx,presentation,spreadsheet,html,ocr]"
```

#### System tools (required for certain file types)

| Tool | Purpose | Without it |
|------|---------|------------|
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | Extract text from images (`.jpg`, `.png`, `.gif`, `.tif`) | Images will be skipped |
| [ffmpeg](https://ffmpeg.org/) | Decode audio and video for Whisper | Audio/video will not work |

Pukeko will warn you at startup if any system tool is missing.

How to Install
======

1) `pip install python-magic openai-whisper colorama pyxtxt`

2) Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for image support

3) Install [ffmpeg](https://ffmpeg.org/download.html) for audio/video support

#### Troubleshooting:

- **python-magic:** as if the World wasn't complicated enough, there are 2 'Magic' libraries. You can find the right one [here on GitHub](https://github.com/ahupp/python-magic) or [here on pypi.python.org](https://pypi.python.org/pypi/python-magic/)
- **openai-whisper:** runs fully locally — no API key, no internet, no token limits. See the [GitHub repo](https://github.com/openai/whisper) for details. A GPU is optional but speeds up transcription significantly.
- **pyxtxt:** supports many formats out of the box; install with extras (`pyxtxt[ocr]`, `pyxtxt[pdf]`, etc.) for broader coverage. See the [pyxtxt PyPI page](https://pypi.org/project/pyxtxt/) for the full list.

If the situation gets tragic open an issue and I will help you troubleshooting

How to use it
------

Pukeko can currently parse:

**Documents & images** (via `pyxtxt`): `'.csv', '.doc', '.docx', '.eml', '.epub', '.gif', '.htm', '.html', '.jpeg', '.jpg', '.json', '.log', '.msg', '.odt', '.pdf', '.png', '.pptx', '.ps', '.psv', '.rtf', '.tff', '.tif', '.tiff', '.tsv', '.txt', '.xls', '.xlsx'`

**Audio & video** (via `openai-whisper`, transcribed locally): `'.mp3', '.wav', '.ogg', '.flac', '.m4a', '.aac', '.wma', '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'`

**Plain text files** (via `python-magic`): any file identified as plain text by the system, e.g. `.py`, `.js`, `.xml`, shell scripts, config files, and other text-based formats.

The `-model` flag lets you choose the Whisper model size for audio/video transcription:

| Model | Speed | Accuracy |
|-------|-------|----------|
| `tiny` | fastest | lowest |
| `base` | fast | low |
| `small` | balanced | good (default) |
| `medium` | slow | very good |
| `large` | slowest | best |

Example: `python Pukeko.py -input /path/to/files -output wordlist.txt -model medium`

Have a look at my YouTube presentation:

[![IMAGE ALT TEXT HERE](https://github.com/francesco1119/Pukeko/blob/master/Capture.PNG?raw=true)](https://youtu.be/CD1zNNGDrUQ)

Future developent
------
On spare time my TODO list is:

* add option `-URL` to create wordlists from a target web page like [CeWL](https://github.com/digininja/CeWL)
* add option `-site` to create wordlists from a target website
* add option `Leet` (or `1337`), also known as `eleet` or `leetspeak` (so many passwords are week because of  [leetspeak](https://optimwise.com/passwords-with-simple-character-substitution-are-weak/) )
* add multilanguage (`pip install alphabet-detector`)
* add highlight HotWords in string
* add e-mail to HotWords

