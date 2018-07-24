import feedparser
import json
import datetime
import time

def rss2json(url):
    
    """
    rss atom to parsed json data
    supports google alerts
    """
    parsedurl = feedparser.parse(url)
    item = {}
    feedslist = []
    feed = {}
    feedsdict = {}
    
    feed["status"] = "ok"
    if 'updated' in parsedurl.feed.keys():
        feed["date"] = parsedurl.feed.updated 
    if 'title' in  parsedurl.feed.keys():    
        feed["title"]=parsedurl.feed.title
    if 'image' in parsedurl.feed.keys():    
        feed["image"] =parsedurl.feed.image
    
#     feeds.append(feed.copy())
    feedsdict["data"] = feed
    for fd in parsedurl.entries:
        item["title"]=fd.title
        item["link"] = fd.link
        item["summary"]=fd.summary
        item["published"]=time.mktime(datetime.datetime.strptime(fd.published, "%a, %d %b %Y %H:%M:%S %z").timetuple())
        
        if 'links' in fd and 'image' in fd.links:
            item["thumbnail"]=feed.links[1]
        if 'storyimage' in fd.keys():
            item["thumbnail"] = fd["storyimage"]
        
        feedslist.append(item.copy())
        
    feedsdict["feeds"] = feedslist
        
    return json.dumps(feedsdict) 
