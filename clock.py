import os,time,platform
system = platform.system()
# print("Hello world!")

# x = input()

# os.system("clear")

# don't use gmttime() otherwise u have to convert the time zones
t = time.localtime()
pt = t
# print(t)

# This program works like a digital clock that prints the current time on console in a designed fashion
# while True:
# 	t = time.localtime()
# 	while pt.tm_sec != t.tm_sec:
# 		print(t.tm_hour,t.tm_min,t.tm_sec)
# 		pt = t

'''
05:25:47 will look like
██████████████████████████████████████████████████████████████
██                                                          ██
██  ██████  ██████      ██████  ██████      ██  ██  ██████  ██                  
██  ██  ██  ██      ██      ██  ██      ██  ██  ██      ██  ██     
██  ██  ██  ██████      ██████  ██████      ██████      ██  ██               
██  ██  ██      ██  ██  ██          ██  ██      ██      ██  ██   
██  ██████  ██████      ██████  ██████          ██      ██  ██           
██                                                          ██
██████████████████████████████████████████████████████████████

                                  
   ██████                          
   ██  ██
   ██████                            
   ██  ██                           
   ██████                             

'''


digits = [
[
"██████",
"██  ██",
"██  ██",
"██  ██",
"██████"
],
[
"  ██  ",
"  ██  ",
"  ██  ",
"  ██  ",
"  ██  "
],
[
"██████",
"    ██",
"██████",
"██    ",
"██████"
],
[
"██████",
"    ██",
"  ████",
"    ██",
"██████"
],
[
"██  ██",
"██  ██",
"██████",
"    ██",
"    ██"
],
[
"██████",
"██    ",
"██████",
"    ██",
"██████"
],
[
"██████",
"██    ",
"██████",
"██  ██",
"██████"
],
[
"██████",
"    ██",
"    ██",
"    ██",
"    ██"
],
[
"██████",
"██  ██",
"██████",
"██  ██",
"██████"
],
[
"██████",
"██  ██",
"██████",
"    ██",
"██████"
]
]

colon = [
"      ",
"  ██  ",
"      ",
"  ██  ",
"      "
]

# rendering one digit successful
# print(digits[8])

# rendering 2 digits side by side
n = 71
a,b = n//10,n%10
numbers = ""
for i in range(5):
	numbers += digits[a][i] + "  " + digits[b][i] + "\n"

# print(numbers)

# # render a string of form "hh:mm:ss"
# h = 88
# ha,hb = h//10,h%10
# m = 99
# ma,mb = m//10,m%10
# s = 00
# sa,sb = s//10,s%10

# display =  "██████████████████████████████████████████████████████████████\n"
# display += "██                                                          ██\n"
# for i in range(5):

# 	display += "██  "

# 	# hours
# 	display += digits[ha][i] + "  " + digits[hb][i]

# 	# colon
# 	display += colon[i]

# 	# minutes
# 	display += digits[ma][i] + "  " + digits[mb][i]
	
# 	# colon
# 	display += colon[i]

# 	# seconds
# 	display += digits[sa][i] + "  " + digits[sb][i]

# 	display += "  ██\n"

# display += "██                                                          ██\n"
# display += "██████████████████████████████████████████████████████████████\n"


# # print(display)

def constructString(h,m,s):
	ha,hb = h//10,h%10
	ma,mb = m//10,m%10
	sa,sb = s//10,s%10

	display =  "██████████████████████████████████████████████████████████████\n"
	display += "██                                                          ██\n"
	for i in range(5):

		display += "██  "

		# hours
		display += digits[ha][i] + "  " + digits[hb][i]

		# colon
		display += colon[i]

		# minutes
		display += digits[ma][i] + "  " + digits[mb][i]
		
		# colon
		display += colon[i]

		# seconds
		display += digits[sa][i] + "  " + digits[sb][i]

		display += "  ██\n"

	display += "██                                                          ██\n"
	display += "██████████████████████████████████████████████████████████████\n"

	return display

# print(constructString(4,5,6))	

while True:
	t = time.localtime()
	while pt.tm_sec != t.tm_sec:
		# try:
		# 	os.system("cls")
		# except e:
		# 	os.system("clear")
		
		if (system == "Windows"):
			os.system("cls")
		else :
			os.system("clear")


		print(constructString(t.tm_hour,t.tm_min,t.tm_sec))
		pt = t




