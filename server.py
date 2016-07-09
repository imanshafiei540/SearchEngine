import socket
import re
import sqlite3
import time
import sample_pb2
import results_pb2


con=sqlite3.connect("crawler")
links=con.execute("select link from scrapper").fetchall()
contents=con.execute("SELECT content FROM scrapper").fetchall()

def setter(q,w,e):
    a=time.time()
    must_contain = q
    mustnot_contain = w
    least_contain =e


    con=sqlite3.connect("crawler")
    links=con.execute("select link from scrapper").fetchall()
    contents=con.execute("SELECT content FROM scrapper").fetchall()
    #print len(links)
    #print must_contain
    links=[link[0] for link in links]
    contents=[content[0] for content in contents]
    #print links
    '''print must_contain
    print mustnot_contain
    print least_contain'''
    file = open("websites.txt", "r")
    list = []
    for i in range(len(links)):
        line=links[i]
        #print line
        html_content = contents[i]
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
                print matches2
                if len(matches2) != 0:
                    if line in list:
                        list.remove(line)


    #print list
    result=open("result.txt","w")
    result.write(str(time.time()-a)+"\n")
    result.write(str(len(links))+"\n")
    result.write(str(len(list))+"\n")
    for i in list:
        result.write(i+"\n")
    result.close()
    #print must_contain,mustnot_contain,least_contain
    print time.time()-a
    return list

#setter("<body>","","")

s = socket.socket()
host = "localhost"
port = 9999
s.bind((host,port))

s.listen(5)
while True:
    c, addr = s.accept()
    res = c.recv(10000)
    data = sample_pb2.Data()
    data.ParseFromString(res)
    mb = []
    for item in data.mustbe:
        mb.append(item.mustbe)
    mnb = []
    for item in data.mustnotbe:
        mnb.append(item.mustnotbe)
    ob = []
    for item in data.onlybe:
        ob.append(item.onlybe)

    links = setter(mb , mnb , ob)
    print links
    data = results_pb2.Data()

    for item in links:
        link = data.repeatLinks.add()
        link.containLinks = item

    final_res = data.SerializeToString()

    c.send(final_res)


    c.close()
