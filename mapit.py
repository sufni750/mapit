#! python3
# mapit.py lanching a browser tab with map with adress from clipboard or command line

import webbrowser, sys
if len(sys.argv) > 1:
	# Get address from command line
	address = ' '.join(sys.argv[1:])
else:
	# Get address from clipboard
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
