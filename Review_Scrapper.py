import requests
import bs4

request1=requests.get('https://bit.ly/3MpHH3u')

soup=bs4.BeautifulSoup(request1.text)

reviews=soup.findAll('div',{'class':'ZmyHeo'});

#Fetching Reviews/Comments
for review in reviews:
    print(review.get_text()+"\n\n")

#Fetching Ratings
ratings=soup.find('div',{'class':'ipqd2A'}).get_text()
print("Ratings : ",ratings)

#Fetching Indivisual Ratings
rate=soup.findAll('div',{'class':'XQDdHH Ga3i8K'})

for ir in rate:
    print(ir.get_text()+"\n")


#Fetching Customer Name
cus=soup.findAll('p',{'class':'_2NsDsF AwS1CA'})

for cu in cus:
    print(cu.get_text()+"\n")

#Fetching Questions and Answers
ques=soup.findAll('div',{'class':'wys2hv _43gOsC'})

for qu in ques:
    print(qu.get_text())
    ans=qu.findNext('div',{'class':'JxAXcP'}).get_text()
    print(ans+"\n")
