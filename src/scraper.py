import requests 
import argparse
import csv
import datetime
import os

#CLI definition
parser = argparse.ArgumentParser(description="Retrieve last sales from StockX")
parser.add_argument("--keywords", type=str, nargs="+", help="Keywords of the shoe you want to retrieve sales of", required=True)
args = parser.parse_args()

#variables initialization
s = requests.session()
keywords = " ".join(args.keywords)
global_iterable = [['Product Name','Size','Sale Price','Sale Date']]

#get API url using keywords
def getAPIurl():

  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "x-algolia-api-key": "6b5e76b49705eb9f51a06d3c82f7acee",
    "x-algolia-application-id": "XW7SBCT9V6"
  }
  
  #POST request
  response = s.post(url = "https://xw7sbct9v6-dsn.algolia.net/1/indexes/products/query",headers=headers, json = {"query":keywords,"facets":"*","filters":""})

  json_data = response.json()

  #getting info from JSON
  url = json_data["hits"][0]["url"]

  #returning API url
  api_url = "https://stockx.com/api/products/"+url
  
  return(api_url)

#get uuid from StockX
def getUuid(url):

  uuidList = []

  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
  }

  response = s.get(url, headers=headers)
  if (response.status_code != 200):
    raise Exception(response)
  json_content = response.json()

  #getting shoe short description
  shortDescription = json_content['Product']['shortDescription'].lower()

  #getting shoe name
  shoeName = json_content['Product']['title']

  #getting uuid's
  for i in json_content['Product']["children"]:
    uuidList += [json_content['Product']['children'][i]['uuid']]

  return shoeName,uuidList,shortDescription


def getSales(uuid,shoeName):

  iterable = []

  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
  }
  
  #building sales link
  url = 'https://stockx.com/api/products/' + str(uuid) + '/activity?state=480&currency=EUR&limit=250&page=1&sort=createdAt&order=DESC&country=FR'
  response = s.get(url, headers=headers)
  json = response.json()

  #getting the actual sales number to build the actual link 
  maxNumberOfSales = json["Pagination"]["total"]

  #checking there were sales for the current size
  if json.get("ProductActivity"):
      shoeSize = str(json["ProductActivity"][0]["shoeSize"])

  def getPrices(i):
    return str(json["ProductActivity"][i]["localAmount"])
  
  def getDate(i):
    if json.get("ProductActivity"):
      initial_date = str(json["ProductActivity"][i]["createdAt"])[0:10]
      dd = int(initial_date[8:10])
      mm = int(initial_date[5:7])
      yy = int(initial_date[0:4])
      temp_date = datetime.date(yy,mm,dd)
    return temp_date

  #print last sales with a timestamp
  for i in range(maxNumberOfSales):
      date = getDate(i)
      iterable += [[shoeName] + [shoeSize] + [getPrices(i)] + [date]]
  
  return iterable

url = getAPIurl()

shoeName, uuidList, shortDescription = getUuid(url)

for uuid in uuidList:
  global_iterable += getSales(uuid, shoeName)

with open("../assets/data/" + shortDescription + '.csv','w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(global_iterable)