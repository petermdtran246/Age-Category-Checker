def CheckAge(age):
    # Check if the age is between 12 and 50 (inclusive)
	if age >= 12 and age <= 50:
		print('young')
	else:
		print('not young')

# Declare age variable
age = int(input('Enter your age:\n'))
# Call the CheckAge function
CheckAge(age)

