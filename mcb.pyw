#! python 3

## The program will save each piece of clipboard text under a keyword. For example, when you run py mcb.pyw save spam, the current contents of the clipboard will be saved with the keyword spam. This text can later be loaded to the clipboard again by running py mcb.pyw spam. And if the user forgets what keywords they have, they can run py mcb.pyw list to copy a list of all keywords to the clipboard.

## Here’s what the program does:

# The command line argument for the keyword is checked.
# If the argument is save, then the clipboard contents are saved to the keyword.
# If the argument is list, then all the keywords are copied to the clipboard.
# Otherwise, the text for the keyword is copied to the clipboard.
# This means the code will need to do the following:

# Read the command line arguments from sys.argv.
# Read and write to the clipboard.
# Save and load to a shelf file.

## Step 1: Comments and Shelf Setup

# mcb.pyw -- Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - saves clipboard to the keyword
#   py.exe mcb.pyw<keyword> - Loads keyword to clipboard
#   py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')

#: Save the clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
#: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()

## Step 2: Save clipboard Content with a Keyword

# The program does different things depending on whether the user wants to save text to a keyword, load text into the clipboard, or list all the existing keywords. Let’s deal with that first case. 

## Step 3 : List keywords and Load a keyword's content

# the user wants to load clipboard text in from a keyword, or they want a list of all available keywords