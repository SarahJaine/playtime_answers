# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.
contacts = {
    'Shannon': {
        'phone': '202-555-1234',
        'twitter': '@svt827',
        'github': '@shannonturner'
    },
    'Beyonce': {
        'phone': '303-404-9876',
        'twitter': '@beyonce',
        'github': '@bey'
    },
    'Tegan and Sara': {
        'phone': '301-777-3313',
        'twitter': '@teganandsara',
        'github': '@heartthrob'
    }
}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @bey

for name, info in contacts.items():
    print('''{0}'s contact information is:
        Phone: {1}
        Twitter: {2}
        Github: {3}'''.format(name, info['phone'], info['twitter'], info['github']))


# Goal 2:  Display that information as an HTML table.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

print('<table border="1">')
for name, info in contacts.items():
    print(str("""\t<tr>
        <td colspan="2"> {0} </td>
    </tr>
    <tr>
        <td> Phone: {1} </td>
        <td> Twitter: {2} </td>
        <td> Github: {3} </td>
    </tr>""".format(name, info['phone'], info['twitter'], info['github'])))
print('</table>')


# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

file_contents = '<table border="1">'
for name, info in contacts.items():
    file_contents += """\t
    <tr>
        <td colspan="2"> {0} </td>
    </tr>
    <tr>
        <td> Phone: {1} </td>
        <td> Twitter: {2} </td>
        <td> Github: {3} </td>
    </tr>""".format(name, info['phone'], info['twitter'], info['github'])
file_contents += '\n</table>'

with open('contacts.html', 'w') as contacts_file:
    contacts_file.write(file_contents)


# Goal 4: Instead of reading in the contacts from the dictionary above, 
# read them in from contacts.csv, which you can find in lesson_07_(files).

with open('contacts.csv') as contacts_file:
    contacts = contacts_file.read()

contact_directory = {}
i = 0

# split file contents by row
for row in contacts.split('\n'):
    # split row by column
    if row != 0:
        name, phone, github, twitter = row.split(',')
        contact_directory[name] = {
            'Phone': phone,
            'Github': github,
            'Twitter': twitter
        }
    i += 1
print(contact_directory)
