import urllib2
import random
import time
import twitter

api = twitter.Api(consumer_key='fsu5mdhbM3NPKU329WzcLBLXQ',
                      consumer_secret='Secret',
                      access_token_key='4553832074-z2S1CGvyKyahsXQezo351WT8YQxuu3KRdA3U5HA',
                      access_token_secret='Secret')

moby_dick = 'https://www.gutenberg.org/files/2701/2701.txt' #Project Gutenberg text file of "Moby Dick"
the_whale = []
ahab = {}

contents = urllib2.urlopen(moby_dick).read()

contents = contents[contents.find("CHAPTER 1. Loomings."):].replace("--"," ").translate(None,'''.,'"-?!:;/&<>()[]{}|1234567890''').replace("CHAPTER","").lower()

tokens = contents.split()

for i in range(len(tokens) - 1):
    if tokens[i] not in ahab:
        ahab[tokens[i]] = []
    ahab[tokens[i]].append(tokens[i+1])

t = random.choice(ahab.keys())
tk = ""

while True:
    tk = ""
    while True:
        if len(tk + t) > 139:
            tk = tk.rstrip().lstrip() + "."
            print tk
            api.PostUpdates(tk.capitalize())
            break
        tk += t + " "
        t = random.choice(ahab[t])
    time.sleep(3600)
