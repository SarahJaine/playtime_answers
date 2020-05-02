# Lesson 3
# Difficulty level: Beginner
# From https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_pbj_while.py

# Goal #1: Write a new version of the PB&J program that uses a while loop.  
# Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

bread = 4
peanut_butter = 3
jelly = 10

sandwiches = 0
while bread > 1 and peanut_butter > 0 and jelly > 1:
	sandwiches += 1
	print('Making sandwich #'+str(sandwiches))
	bread -= 2
	peanut_butter -= 1
	jelly -= 1

print("All done; only had enough bread for {0} sandwiches.".format(sandwiches))

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

bread = 12
peanut_butter = 5
jelly = 5

sandwiches = 0
while bread > 1 and peanut_butter > 0 and jelly > 0:
	sandwiches += 1
	print('Making sandwich #'+str(sandwiches))
	bread -= 2
	peanut_butter -= 1
	jelly -= 1
	
	# Note: We only need to do this with python3. In python2: 7/2 = 3.
	# Force python3 to use ints so it behaves like python2.
	bread_pairs = int(bread/2)

	print('''\t\tI have enough bread for {0} more sandwiches, 
		enough peanut butter for {1} more, 
		and enough jelly for {2} more.'''.format(bread_pairs, peanut_butter, jelly))

missing_ingredients = []
if bread_pairs == 0:
	missing_ingredients.append('bread')
if peanut_butter == 0:
	missing_ingredients.append('peanut butter')
if jelly == 0:
	missing_ingredients.append('jelly')

print("All done; I ran out of: {0}.".format(missing_ingredients))

