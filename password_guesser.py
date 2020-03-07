#!/usr/bin/python

import sys
import datetime

def function1(word):
	wordlist.append(word)
	for pattern in patterns:
		wordlist.append(word+pattern)
	for delimiter in delimiters:
		for pattern in patterns:
			wordlist.append(word+delimiter+pattern)

words = sys.argv[1:]
patterns = ['1','12','123','456','1234','12345','123456','321','54321','2018','2019','2020']
delimiters = ['@','$','&','!']
delimiters2 = ['','.','_']
character_convert = {'a':'@','e':'3','o':'0','i':'!','s':'$','h':'#'}
wordlist = []

for word in words:
	function1(word)
for word in words:
	function1(word.capitalize())
for word in words:
	function1(word.upper())
for word in words:
	if len(word.split(" ")) > 1:
		function1(word.title())
		for item in delimiters2:
			test = word.replace(" ",item)
			function1(test)
			function1(test.capitalize())
for character in character_convert.keys():
	for item in wordlist:
		if character in item:
			wordlist.append(item.replace(character,character_convert[character]))

file = open("password_wordlist.txt","w")
for item in wordlist:
	file.write(item+"\n")

print "*"*50
print "-"*17 + "Passowrd Guesser" + "-"*17
print "-"*8 + "I-man : https://github.com/imnkrm/" + "-"*8
print "*"*50
print "\n" + str(len(wordlist)) + " words generated and written to \"password_wordlist.txt\""
