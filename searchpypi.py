#! python3
# searchpypi.py - Opens several search results.

## This is what this program does:
#   1. Gets search keywords from the command line arguments
#   2. Retrieves the search results page
#   3. Opens a browser tab for each result

## Code needs to do the following:
#   1. Read the command line arguments from sys.argv.
#   2. Fetch the search result page with the requests module.
#   3. Find the links to each search result.
#   4. Call the webbrowser.open() Function to open the web browser.

##  Step 1: Get the Command line Arguments and Request the Search page

import requests,sys,webbrowser,bs4,pyperclip

print('Searching...')   # display text while downloading the search result page

res = requests.get( 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

##  Step 2: Find all the Results.
# Now you need to use Beautiful Soup to extract the top search result links from your downloaded HTML. But how do you figure out the right selector for the job? For example, you can’t just search for all <a> tags, because there are lots of links you don’t care about in the HTML. Instead, you must inspect the search result page with the browser’s developer tools to try to find a selector that will pick out only the links you want.
# : Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'html.parser')


# : Opens a browser tab for each result.

linkElems = soup.select('.package-snippet')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)