# Challenge level: Beginner

# Scenario: You have two files containing a list of email addresses of people who attended your events.
#       File 1: People who attended your Film Screening event
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/film_screening_attendees.txt
#
#       File 2: People who attended your Happy hour
#       https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/happy_hour_attendees.txt
#

# Note: You should create functions to accomplish your goals.

# Goal 1: You want to get a de-duplicated list of all of the people who have come to your events.

def deduplicate(files):
	"""Takes a list of files as input, returns list of deduplicate items from files"""
	individuals = []
	for file in files:
		with open(file) as open_file:
			individuals.extend(open_file.read().split('\n'))
	return list(set(individuals))

print(deduplicate(['film_screening_attendees.txt', 'happy_hour_attendees.txt']))


# Goal 2: Who came to *both* your Film Screening and your Happy hour?

def get_duplicates(file1, file2):
	"""Takes two files as input, returns list of items that appear in both files."""
	with open(file1) as open_file_1:
		individuals_1 = open_file_1.read().split('\n')

	with open(file2) as open_file_2:
		individuals_2 = open_file_2.read().split('\n')

	duplicates = []
	for item in individuals_1:
		if item in individuals_2:
			duplicates.append(item)
	return(duplicates)

print(get_duplicates('film_screening_attendees.txt', 'happy_hour_attendees.txt'))
