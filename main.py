import requests 
import argparse

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
global_data = ""

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


def getSales(uuid,shoeName,retailPrice,cli_sales,data):

  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Host': 'stockx.com'
  }
  
  #sales link building
  url = 'https://stockx.com/api/products/' + str(uuid) + '/activity?state=480&currency=EUR&limit=' + str(numberOfSales) + '&page=1&sort=createdAt&order=DESC&country=FR'
  
  response = s.get(url, headers=headers)
  
  json = response.json()
  
  #getting last payout and max number of sales (if cli_size exceeds it)
  lastPrice = json["ProductActivity"][0]["localAmount"]*0.88-5 #need to find the exact formula and implements luxury tax
  maxNumberOfSales = int(json["Pagination"]["total"])
  
  #printing shoe name
  print(shoeName + " " + str(json["ProductActivity"][0]["shoeSize"]))
  data += shoeName + " " + str(json["ProductActivity"][0]["shoeSize"])

  #getting a readable date format
  def printPrices(i):
    return str(json["ProductActivity"][i]["localAmount"]) + " € le "
  
  def printDate(i):
    date = str(json["ProductActivity"][i]["createdAt"])[0:10]
    dd = date[8:10] + "/"
    mm = date[5:7] + "/"
    yy = date[0:4]
    return dd + mm + yy + " à "
    
  def printTime(i):
    return str(json["ProductActivity"][i]["createdAt"])[11:19]

  #print last sales with a timestamp
  for i in range(numberOfSales-1):
    if (numberOfSales > maxNumberOfSales):
      print("Please enter : " + str(maxNumberOfSales) + " instead of " + str(numberOfSales))
    else:
      print(printPrices(i) + printDate(i) + printTime(i))
      data += printPrices(i) + printDate(i) + printTime(i) + "\n"
    
  
  print("Retail price : " + str(retailPrice))
  data += "Retail price : " + str(retailPrice)

  print("--> stockx payout = " + str(lastPrice))
  data += "--> stockx payout = " + str(lastPrice)
  
  print("--> ROI = " + str((lastPrice-retailPrice)/retailPrice*100) +"\n")
  data += "--> ROI = " + str((lastPrice-retailPrice)/retailPrice*100) +"\n"
  
  return data

url = getAPIurl()
retailPrice, shoeName, uuidList = getUuid(url, sizes)

for uuid in uuidList:
  global_data = getSales(uuid, shoeName, retailPrice, numberOfSales,global_data)

#saving info locally as a .txt file
if booleanSave==True:
  with open('data.txt', 'w') as fd:
    fd.write(global_data)




  
  

  

