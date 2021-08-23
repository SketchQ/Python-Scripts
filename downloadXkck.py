#!python3
# downloadXkck.py - Downloads every single XKCD Comic.


## This program does:
#   1. Loads the XKCD home page
#   2. Saves the comic image on that page
#   3. Follows the Previous Comic Link
#   4. Repeats until it reaches the first comic.

## Code will do the following
#   1. Download pages with the request module.
#   2. Find the URL of the comic image for a page using Beautiful Soup.
#   3. Download and save the comic image to the hard drive with iter_content().
#   4. Find the URL of the Previous Comic link, and repeat.

## Step 1: Design your program.

#   the URL of the comic's image file is given by the 'href' attribute of an <img> element.
#   the <img> element is inside a <div id="comic" element.
#   the Prev button has a 'rel' HTML attribute with the value 'prev'.
#   the first comic's Prev button links to the 'https://xkcd.com/# URL, indicating that there are no more previous pages.



import requests,bs4,webbrowser,os

'''res = requests.get('https://xkcd.com/')
res.raise_for_status

soup = bs4.BeautifulSoup(res.text,'lxml')
elems = soup.select('#middleContainer > ul:nth-child(2) > li:nth-child(2) > a')


urlToOpen = 'https://xkcd.com/' + elems[0].get('href')
webbrowser.open(urlToOpen)
'''    

url = 'https://xkcd.com/'       # Starting URL
os.makedirs('xkcd', exist_ok=True)  # Store comics in ./xkcd
while not url.endswith('#'):
    # : Download the Page.
    print('Downloading page %s'% url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # : Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find a comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')

    # : Download the image.
    print('Downloading image %s' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()
    #: Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #  Get the Prev's button URL.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done...')
