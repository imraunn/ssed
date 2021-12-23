
# Semi Smart Esolang Decryptor(SSED) #
A semi-smart python3 project that detects with high accuracy the type of Esolang and then proceeds to decrypt it
> "An esoteric programming language, or esolang, is a computer programming language designed to experiment with weird ideas, to be hard to program in, or as a joke, rather than for practical use."
> ***https://esolangs.org/***

## Installation

1)`git clone https://github.com/imraunn/ssed.git`

2)`cd ssed`

3)`pip3 install -r requirements.txt`


## Usage

### Detect

Detect/index.py imports the database from ./database.txt and displays percentage/hits found on a language.

**Example:**

`python3 index.py ascii_art.txt c`

The input file is ascii_art.txt and it is suspected that the language is c(har) type.

`python3 index.py pikalang.txt w`

The input file is pikalang.txt and it is suspected that the language is w(ord) type.


### Webscraper



* `x <<keywords separated by space>>`

	This will filter keywords entered by the user from the dumped code snippets. Probable codes containing
	those keywords will not be displayed.

	 **Example:** `x echo import`
	 Snippets containing echo and import will not be shown while running code_extract.py

* `c/w <<counters separated by space>>`

	 Use  c for character type esolang
	 Use w for word type esolang
	 Enter counter numbers separated by space that need to be saved in the database

	 **Example:**

	`c 1 2 9` snippets 1,2,9 will be processed and saved in database as char type
	`w 3 8 11` snippets 3,8,11 will be processed and saved in database as word type

* `mc <<characters without spacing>>`

     This is for manual entry of characters of an esolang

	` mw <<words separated by space`

	This is for manual entry of words of an esolang

	If the probable codes aren't sufficient or contain comments, in such scenarios, this format can be used.

	**Example:** `mc ?!+$`  `mw pika pi pikaa`
* `q`

	This keyword will terminate the program and save all the progress in /storage/
Charsets and wordsets will be generated and saved. Due to local storage, the program will continue from where it was left.

* `r`

	This keyword will save the language for later review in review_later.txt



Made with :heart: by Raunak Asnani, under the supervision of Cyber Labs, IIT (ISM) Dhanbad WoC 2020.
