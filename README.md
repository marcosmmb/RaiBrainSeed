# Rai Brain Seed
A brain seed algorithm for Nano

----

![screenshot](https://i.imgur.com/TZiGo5o.png)

**How to use**

 1. [Install python 3](https://www.python.org/downloads/)
 2. Clone the repository to a paste
 3. Run the command prompt on this paste
 4. Run the following command:

    $ python3 RaiBrainSeed.py

 5. Now you can insert a phrase in the text field. Be sure to choose a long and unique phrase, this is like a password
 6. Click on Generate seed button to generate the seed
 7. Copy and paste your seed wherever you want

**How to test your seed**

This algorithm was made so you can try it yourself with paper and pen:

 - Choose a long and difficult phrase
 - Enumerate using [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) and [ASCII](http://knoow.net/wp-content/uploads/2016/01/ASCII-Table.png) order each unique character of your phrase
 - So if your phrase is "Hello World", your enumerated list must be "H W d e l o r"
 - Using the hexadecimal pattern, you must enumerate this list such as: 

> H = 0
> W = 1
> d = 2
> e = 3
> l = 4
> o = 5
> r = 6

*If we had more unique characters, we would continue listing up to 'F' (F is hexadecimal for 15), and we would repeat the process if we had more than 16 unique characters.*

 - Now you must translate your phrase to the correspondent hexadecimal number:

> Hello World = 03445 15642

 - Now, since this string has less than 64 characters, we concatenate it until it has 64 characters: 
 *0344515642034451564203445156420344515642034451564203445156420344*

Example:

> Phrase -> The quick brown fox jumps over the lazy dog
> Seed -> 0851593B22F7E6F8A5D03F652485C1A94F70851593B22F7E6F8A5D03F652485C


