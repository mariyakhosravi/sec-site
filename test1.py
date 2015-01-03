from bs4 import BeautifulSoup
import urllib3
page = urllib3.PoolManager()
r =page.request('GET',"http://www.pooyatv.ir/naghashi?start=56400")
print r.status
soup = BeautifulSoup(r.data)
k = soup.find_all("h3", attrs={"class" : "catItemTitle"})
for link in k:
    newlink = "http://www.pooyatv.ir"+ link.a["href"]
    item = page.request('GET' , newlink)
    newsoup = BeautifulSoup(item.data)
    fn = newsoup.find({"div"}, attrs={"class":"itemBody"}).strong
    ln = newsoup.find({})
    print fn.text
    print "###################"
