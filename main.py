import requests 
import argparse
import csv
import datetime

#CLI definition
parser = argparse.ArgumentParser(description="Retrieve last sales from StockX")
parser.add_argument("--keywords", type=str, nargs="+", help="Keywords of the shoe you want to retrieve sales of", required=True)
parser.add_argument("--sizes", type=str, nargs="+", help="Sizes you want", required=True)
parser.add_argument("--sales", type=int, nargs=1, help="Indicate the number of sales you want to get", required=True)
parser.add_argument("-s", "--save", type=bool, default=False, help="Indicate True if you want to save the file")
args = parser.parse_args()

#variables initialization
s = requests.session()
keywords = " ".join(args.keywords)
sizes = args.sizes
numberOfSales = args.sales[0]
booleanSave = args.save
global_iterable = [['Product Name','Size','Retail Price','Sale Price','Sale Date']]

#get API url using keywords
def getAPIurl():

  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en;q=0.5",
    "x-algolia-api-key": "6bfb5abee4dcd8cea8f0ca1ca085c2b3",
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
def getUuid(url,cli_size):

  uuidList = []
  retailPrice = 1

  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Host': 'stockx.com'
  }
  		
  response = s.get(url, headers=headers)
  
  json_content = response.json()
  
  #getting retail price
  data = json_content['Product']['traits']
  for j in data:
    if (j['name']=="Retail Price" or j['name']=="Retail"): #need to a better method to get retail price
      retailPrice = j['value']


  #getting shoe name and its uuid
  for i in range(0,len(cli_size)):
    shoeName = str(json_content["Product"]["title"])
    for d in json_content['Product']['children']:
      size = json_content['Product']['children'][d]['shoeSize']
      if (size==cli_size[i]):
        uuidList += [json_content['Product']['children'][d]['uuid']]


  return retailPrice,shoeName,uuidList


def getSales(uuid,shoeName,retailPrice,userSales):

  iterable = []

  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Host': 'stockx.com'
  }
  
  #sales link building
  url = 'https://stockx.com/api/products/' + str(uuid) + '/activity?state=480&currency=EUR&limit=' + str(userSales) + '&page=1&sort=createdAt&order=DESC&country=FR'

  response = s.get(url, headers=headers)
  
  json = response.json()
  
  #getting last payout or max number of sales (if cli_size exceeds it)
  shoeSize = int(json["ProductActivity"][0]["shoeSize"])
  lastPrice = json["ProductActivity"][0]["localAmount"]*0.88-5 #need to find the exact formula and implements luxury tax
  maxNumberOfSales = int(json["Pagination"]["total"])
  
  #printing shoe name
  print(shoeName + " " + str(json["ProductActivity"][0]["shoeSize"]))

  #getting a readable date format
  def printPrices(i):
    return str(json["ProductActivity"][i]["localAmount"])
  
  def printDate(i):
    initial_date = str(json["ProductActivity"][i]["createdAt"])[0:10]
    dd = int(initial_date[8:10])
    mm = int(initial_date[5:7])
    yy = int(initial_date[0:4])
    temp_date = datetime.date(yy,mm,dd)
    return temp_date
    
  def printTime(i):
    return str(json["ProductActivity"][i]["createdAt"])[11:19]


  if (userSales > maxNumberOfSales):
    userSales = maxNumberOfSales

  #print last sales with a timestamp
  for i in range(userSales):
      print(printPrices(i) +  "€ le " + str(printDate(i)) + " à " + printTime(i))
      date = printDate(i)
      iterable += [[shoeName] + [shoeSize] + [retailPrice] + [printPrices(i)] + [date]]
  
  print("Retail price : " + str(retailPrice))

  print("--> stockx estimated payout = " + str(lastPrice))
  
  print("--> ROI = " + str((lastPrice-retailPrice)/retailPrice*100) +"\n")
  
  return iterable

url = getAPIurl()
retailPrice, shoeName, uuidList = getUuid(url, sizes)

for uuid in uuidList:
  global_iterable += getSales(uuid, shoeName, retailPrice, numberOfSales)

with open('sales.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(global_iterable)