# -*- coding: utf-8 -*-
import sys
import os, time
import urllib, urllib2, cookielib
import threading

exhibit_list = [
    # (title, author, description, pages, award, directory)
]

title_list = []
exhibitor_list = []
description_list = []
directory_list = []
pages_list = []
award_list = []

exhibits_txt = open("exhibits.txt").read()
exhibits_txt = exhibits_txt.split('\n\n')

for exhibit in exhibits_txt:
    if exhibit.find("Highest Award\t") < 0:
        exhibit += "Highest Award\t\n"
    title = exhibit[exhibit.find("Title\t")+len("Title\t") : exhibit.find("Exhibitor\t")]
    exhibitor = exhibit[exhibit.find("Exhibitor\t")+len("Exhibitor\t") : exhibit.find("Frames(Pages)\t")]
    pages = exhibit[exhibit.find("Frames(Pages)\t")+len("Frames(Pages)\t") : exhibit.find("Description\t")]
    pages = int(pages[pages.find("(")+1: pages.find(")")])
    description = exhibit[exhibit.find("Description\t")+len("Description\t") : exhibit.find("Highest Award\t")]
    award = exhibit[exhibit.find("Highest Award\t")+len("Highest Award\t") :].split("\n")[0]
    title_list.append(title)
    exhibitor_list.append(exhibitor)
    description_list.append(description)
    pages_list.append(pages)
    award_list.append(award)

exhibits_asp = open("exhibits.asp").read()
exhibits_asp = exhibits_asp.split('\n')

for exhibit in exhibits_asp:
    if exhibit.find("img border='1' width='100' height='130' src='http://www.malariastamps.com/exhibits/exhibits_images/") > 0:
        directory = exhibit[exhibit.find("img border='1' width='100' height='130' src='http://www.malariastamps.com/exhibits/exhibits_images/") + len("img border='1' width='100' height='130' src='http://www.malariastamps.com/exhibits/exhibits_images/") : exhibit.find("/1L.jpg")]
        directory_list.append(directory)



def download(url):
    print "downloading file: " + url
    #request = urllib2.Request(url, self.login_data, self.headers)
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)  
        downloaded = response.read()
    except Exception, e:
        print e
        downloaded = None
    return downloaded

url_base = 'http://www.malariastamps.com/exhibits/exhibits_images/'



def download_exhibits(start, count):
    if start > len(title_list):
        start = len(title_list)
    end = start + count
    if end > len(title_list):
        end = len(title_list)
    for i in range(start, end):
        print "handling exhibit (" + str(i+1) + "): "+ title_list[i]
        directory = directory_list[i]
        d = directory.replace('\\', '_')
        d = d.replace('/', '_')
        if os.path.exists(d) == False:
            os.mkdir(d)
        for j in range(pages_list[i]):
            file_name = d + '/' + str(j+1).zfill(3) + '.jpg'
            if os.path.exists(file_name) == False:
                img = download(url_base + directory + '/' + str(j+1) + '.jpg')
                if img != None:
                    f = open(file_name, 'wb')
                    f.write(img)
                    f.close()
    
def test(start, count):
    if start > len(title_list):
        start = len(title_list)
    end = start + count
    if end > len(title_list):
        end = len(title_list)
    while True:
        print start, end

if False:
    threads = []
    for i in range(9):
        threads.append(threading.Thread(target=download_exhibits, args=(i * 20, 20)))

    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
else:
    download_exhibits(0, len(title_list))

    
