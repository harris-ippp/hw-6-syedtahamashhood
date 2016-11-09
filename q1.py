import requests
from bs4 import BeautifulSoup

url =  "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html, 'html.parser')

#  print(result["id"], type(result["id"]))
#  print(result(["id"].split(".")[2])
with open("ELECTION_ID", "w") as out:
    for result in soup.find_all("tr", "election_item"): #for every element in our url soup find all table row that have election item in them
        #print(result["id"], type(result["id"]))
        id_number = result["id"].split("-")[2] # creating a variable  id_number,calling on "id" in the result, cut this string by the dashes and select position two
        year = result.find("td", "year first").contents[0] #creating a variable called year that will find td row that contains year first and give me the content of this tag at position 0
        out.write("{} {}\n".format(id_number, year))
        #print id_number and year. #just for checking 
