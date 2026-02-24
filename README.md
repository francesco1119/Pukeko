<p align="center">
<img alt="Pukeko" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Australasian_swamphen_%28Porphyrio_melanotus%29_Tiritiri_Matangi.jpg/1920px-Australasian_swamphen_%28Porphyrio_melanotus%29_Tiritiri_Matangi.jpg" />
<p align="center">
<a href="https://github.com/francesco1119/Pukeko/issues"><img alt="issues" src="https://img.shields.io/github/issues/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/network"><img alt="network" src="https://img.shields.io/github/forks/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/stargazers"><img alt="stargazers" src="https://img.shields.io/github/stars/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/blob/master/LICENSE"><img alt="LICENSE" src="https://img.shields.io/github/license/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/commits/master"><img alt="last commit" src="https://img.shields.io/github/last-commit/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/graphs/commit-activity"><img alt="commit activity" src="https://img.shields.io/github/commit-activity/m/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko"><img alt="repo size" src="https://img.shields.io/github/repo-size/francesco1119/Pukeko.svg"></a>
<a href="https://github.com/francesco1119/Pukeko/watchers"><img alt="watchers" src="https://img.shields.io/github/watchers/francesco1119/Pukeko.svg"></a>
<img alt="python" src="https://img.shields.io/badge/python-3.x-blue.svg">
</p>
</p>

## Pukeko
#### Pukeko goes in the wild, create tailored wordlists and enumerate credentials from a local folder

Tired of using `sort input.txt | uniq > output.txt` I wanted to create a cross OS script that could read any possible file, take each word once, and list them all in a word-list. 

How to Install
======

1) `pip install argparse glob python-magic textract colorama`

#### Troubleshooting:

- **python-magic:** as if the World wasn't complicated enough, there are 2 'Magic' libraries. You can find the right one [here on GitHub](https://github.com/ahupp/python-magic) or [here on pypi.python.org](https://pypi.python.org/pypi/python-magic/)
- **textract:** this too is not easy to install, you can find detailed documentation [here on GitHub](https://github.com/deanmalmgren/textract) or on the [official website](https://textract.readthedocs.io/en/stable/index.html) or on the [formal pypi.python.org](https://pypi.python.org/pypi/textract) 

If the situation gets tragic open an issue and I will help you troubleshooting 

How to use it 
------

Pukeko can currently parse: `'.csv', '.doc', '.docx', '.eml', '.epub', '.gif', '.htm', '.html', '.jpeg', '.jpg', '.json', '.log', '.mp3', '.msg', '.odt', '.ogg', '.pdf', '.png', '.pptx', '.ps', '.psv', '.rtf', '.tff', '.tif', '.tiff', '.tsv', '.txt', '.wav', '.xls', '.xlsx'` plus any file identified as plain text by the system (e.g. `.py`, `.js`, `.xml`, shell scripts, config files, and other text-based formats).

Have a look at my YouTube presentatoin:

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

