# Challenge level: Beginner

# Goal: Using the code from Lesson 3: File handling and dictionaries, create a 
# function that will open a CSV file and return the result as a nested list.

def to_nested_list(file):
	with open(file) as open_file:
		rows = open_file.read().split('\n')

	output = []
	for row in rows:
		output.append(row.split(','))

	return output

print(to_nested_list('contacts.csv'))