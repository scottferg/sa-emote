def download(url):
    import urllib
    webFile = urllib.urlopen(url)
    localFile = open(url.split('/')[-1], 'wb')
    localFile.write(webFile.read())
    webFile.close()
    localFile.close()


import smilies
for text, url in smilies.smilies:
    download(url)
