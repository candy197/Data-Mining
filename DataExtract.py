from bs4 import BeautifulSoup
import pandas as pd
import requests
import os.path


def FetchData(URL,URL_ID):
    UserAgent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
    page = requests.get(URL,headers={"User-Agent":UserAgent})#Passing User Agent Through Request
    Src = page.content
    StatusOfUrl = page.status_code #Site Status Code checking 
    print(URL," = ",StatusOfUrl)
    soup = BeautifulSoup(Src,'lxml')
    ArticlePara = soup.find("div",attrs={"class":"td-post-content"})#Finding Article Data in HTML Page and name of the class
    ArticleTitle = soup.find("h1",attrs={"class":"entry-title"})#Finding Title of the Article
    TagsFind = ["h3","p","h1","h2","h4","ul"] #List of Some Specific Tags 
    name = "URL_ID-"+str(URL_ID)+".txt" #Writing File name as URL_ID{No of ID}
    title = ArticleTitle.text+'\n'
    SavePath = "C:\\Users\\Celestial\\Desktop\\Task\\TextLogs"
    CompletedPath = os.path.join(SavePath,name)   

    filename = open(CompletedPath,"w",encoding='utf-8')  
    filename.writelines(title)
    for article in ArticlePara.find_all(TagsFind): #Looping Content by paragraph and writing it to text file        
        para = article.text+"\n"  
        filename.write(para)




InputData = pd.read_excel("input.xlsx")
Search = pd.DataFrame(InputData,columns=["URL_ID","URL"])
#FetchData("https://insights.blackcoffer.com/how-is-login-logout-time-tracking-for-employees-in-office-done-by-ai/")
i = 0
for URls in  Search.index:
    i = i+1
    URL_ID = int(Search['URL_ID'][URls])
    URL = str(Search['URL'][URls])
    FetchData(URL,URL_ID)
    print("Fetching ID-",i,"URL")





