import requests 

totalProfit = 0
totalSales = 0
infos = ""
s = requests.session()


def getPrices(url,yourSize,numberOfSales):

  global s
  
  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Host': 'stockx.com'
  }
    
  		
  response = s.get(url, headers=headers)
  
  json_content = response.json()
    
  for i in json_content['Product']['traits']:
    data = json_content['Product']['traits']
    for j in data:
      if (j['name']=="Retail Price" or j['name']=="Retail"):
        retailPrice = j['value']

  shoeName = str(json_content["Product"]["title"])

  for d in json_content['Product']['children']:
    size = str(json_content['Product']['children'][d]['shoeSize'])
    if (size==yourSize):
      uuid = json_content['Product']['children'][d]['uuid']
	
  getUrl(uuid,shoeName,retailPrice,numberOfSales)


def getUrl(uuid,shoeName,retailPrice,numberOfSales):

  global totalProfit 
  global totalSales
  global infos
  global s

  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Host': 'stockx.com'
  }
  
  url = 'https://stockx.com/api/products/' + str(uuid) + '/activity?state=480&currency=EUR&limit=' + str(numberOfSales) + '&page=1&sort=createdAt&order=DESC&country=FR'
  
  response = s.get(url, headers=headers)
  
  json = response.json()
  
  lastPrice = json["ProductActivity"][0]["localAmount"]*0.88-5
  maxNumberOfSales = int(json["Pagination"]["total"])
  
  print(shoeName + " " + str(json["ProductActivity"][0]["shoeSize"]))
  infos += shoeName + " " + str(json["ProductActivity"][0]["shoeSize"]) + "\n"

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

  for i in range(numberOfSales-1):
    if (numberOfSales > maxNumberOfSales):
      print("Please enter : " + str(maxNumberOfSales) + " instead of " + str(numberOfSales))
      return
    else:
      print(printPrices(i) + printDate(i) + printTime(i))
      infos += printPrices(i) + printDate(i) + printTime(i) + "\n"
    
  
  print("Retail price : " + str(retailPrice))
  infos += "Retail price : " + str(retailPrice) + "\n"
  print("--> stockx payout = " + str(lastPrice))
  infos += "--> stockx payout = " + str(lastPrice) +"\n"
  print("--> ROI = " + str((lastPrice-retailPrice)/retailPrice*100) +"\n")
  infos += "--> ROI = " + str((lastPrice-retailPrice)/retailPrice*100) + "\n\n"
  
  totalProfit = totalProfit + lastPrice-retailPrice
  totalSales += lastPrice
  
  


