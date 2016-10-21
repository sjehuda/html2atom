#!/usr/bin/python
# coding: utf-8

from lxml import etree
import feedgenerator
import urllib2
import os

# fetch html page
response = urllib2.urlopen('http://psi-im.org/')
doc = response.read()

# you may require an encoding change
# e.g. latin1 -> unicode
#doc = unicode(doc, 'latin1')

# get desired nodes 
tree = etree.HTML(doc)
items = tree.xpath('//a[@class="news"]')

# create feed
feed = feedgenerator.Atom1Feed(
        title = 'Psi - The cross-platform XMPP client for power '
        'users',
        link = 'http://psi-im.org/',
        description = 'XMPP',
        subtitle = 'Psi is a free instant messaging application '
        'designed for the XMPP network (including Google Talk). '
        'Fast and lightweight, Psi is fully open-source and '
        'compatible with Windows, Linux, and Mac OS X.',
        language = 'en-US')

# for each instance of given node
for i in items:
  # get identifier
  ids = i.xpath('@href')
  idposte = 'empty' if len(ids) == 0 else ids[0]

  # get link
  links = i.xpath('@href')
  link = 'empty' if len(links) == 0 else links[0]

  # get description
  descriptions = i.xpath('small/text()')
  description = 'empty' if len(descriptions) == 0 else descriptions[0]

  # get title
  titles = i.xpath('text()')
  title = 'empty' if len(titles) == 0 else titles[0]

  feed.add_item(
        title = title,
        link = link,
        description = description,
        unique_id = idposte
      )

print feed.writeString('utf-8')
