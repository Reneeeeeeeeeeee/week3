import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
spot=data["result"]["results"]
with open("data.csv","w",encoding="utf-8") as file:
    for distrit in spot:
        int(distrit["xpostDate"][0:4])       
        str1=str(distrit["file"])
        str2=str1.replace("jpghttps", "jpg;https")
        str3=str2.replace("JPGhttps", "JPG;https")
        str4=str3.split(";")[0]
        if int(distrit["xpostDate"][0:4]) >= 2015:
            file.write(distrit["stitle"]+","+ distrit["address"][5:8]+","+ distrit["longitude"]+","+ distrit["latitude"]+","+ str4+"\n")
     