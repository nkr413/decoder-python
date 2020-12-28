#import decoder_data
from decoder_data import one, two, the
import random

def createKey(txt, data, randNum, base):
	for i in txt: data.append(base[i])
	if randNum == 1: data.insert(0, "-")
	elif randNum == 2: data.append("-")
	elif randNum == 3: data.insert(0, "/")

	res = ''.join(data)
	print(res, '\n')

def searchKey(txt, dataOne, dataTwo, dataThe):
	if txt[0] == '-':
		txt = txt[1:]

		for i in txt: dataOne.append(one[i])
		res = ''.join(dataOne)

	elif txt[-1] == '-':
		txt = txt[:-1]

		for i in txt: dataTwo.append(two[i])
		res = ''.join(dataTwo)

	elif txt[0] == '/':
		txt = txt[1:]

		for i in txt: dataThe.append(the[i])
		res = ''.join(dataThe)

	else: return
	print(res + " \n")

def decoder():
	dataOne = []
	dataTwo = []
	dataThe = []

	decod = input("Encrypt (1) or Decrypt (2) ?: ")

	txt = input("Enter a word: ").lower()
	txt = list(txt)

	if decod == '1':
		randNum = random.randint(1, 3)
		if randNum == 1: createKey(txt, dataOne, randNum, one)
		elif randNum == 2: createKey(txt, dataTwo, randNum, two)
		elif randNum == 3: createKey(txt, dataThe, randNum, the)
		else: return

	elif decod == '2': searchKey(txt, dataOne, dataTwo, dataThe)
	else: return
				
	question = input("Again ? (yes) or (no): ")
	if question == "yes": decoder()
	else: return

def startDecode():
	print('___DECODER___\n')
	decoder()

startDecode()


