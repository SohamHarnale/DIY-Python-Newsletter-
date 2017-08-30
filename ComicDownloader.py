#Multi Threaded Xkcd Comic Downloader

import threading, requests, os, bs4

# Create file 'xkcd'. This file will contain all downloaded comics.
os.makedirs('xkcd')

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading comic from:- http://xkcd.com/%s' %(urlNumber))
        #Download page
        res = requests.get('http://xkcd.com/%s' %(urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)
        element = soup.select('#comic img')
        if element == []:
            print('No image found')
        else:
            comicURL = element[0].get('src')
            #Download the image
            print('Downloading image %s' %(comicURL))
            res = requests.get('https:' + comicURL)
            res.raise_for_status()
            #Saving file to computer. 'wb' -> Write Binary
            imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
            for chunk in res.iter_content(100000):
                # Writing data on computer
                imageFile.write(chunk)
            imageFile.close()

#Creating list to manage all created threads
downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target = downloadXkcd, args = (i, i+99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

#Waiting for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done')