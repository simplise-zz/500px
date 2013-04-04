# -*- coding:UTF-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2,re, os, urllib

#read the 500px html page with BeautifulSoup
page_url=raw_input('Please enter the url of 500px image:')
print "Image Downloading......"
page_soup=BeautifulSoup(urllib2.urlopen(page_url).read())

#find the exact link of image from the html page
image_list=page_soup.findAll('img',id='mainphoto')
image_link=image_list[0]['src']
image_name=image_list[0]['alt']

#download the image
image_path='/home/500px/'
if not os.path.exists(image_path):
    os.mkdir(image_path)
urllib.urlretrieve(image_link,'%s%s.jpg' % (image_path, image_name))
print "Image Downloaded!"
