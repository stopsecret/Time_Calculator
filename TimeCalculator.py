
#################################################################################
#
#	Time Sheet Input Calculator. 
#	Copyright 2013 Stopsecret Design.
#	If you enjoyed, please leave a comment on my website.
#	http://stopsecretdesign.wordpress.com/
#
#	You are free to use this script for yourself and your personal projects.
#
#################################################################################


#The bulk of the processing takes place in this main function, responsible for taking two input strings and outputting time worked in hours
def hours_calc(inputhoursstart, inputhoursend):

	#if we don't find a colon in the input string, it's not a valid input and we return an error
	if parsetime(inputhoursstart) == -1 or parsetime(inputhoursend) == -1:
		return "Error! Please make sure input is in <hour>:<minutes> form and try again!"
		
	#otherwise, we get the start time in minutes, and the end time in minutes
	minstart = parsetime(inputhoursstart)
	minend = parsetime(inputhoursend)
	
	#now, if the end time is less than the start time, we need to add 720 minutes (12 hours) to compensate
	if(minend < minstart):
		minend += 720
		
	#take the difference of the minutes to see how long the distance between the two is
	endresult = minend - minstart
	
	#we now round to the nearest hour
	endresulthours = int(endresult/60)
	
	#to get the leftover minutes, we multiply by 60 and subtract the original value. We then take the absolute value of this.
	leftover = abs((endresulthours*60) - endresult)
	
	#return a string telling how long we worked
	return "\n\nYou worked:\n{0}:{1}\n({0} hours and {1} minutes)".format(endresulthours, leftover)

#parse time returns the time as a minutes value
def parsetime(inputstring):
	#if there's no colon, return a value of -1
	if(inputstring.find(":") == -1):
		return -1
	#get the beginning number
	firstpart = int(inputstring[:inputstring.find(":")])
	#get the end number
	secondpart = int(inputstring[(inputstring.find(":") + 1):])
	#multiply the hours by 60 to turn them into minutes
	firstpart *= 60
	#add both these values together
	endresult = firstpart+secondpart
	#return the added values
	return endresult

def input_new_hours():
	#this is the user-end of things for putting in new hours.
	print("Input hours below:\n")
	#get both string input values
	inputstart = raw_input("When did you start working? (H:M)\n\n\n");
	inputend = raw_input("When did you end working? (H:M)\n\n");
	#print the results of the calculation
	print(hours_calc(inputstart, inputend))

#a border to make things look nice
border = "_______________________________________________________________"
print ("{0}\nTime Sheet Input Calculator. Copyright 2013 Stopsecret Design.\nIf you enjoyed, please leave a comment on my website.\nhttp://stopsecretdesign.wordpress.com/\n{0}\n\n".format(border))

#run the intial solve from the start
input_new_hours()

#go into this loop if the user wants to calculate more than one time slot
while True:
	new = raw_input("\nDo you want to add another time?\n");
	#if the user does, redo the calculation
	if(new.lower() == "yes" or new.lower() == "yeah" or new.lower() == "sure" or new.lower() == "y"):
		input_new_hours()
	#if not, then break
	else:
		break
		
#display a logout message at the end
print ("{0}\nThanks for using!\n{0}\n\n".format(border))
		
