# rss2json python script
========================
this `rss2json` script will convert any rss feed link into wel formated json data, and its supports RSS, ATOM, Google alerts rss feeds, .rss files.


Requirements:
-------------
**Install the library**:

``pip install feedparser``

Run function
``rss2json('your rss link')``

Output:
-------

``
{
"feeds":[
  {
  "title":"Change Taiwan On Your Websites, Or Pay The Price: China To US Airlines",
  "summary":"US-based airlines in China could face internet trouble, snubs from Chinese ticket brokers and state-sanctioned boycotts if they do not follow Beijings order to change the way they label Taiwan on...",
  "link":"https://www.ndtv.com/world-news/china-to-american-airlines-delta-united-airlines-change-taiwan-on-your-websites-or-pay-the-price-1889305",
  "thumbnail":"https://c.ndtvimg.com/05gfdark_united-airlines-bloomberg_120x90_25_July_18.jpg",
  "published":"Wed, 25 Jul 2018 11:22:00 +0530"
  }
  ],
"data":{
  "status":"ok",
  "date":"July 25, 2018 11:35 AM",
  "version":"rss20",
  "title":"NDTV News - Top-stories"
  }
}
``

