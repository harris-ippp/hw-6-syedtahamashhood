
import requests

url="http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

for line in open("ELECTION_ID"):  #we are opening the line
  newvar=line.strip().split()   # create new variable and split each line where there are white spaces
  print(newvar[1], url.format(newvar[0]))
  year=newvar[1]
  urls=url.format(newvar[0])
  abc = requests.get(urls)  # create a variable called abc, and call on url for that file
  file_name = year + ".csv"     # create a new variable called file_name, its consists of the 'year' and the extension '.cvs' which makes sure that we save it as a .cvs file
  with open(file_name, "w") as out:
    out.write(abc.text)  #save a file with the response content for each file_name
