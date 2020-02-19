import pyperclip, re

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @                 # @ symbol
    [a-zA-Z0-9.-]+  # domain name
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text
# TODO: Copy results to the clipboard

# Find matches in the clipboard text
text = str(pyperclip.paste())

matches = []
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#TODO: Copy results to the clipboard.

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to the clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')
