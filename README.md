# seoish.py
Need a lot of variants of your text? Fear no more.

Now you can make text like this:

```
Word1 word2 [word3|word3_synonym1|word3_synonym2] word4. [Word5 word6 word7|Word8 word6 word9] word, word etc
```

and have all the variants or some of them.

#### Usage

```
seoish.py [-h] [-i INPUTFILE] [-o OUTPUTFILE] [-c COUNT]
```

#### Example

Let's say:

input.txt 

As an Internet marketing [strategy|tactics|approach], SEO [considers|recognizes|regards] how search engines work, the computer programmed algorithms which dictate search engine [behavior|performance], what people search for, the [actual|real|original] search terms or keywords [typed|keyboarded|typewritten] into search engines, and which search engines are preferred by their targeted audience.

Command line:

```
seoish.py -i input.txt  -o output.txt -c 3
```
The output.txt will be:

As an Internet marketing tactics, SEO regards how search engines work, the computer programmed algorithms which dictate search engine behavior, what people search for, the original search terms or keywords keyboarded into search engines, and which search engines are preferred by their targeted audience. 
__________________________________________________
As an Internet marketing tactics, SEO recognizes how search engines work, the computer programmed algorithms which dictate search engine performance, what people search for, the real search terms or keywords keyboarded into search engines, and which search engines are preferred by their targeted audience. 
__________________________________________________
As an Internet marketing approach, SEO recognizes how search engines work, the computer programmed algorithms which dictate search engine behavior, what people search for, the real search terms or keywords typewritten into search engines, and which search engines are preferred by their targeted audience. 
__________________________________________________

