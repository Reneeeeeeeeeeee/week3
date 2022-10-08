import urllib.request as req
def getData(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.findAll("div", class_="title")
    with open("movie.txt","a",encoding="utf-8") as file: 
        for title in titles:
            if title.a !=None:
                if "[好雷]" in title.a.string and "Re:" not in title.a.string:
                    print(title.a.string)
                    file.write(title.a.string +"\n")
   
    nextLink=root.find("a", string="‹ 上頁")  
    return(nextLink["href"]) 
pageurl="https://www.ptt.cc/bbs/movie/index.html"  
count=0
while count<10:
    pageurl="https://www.ptt.cc"+getData(pageurl)
    count+=1

def getData(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.findAll("div", class_="title")
    with open("movie.txt","a",encoding="utf-8") as file: 
        for title in titles:
            if title.a !=None:
                if "[普雷]" in title.a.string and "Re:" not in title.a.string:
                    print(title.a.string)
                    file.write(title.a.string +"\n")
   
    nextLink=root.find("a", string="‹ 上頁")  
    return(nextLink["href"]) 
pageurl="https://www.ptt.cc/bbs/movie/index.html"  
count=0
while count<10:
    pageurl="https://www.ptt.cc"+getData(pageurl)
    count+=1
    
def getData(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.findAll("div", class_="title")
    with open("movie.txt","a",encoding="utf-8") as file: 
        for title in titles:
            if title.a !=None:
                if "[負雷]" in title.a.string and "Re:" not in title.a.string:
                    print(title.a.string)
                    file.write(title.a.string +"\n")
   
    nextLink=root.find("a", string="‹ 上頁")  
    return(nextLink["href"]) 
pageurl="https://www.ptt.cc/bbs/movie/index.html"  
count=0
while count<10:
    pageurl="https://www.ptt.cc"+getData(pageurl)
    count+=1
    

        