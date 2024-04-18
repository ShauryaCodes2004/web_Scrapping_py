import requests
from bs4 import BeautifulSoup
url = "https://www.youtube.com/"
content= requests.get(url)
htmlContent = (content.content)
#print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify())

title =soup.title
# print(title)
# print(type(title))
#get all the paragraph tags in website
paras= soup.find_all('p')
# print(paras)
#to get the first para in html page

print(soup.find('p'))
#get classes of any element in html page
print(soup.find('p')['class'])
#find all the elements with class lead
print(soup.find_all("p",class_="lead"))

#to get all the text from tags/soup

# print(soup.find(('p').get_text()))




#types of object 1.tag , 2navagable string ,3beautiful soup , 4 comment




#get all the links present on a web page

anchors = soup.find_all('a')
all_links= set()
for link in anchors:
    if(link.get('href') != '#'):
       linkText= "https://codewithharry.com " + link.get('href')
       all_links.add(link)
    print(linkText)


