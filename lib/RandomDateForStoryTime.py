from random import seed 
from random import random
from random import choice
from random import randint
from datetime import datetime  
from datetime import timedelta  
import calendar
import math


def functionA():
	###### This is a number that changes the date by a random amount of days.
	dateChanger = randint(50000,500000)
	###### This is how many years apart today's date is with the new date
	dateDifference = round(dateChanger / 365.25)
	# I referenced https://pumas.nasa.gov/files/04_21_97_1.pdf 

	#storyYear = datetime.now() + timedelta(dateChanger)
	
	ops = ['+', '-']
	operator = choice(ops)
	#print(operator)
	if operator == '+':
		storyDate = datetime.now() + timedelta(dateChanger)
		storyYear = storyDate.year
		storyMonth = storyDate.month
		storyDay = storyDate.day
		yearsApart = str(dateDifference) + ' years in the future'
		
	else: 
		storyDate = datetime.now() - timedelta(dateChanger)	
		storyYear = storyDate.year
		storyMonth = storyDate.month
		storyDay = storyDate.day
		yearsApart = str(dateDifference) + " years ago"

	if storyMonth == 1:
		storyMonth = "January"
	if storyMonth == 2:
		storyMonth = "February"
	if storyMonth == 3:
		storyMonth = "March"
	if storyMonth == 4:
		storyMonth = "April"
	if storyMonth == 5:
		storyMonth = "May"
	if storyMonth == 6:
		storyMonth = "June"
	if storyMonth == 7:
		storyMonth = "July"
	if storyMonth == 8:
		storyMonth = "August"
	if storyMonth == 9:
		storyMonth = "September"
	if storyMonth == 10:
		storyMonth = "October"
	if storyMonth == 11:
		storyMonth = "November"
	if storyMonth == 12:
		storyMonth = "December"

	
	#today = datetime.now()
	
	print(dateDifference)
	print("the opperator was: " + operator)
	#storyYear = eval(str(datetime.now()) + operator + str(timedelta(dateChanger)))
	print("Year:", storyYear)
	print("Month:", storyMonth)
	print("Date:", storyDay)
	print('Day of Week (number): ', storyDate.weekday())
	print('Day of Week (name): ', calendar.day_name[storyDate.weekday()])
	print("This was", yearsApart)

	
	print("The year was", storyYear, "in the month of", storyMonth)
if __name__ == '__main__':
	functionA()

