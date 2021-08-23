#! python 3
# This program will automatically look for the weather info of that day.
# Will use pyperclip and sys.argv() 

import webbrowser,sys,pyperclip,bs4,requests

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

res = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=')
res.raise_for_status
soup = bs4.BeautifulSoup(res.text,'lxml')
elems = soup.select('.s-item__link')
numOpen = min(len(elems))
for i in range(numOpen):
    urlToOpen = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=' + elems[i].get('href')
    print('Opening' + urlToOpen)
    webbrowser.open('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=' + urlToOpen)