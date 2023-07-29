logo = """
$$\      $$\ $$\   $$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  
$$$\    $$$ |$$ |  $$ |$$  _____|$$  __$$\ $$  __$$\ 
$$$$\  $$$$ |$$ |  $$ |$$ |      $$ /  $$ |$$ |  $$ |
$$\$$\$$ $$ |$$ |  $$ |$$$$$\    $$ |  $$ |$$$$$$$  |
$$ \$$$  $$ |$$ |  $$ |$$  __|   $$ |  $$ |$$  __$$< 
$$ |\$  /$$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$  |$$$$$$$$\  $$$$$$  |$$ |  $$ |
\__|     \__| \______/ \________| \______/ \__|  \__|
"""
loop = 0
ok = []:;
cp = []:
def main():
	os.system("clear")
	print(logo)
	print(47*'\033[92;1m-')
	print(" \x1b[1;95m[1] \x1b[1;95mStart Cloning")
	print(" \x1b[1;96m[2] \x1b[1;96mOwner Contact  ")
	print(" \x1b[1;97m[3] \x1b[1;97mJoin telegram group   ")
	print(" \x1b[1;98m[0] \x1b[1;92mExit")
	print(47*'\033[92;1m-')
	MUEORðŸ¤¬_select():

def MUEORðŸ¤¬_select():
	MUEORðŸ¤¬ = input('\n\x1b[1;93m[+] Choose Option: \x1b[1;92m')
	if MUEORðŸ¤¬ == '':
		print("\x1b[1;91mFill in correctly")
		main()
	elif MUEORðŸ¤¬ == '1':
		MUEORðŸ¤¬_TRICKER()
	elif MUEORðŸ¤¬ == '2':
		os.system('xdg-open https://www.facebook.com/mueor')
		main()
	elif MUEORðŸ¤¬ == '3':
		os.system('xdg-open https://t.me/mueorb')
		main()
	elif MUEORðŸ¤¬ == '0':
		os.system('exit')
	else:
		print ('\x1b[1;91m[!] Please select a valid option')
		time.sleep(2)
		main()

   
def MUEORðŸ¤¬_TRICKER():
	os.system('clear')
	print(logo)
	os.system('xdg-open https://www.facebook.com/profile.php?id=100007946797233')
	print('\x1b[1;92m[1]\x1b[1;93m Random UID Cloning')
	print('\x1b[1;92m[0]\x1b[1;94m Back')
	print(47*'\033[92;1m-')
	print ("")
	opt = input('\x1b[1;93m[+] Choose option: \x1b[1;92m')
	if opt =='1':
		method()
	elif opt =='0':
		main()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		MUEORðŸ¤¬_KING()
		
def method():
	os.system('clear')
	print(logo)
	os.system('xdg-open https://www.facebook.com/profile.php?id=100007946797233')
	print('\x1b[1;92m[1]\x1b[1;93m Method1  \x1b[1;92m[Ok idz] \x1b[1;93m[BEST]')
	print('\x1b[1;92m[2]\x1b[1;94m Method2  \x1b[1;92m[Ok idz]')
	print('\x1b[1;92m[0]\x1b[1;95m Back')
	print(47*'\033[92;1m-')
	print ("")
	opt = input('\x1b[1;93m[+] Choose option: \x1b[1;92m')
	if opt =='1':
		method1()
	elif opt =='2':
		method2()
	elif opt =='0':
		MUEORðŸ¤¬_KING()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		method()
