import mechanize
import copy
import threading
import traceback
br=mechanize.Browser()
br2=mechanize.Browser()
lock=threading.Lock()
browsers=[br]
root="http://www.tutorialspoint.com/python/"
response=browsers[-1].open(root)
br.open(root)
links=br.links()
links=[link for link in links]
print br.open("http://www.python.org/")
i=[root[:-1]+link.url for link in br.links() if link.url[0]=="/"]
#crawler={"link":[root],"content":[],"links":[[root[:-1]+link.url for link in br.links() if link.url[0]=="/"]],"flag":[False]}
crawler={"link":[root],"content":[],"links":[[root[:-1]+link.url for link in br.links() if link.url[0]=="/"]]}
f=open("root.txt","w")
f.write(str(crawler))
f.close()