#! python3
# mappit.py - uses a bat file to automatically goes to a scripted website.

## This program will do:
# 1. gets a street address from the command line or clipboard.
# 2. Opens the web browser to the Google Maps page for the address.
## Code will do;
# 1. Read the command line arguments from sys.argv
# 2. Read the clipboard contents.
# 3. Call the webbrowser.open() function to open the webbrowser.

import webbrowser,sys,pyperclip

# sys.argv System variables will use sys.argv function and will return list of strings ('mapit.py','870','Valencia','St.') 

# Check if command line arguments were passed

if len(sys.argv) > 1:   # if lenght is more than '1' which means command line arguments has been provided.
    # ['mappit.py,'870','Valencia','st.'] -> '870 Valencia st.'
    address = ' '.join(sys.argv[1:])  # will only contain ('870' and after)
else:
    address = pyperclip.paste() # Whatever text is n the clipboard and returns a string which we store to address variable

# https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110,+Amerika+Birle%C5%9Fik+Devletleri/@37.7589621,-122.4238514,17z/data=!3m2!4b1!5s0x808f7e3dae6df76b:0x6240f16ee9572080!4m5!3m4!1s0x808f7e3dae0fc797:0x26acf7c8a5797e94!8m2!3d37.7589579!4d-122.4216627
# as you can see this url for the address is too long
# https://www.google.com/maps/place/<ADDRESS>
# Because google is smart enough to understand we can shorten the url as above. After that we can just use the 'address' variable as an extension for that url as below;

webbrowser.open('https://www.google.com/maps/place/' + address)