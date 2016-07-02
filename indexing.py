import urllib2
import re

a = raw_input("Words that need to be : ")
b = raw_input("Words that you don't need : ")
c = raw_input("Containing at least one word: ")

must_contain = a.split(" ")
mustnot_contain = b.split(" ")
least_contain =c.split(" ")
file = open("websites.txt", "r")
list = []
for line in file:
    print line
    html_content = urllib2.urlopen(line).read()
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
