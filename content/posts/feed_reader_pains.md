Title: Pains of Feed Reader Migration
Date: 2024-06-10T02:11:41+0000
Category: Tech
Tags: atom, blog, feeds, rss, web
Author: ryochan7
Keywords: atom, blog, feeds, rss, web
Featured_image: images/QuiteRSS_logo.png
Featured_image_alt: QuiteRSS logo

For the past couple of years, I was using the feed reader program QuiteRSS.
I had tried using feed reader programs in the past but I did not get in the habit
of checking on feeds regularly. I allowed myself to get sucked into mostly using
big corporate hubs to read news and find information. QuiteRSS was very simple and
fast. Also, it was very easy to check the original full content from the website from within the
application. Checking blog and other site feeds felt more like checking email
so I finally made checking feeds a habit.

![RSS Guard]({static}/images/RSS_Guard_4.2.1_(dark_mode).png)

Unfortunately, that program has not been maintained since around 2020; I only found
out about that recently from
[https://github.com/QuiteRSS/quiterss/issues/1598](https://github.com/QuiteRSS/quiterss/issues/1598).
People on the QuiteRSS GitHub issue tracker have recommended
the use of the feed reader Rss Guard. [Rss Guard](https://github.com/martinrotter/rssguard)
works okay but it seems like a downgrade
despite being a bigger application with more features. RSS Guard fails on some RSS
feeds for me that QuiteRSS could read just fine. Rss Guard feels extremely bloated
and it seems like some plugins actively need Node.js in order to run; I absolutely
hate Node.js btw. Despite the app having buttons to check the original source for a
feed item, that function almost never works for me. Even trying to open a page in an
external browser only works from the context menu rather than the dedicate buttons or
links. Many feeds only offer a summary of the article text so having problems
browsing the actual page on the site is a big problem for me.

Reading blog feeds will not be as conveninent anymore. I would hope someone
makes a better feed reader or maybe one of the small QuiteRSS forks
gets off the ground. I do not want to have to rely on X, Meta,
and YouTube to get news.
