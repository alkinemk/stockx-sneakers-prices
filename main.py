import requests 

totalProfit = 0
totalSales = 0
infos = ""
s = requests.session()


diaDeLosMuertos = 'https://stockx.com/api/products/air-jordan-1-mid-dia-de-los-muertos'
rubberDunk = 'https://stockx.com/api/products/nike-air-rubber-dunk-off-white-unc'
dunkHighPlatinum = 'https://stockx.com/api/products/nike-dunk-high-sp-white-grey'
yeezyNatural = 'https://stockx.com/api/products/adidas-yeezy-boost-350-v2-natural'
mocha = 'https://stockx.com/api/products/air-jordan-1-retro-high-dark-mocha'
luckyGreen = 'https://stockx.com/api/products/air-jordan-1-retro-high-lucky-green-w'
pharell = 'https://stockx.com/api/products/adidas-nmd-hu-pharrell-now-is-her-time-cream-white'
banned = 'https://stockx.com/api/products/air-jordan-1-mid-banned-2020'
yeezyBred = 'https://stockx.com/api/products/adidas-yeezy-boost-350-v2-core-black-red-2017'
arcticLow = 'https://stockx.com/api/products/air-jordan-1-low-light-arctic-pink-gs'
coralPink = 'https://stockx.com/api/products/nike-air-force-1-shadow-white-coral-pink-w'
metallicGold = 'https://stockx.com/api/products/air-jordan-1-retro-high-black-metallic-gold-2020'
yeezyCream = 'https://stockx.com/api/products/adidas-yeezy-boost-350-v2-cream-white'
yeezyBlack = 'https://stockx.com/api/products/adidas-yeezy-boost-350-v2-black'
trueForm = 'https://stockx.com/api/products/adidas-yeezy-boost-350-v2-true-form'
travis = 'https://stockx.com/api/products/air-jordan-1-retro-high-travis-scott'
laToChi = 'https://stockx.com/api/products/air-jordan-1-sb-la-to-chicago'
asics = 'https://stockx.com/api/products/asics-gel-lyte-iii-atmos-x-solebox'
dunkParra = 'https://stockx.com/api/products/nike-sb-dunk-low-parra'
travisaf1 = 'https://stockx.com/api/products/nike-air-force-1-low-travis-scott-cactus-jack-td'
vaporstreet = 'https://stockx.com/api/products/nike-vapor-street-off-white-black-laser-fuchsia-w'

boxLogoHoodie = 'https://stockx.com/api/products/supreme-cross-box-logo-hooded-sweatshirt-heather-grey'
banner = 'https://stockx.com/api/products/supreme-banner-tee-black'
cupid = 'https://stockx.com/api/products/supreme-cupid-tee-heather-grey'
maryBlige = 'https://stockx.com/api/products/supreme-mary-j-blige-tee-black'

parkaSupreme = 'https://stockx.com/api/products/supreme-the-north-face-statue-of-liberty-mountain-jacket-red'
jpg = 'https://stockx.com/api/products/supreme-jean-paul-gaultier-tee-white'

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
  
  
  
getPrices(cupid,'M',20)  
#getPrices(asics,'8',2)
getPrices(parkaSupreme,'M',20)
getPrices(maryBlige,'M',20)
getPrices(jpg,'L',20)
getPrices(cupid,'M',20)
getPrices(banner,'M',20)

getPrices(diaDeLosMuertos,'7',20)
getPrices(rubberDunk,'8',20)
getPrices(dunkHighPlatinum,'5',20)
getPrices(dunkHighPlatinum,'5.5',20)
getPrices(dunkHighPlatinum,'6',20)

getPrices(yeezyNatural,'6',20)
getPrices(mocha,'7',20)
getPrices(luckyGreen,'6W',20)
getPrices(pharell,'6',20)
getPrices(banned,'7',20)

getPrices(yeezyBred,'8.5',20)
getPrices(yeezyBred,'10',20)
getPrices(arcticLow,'4.5Y',20)
getPrices(coralPink,'7W',20)
getPrices(coralPink,'7.5W',20)
getPrices(coralPink,'8W',20)

getPrices(metallicGold,'7',20)
getPrices(yeezyCream,'9',20)
getPrices(yeezyBlack,'7',20)
getPrices(trueForm,'6.5',20)
getPrices(travis,'8',20)

getPrices(laToChi,'8',20)
getPrices(dunkParra,'7.5',20)
getPrices(travisaf1,'5C',20)
getPrices(vaporstreet,'8.5W',20)
getPrices(boxLogoHoodie,'M',20)



infos += "Total profit : " + str(totalProfit) + "\nTotal sales : " + str(totalSales)

fichier = open("data.txt", "w")
fichier.write(infos)
fichier.close()

