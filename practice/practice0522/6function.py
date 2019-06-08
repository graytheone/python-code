#play the game
def goldroom():
	print('This room is full of gold. How much do you take?')

	choice = input('>')
	if'0' in choice or '1' in choice:
		howmuch = int(choice)
	else:
		dead('Man,learn to type a number')

	if howmuch < 50:
		print('Nice,you are not greedy, you win !')
		exit(0)
	else:
		dead('You greedy bastard')

def bearroom():
	print('There is a bear here')
	print('The bear has a bunch of honey')
	print('The fat bear is in front of another door')
	print('How are  you going to move the bear')
	bearmoved = False
	
	while True:
		choice = input('>')
		
		if choice == 'take honey':
			dead('The bear looks at you then slaps your face off.')
		elif choice == 'tanut bear' and not bearmoved:
			print('The bear has moved from the door')
			print('You can go through it now')
			bearmoved = True
		elif choice == 'tanut bear' and bearmoved:
			dead('The bear gets pissed off and chews your leg off.')
		elif choice == 'open door' and bearmoved:
			goldroom()
		else:
			('I got no idea what that means')

def cthulhuroom():
	print('Here you see the great evil Cthulhu.')
	print('He,it,whatever stares at you and you go insane.')
	print('Do you flee for your life or eat your head?')

	choice = input('>')
	
	if 'flee' in choice:
		start()
1.编写程序，输入三角形的3条边长，求其面积。注意：三角形的任意三边，对于不合理边长的输入，要求给出错误提示。
	elif'head' in choice:
		dead('Well that was tasty!')
	else:
		cthulhuroom()

def dead(why):
	print(why , 'Good job!')
	exit(0)

def start():
	print('Your are in a dark room.')
	print('There is a door to your right and left.')
	print('Which one do you take.')

	choice = input('>')

	if choice == 'left':
		bearroom()
	if choice == 'right':
		cthulhuroom()
	else:
		dead('You stumble around the room until you starve.')


start()
		
















































































