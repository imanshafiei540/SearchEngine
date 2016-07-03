import mechanize
import copy
import threading
import traceback
import time
import sqlite3

br=mechanize.Browser()
br2=mechanize.Browser()
lock=threading.Lock()
browsers=[br]
root="http://www.python.org/"
response=browsers[-1].open(root)
br.open(root)
links=br.links()
links=[root[:-1]+i.url for i in links if i.url[0]=="/"]
#crawler=[{"link":root,"content":response.read(),"links":browsers[-1].links(),"flag":False}]
crawler=[{"link":root,"content":response.read(),"links":browsers[-1].links()}]
crawler2=[]
browser={}

rooter=open("root.txt","r")
crawler=eval(rooter.readline())
rooter.close()
counter=0

def adder(crawler,link):
    try:
        with lock:
            crawler["link"].append(link)
            browser[link]=mechanize.Browser()
            response=browser[link].open(link)
            print "######################start"
            crawler["content"].append(response.read())
            print browser[link]
            #print browser[link].links()
            links=[root[:-1]+i.url for i in browser[link].links() if i.url[0]=="/"]
            crawler["links"].append(links)
            #crawler["links"].append(browser[link].links())
            #crawler["flag"].append(False)
            print "#######################end"
            db=sqlite3.connect("crawler")
            db.text_factory=str
            try:
                db.execute("insert into scrapper (link, content) values (?, ?);",(str(crawler["link"][-1]), crawler["content"][-1] ))
            except:
                del crawler["links"][-1]
                #del crawler["flag"][-1]
                print "we have no bugs hahahahaha                                   yooohahahaha"
            db.commit()
            db.close()
            '''t=open("test.txt","a")
            t.write(str(crawler["link"])+"\n")
            t.write(crawler["content"][-1])
            t.close()'''
            del crawler["content"][-1]
            rooter=open("root.txt","w")
            st_maker=str(crawler)
            rooter.write(st_maker)
            rooter.close()
        print "added successfully this: "+str(crawler["link"][-1])
    except:
        print link
        traceback.print_exc()


def crawl(links):
    for link in links:
        #if link.url[0]=="/":
            #tmp= root[:-1]+link.url
            tmp= link
            print "start: "+str(link)
            if tmp not in crawler["link"]:
                thread=threading.Thread(target=adder,args=(crawler,tmp))
                while True:
                    try:
                        thread.start()
                        break
                    except:
                        time.sleep(0.5)
                        print "manyyyyyyyy threads!!!!="+str(threading.activeCount())
                #adder(crawler,tmp)
            #th.append(threading.Thread(target=adder,args=(crawler,tmp)))
            #th[-1].start()


while True:
    print crawler
    if (counter>=min(len(crawler["link"]),len(crawler["links"])) and threading.activeCount()==1):
        #t=open("test.txt","w")
        #t.write(str(crawler))
        #t.close()
        print "end of crawling"
        break
    elif (counter>=min(len(crawler["link"]),len(crawler["links"])) and threading.activeCount()>1):
        time.sleep(1)
        print len(crawler["content"])
        print "waiting..."+str(threading.activeCount())
        continue
    else:
        #if crawler["flag"][counter]==False:
        links=crawler["links"][counter]
        #thread=threading.Thread(target=crawl,args=(links,))
        #thread.start()
        crawl(links)
        #crawler["flag"][counter]=True
    counter+=1
    print counter




'''
def adder(crawler,link):
    try:
        #with lock:
        browsers.append(mechanize.Browser())
        response=browsers[-1].open(link)
        crawler.append({"link":link,"content":response.read(),"links":browsers[-1].links(),"flag":False})
    except:
        print link
        traceback.print_exc()
th=[]
def crawl(links):
    for link in links:
        if link.url[0]=="/":
            tmp= root[:-1]+link.url
            adder(crawler,tmp)
            #th.append(threading.Thread(target=adder,args=(crawler,tmp)))
            #th[-1].start()
            print "done"
            #crawler.append({"link":tmp,"content":br2.open(tmp)})
counter=0
while True:
    if (counter>=len(crawler)):
        print counter
        break
    else:
        if (crawler[counter]["flag"]==False):
            links=crawler[counter]["links"]
            crawl(links)
            #th.append(threading.Thread(target="crawl",args=(links)))
            #th[-1].start()
            #now_thread=th[-1]
            for i in th:
                i.join()
            crawler[counter]["flag"]=True
            print "shit"
        counter+=1
'''


