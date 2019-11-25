import requests
r = requests.get("https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html")

# print(r.text[0:500]) #网页前500个text

from bs4 import BeautifulSoup #导入BeautifulSoup
soup = BeautifulSoup(r.text,"html.parser")
results = soup.find_all("span",attrs={"class":"short-desc"})
print(len(results))

# print(results[0:4])

# print(results[-1])

first_result = results[0]#第一句
print(first_result)

#print(first_result.find("strong")) #<strong>Jan. 21 </strong>
#print(first_result.find("strong").text) #去掉左右两边代码，仅保留中间文本

#print(first_result.find("strong").text[0:-1]) #去掉末尾特殊代码
print("第一部分内容，date: "+first_result.find("strong").text[0:-1] + ", 2017")

#print(first_result.contents)#是一个list，把第一段内容根据不同的格式，分割呈3块，例如，日期，文本内容，链接）
#print(first_result.contents[1]) #list 里的第二块内容。
print("第二部分内容，文本: "+first_result.contents[1][1:-2]) #list 里面的第二块内容的 第【1:-2】的内容

#print(first_result.contents[2]) #list 里面第3块内容，链接


#print(first_result.find("a"))
#print(first_result.find("a").text[1:-1])

#print(first_result.find("a").content)
print("第三部分内容，链接： "+ first_result.find("a")["href"])

records = []
for result in results:
    date = result.find("strong").text[0:-1]+", 2017"
    lie = result.contents[1][1:-2]
    explanation = result.find("a").text[1:-1]
    url = result.find("a")["href"]
    records.append((date,lie,explanation,url))

len = len(records)
print(len)

print(records[0:3])

import pandas as pd
df = pd.DataFrame(records, columns = ["date","lie","explanation","url"])

df= df.head()

#print(df)

tail = df.tail()
#print(tail)

df["date"]=pd.to_datetime(df["date"])
print(tail)

df.to_csv("trump_lies.csv",index = False, encoding = "utf-8")
df = pd.read_csv("trum_lies.csv",parse_dates=["date"],encoding = "utf-8")
