from bs4 import BeautifulSoup, NavigableString
import urllib2
import random
import time
import twitter

api = twitter.Api(consumer_key='fsu5mdhbM3NPKU329WzcLBLXQ',
                      consumer_secret='secret',
                      access_token_key='4553832074-z2S1CGvyKyahsXQezo351WT8YQxuu3KRdA3U5HA',
                      access_token_secret='secret')

def strip_tags(html, invalid_tags):
    '''
    sourced from http://stackoverflow.com/questions/1765848/remove-a-tag-using-beautifulsoup-but-keep-its-contents
    '''
    soup = BeautifulSoup(html)
    for tag in soup.findAll(True):
        if tag.name in invalid_tags:
            s = ""
            for c in tag.contents:
                if not isinstance(c, NavigableString):
                     c = strip_tags(unicode(c), invalid_tags)
                s += unicode(c)
            tag.replaceWith(s)
    return soup

literally_hitler = 'http://www.hitler.org/writings/Mein_Kampf/'
my_struggle = []
hitler_bot = {}

landing = BeautifulSoup(urllib2.urlopen(literally_hitler).read())

for tag in landing.find_all("a"):
    if '.html' in tag['href']:
        url = literally_hitler + tag['href']
        response = urllib2.urlopen(url).read()
        soup = strip_tags(response,['img','br','center']).find("blockquote")
        my_struggle.append(soup)

print len(my_struggle)

for chapter in my_struggle:
    tokens = str(chapter).translate(None,'''.,'"-?!:;/&<>''').replace("blockquote",'').replace("lthtmlgtltheadgtltheadgtltbodygtltbodygtlthtmlgt","").split()
    for i in range(len(tokens) - 1):
        if tokens[i].lower() not in hitler_bot:
            hitler_bot[tokens[i].lower()] = []
        hitler_bot[tokens[i].lower()].append(tokens[i + 1].lower())

#print str(my_struggle[5]).translate(None,'''.,'"-?!:;/&<>''').replace("blockquote",'').replace("lthtmlgtltheadgtltheadgtltbodygtltbodygtlthtmlgt","")

t = random.choice(hitler_bot.keys())
#print (t,hitler_bot[t],random.choice(hitler_bot[t]))
tk = ""

for j in range(10):
    tk += t + " "
    t = random.choice(hitler_bot[t])
    
print tk

tk = ""

while True:
    if len(tk + t) > 140:
        tk = tk.rstrip() + "."
        break
    tk += t + " "
    t = random.choice(hitler_bot[t])

print tk

api.PostUpdates(tk)

