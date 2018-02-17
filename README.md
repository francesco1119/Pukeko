## Pukeko
#### Pukeko goes in the wild, create tailored wordlists and enumerate credentials from a local folder
 
![alt text](http://www.gisbornespecials.co.nz/assets/ZOO/ZOO-Pukeko-800461.jpg)

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

Pukeko can currently parse: `'.csv', '.doc', '.docx', '.eml', '.epub', '.gif', '.htm', '.html', '.jpeg', '.jpg', '.json', '.log', '.mp3', '.msg', '.odt', '.ogg', '.pdf', '.png', '.pptx', '.ps', '.psv', '.rtf', '.tff', '.tif', '.tiff', '.tsv', '.txt', '.wav', '.xls', '.xlsx'.`

Have a look at my YouTube presentatoin:

[![IMAGE ALT TEXT HERE](https://github.com/francesco1119/Pukeko/blob/master/Capture.PNG?raw=true)](https://youtu.be/CD1zNNGDrUQ)

Future developent
------
On spare time my TODO list is:

* add option `-URL` to create wordlists from a target web page
* add option `-site` to create wordlists from a target website
* add option `Leet` (or `1337`), also known as `eleet` or `leetspeak` (so many passwords are week because of  [leetspeak](https://optimwise.com/passwords-with-simple-character-substitution-are-weak/) )
* add multilanguage (`pip install alphabet-detector`)
* add highlight HotWord in string

