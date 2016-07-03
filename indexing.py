import re
import sqlite3
import time
'''
a = raw_input("Words that need to be : ")
b = raw_input("Words that you don't need : ")
c = raw_input("Containing at least one word: ")
'''
must_contain , mustnot_contain,least_contain=[],[],[]


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


def setter(q,w,e):
    a=time.time()
    must_contain = q.split(' ')
    mustnot_contain = w.split(' ')
    least_contain =e.split(' ')


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
        html_content = striphtml(contents[i])
        flag = 0

        for word in must_contain:
            if len(word) != 0:
                matches = re.findall(word, html_content)
                if word in matches:
                    flag += 1
        if flag == len(must_contain):
            list.append(line)

        for word in least_contain:
            if len(word) != 0:
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

setter("<body>","","")