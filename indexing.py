import urllib2
import re
import sqlite3
import time
'''
a = raw_input("Words that need to be : ")
b = raw_input("Words that you don't need : ")
c = raw_input("Containing at least one word: ")
'''
must_contain , mustnot_contain,least_contain=[],[],[]
def setter(q,w,e):
    a=time.time()
    must_contain = q
    mustnot_contain = w
    least_contain =e


    con=sqlite3.connect("crawler")
    links=con.execute("select link from scrapper").fetchall()
    contents=con.execute("SELECT content FROM scrapper").fetchall()
    print len(links)
    print must_contain
    links=[link[0] for link in links]
    contents=[content[0] for content in contents]
    print links
    '''print must_contain
    print mustnot_contain
    print least_contain'''
    file = open("websites.txt", "r")
    list = []
    for i in range(len(links)):
        line=links[i]
        print line
        #html_content = urllib2.urlopen(line).read()
        html_content = contents[i]
        flag = 0
        for word in must_contain:
            matches = re.findall(word, html_content)
            if word in matches:
                flag += 1
        if flag == len(must_contain):
            list.append(line)
        for word in least_contain:
            matches3 = re.findall(word, html_content)
            if line not in list:
                if len(matches3) != 0:
                    list.append(line)
                    break
        for word in mustnot_contain:
            if len(word) != 0:
                matches2 = re.findall(word, html_content)
                if len(matches2) != 0:
                    if line in list:
                        list.remove(line)


    print list
    print must_contain,mustnot_contain,least_contain
    print time.time()-a
