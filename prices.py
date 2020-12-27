import requests 
import inspect

total_profit = 0
total_sales = 0

jordan_dia_7 = 'https://stockx.com/api/products/6e827eee-6316-4060-a586-c2b72ebf4938/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

rubber_dunk_8 = 'https://stockx.com/api/products/5dfa9a7e-a1da-4df8-b916-c6f480683406/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

natural_6 = 'https://stockx.com/api/products/31f0aa94-12b3-4a91-95f2-c1f191ff308b/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

mocha_7 = 'https://stockx.com/api/products/64247b14-fafd-402e-97d4-7cf494799c0a/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

lucky_6W = 'https://stockx.com/api/products/e546bf27-f604-465a-9367-7d9ad42faa99/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

pharell_6 = 'https://stockx.com/api/products/f32aaeb7-4500-43e7-b291-fa77f8bccfdd/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

banned_mid_40 = 'https://stockx.com/api/products/27e14ca9-9021-49dc-83b3-7df225c927e2/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

dunk_high_platinum_5 = 'https://stockx.com/api/products/ffb5e723-705e-416d-951a-a54039b89db9/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

dunk_high_platinum_55 = 'https://stockx.com/api/products/8bb7adde-e57b-4719-adf2-a53ddd8b2bb2/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

dunk_high_platinum_6 = 'https://stockx.com/api/products/d8a3283b-a33b-47c5-841e-bc98d7589e23/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

yeezy_bred_85 = 'https://stockx.com/api/products/507f5a75-8dbd-4e4a-bef1-38558aa7aee6/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

yeezy_bred_10 = 'https://stockx.com/api/products/1dab12f4-e348-4f00-946b-e8110c131e49/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

jordan_pink_low_45Y = 'https://stockx.com/api/products/a0463c37-ef14-40f0-927b-52d93d00c88e/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

coral_pink_7W = 'https://stockx.com/api/products/39dc9057-1e7f-484e-8245-fe780e14e7ff/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

coral_pink_75W = 'https://stockx.com/api/products/1615bbbe-4c1f-44fd-ac16-020c6212c4a6/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

metallic_gold_7 = 'https://stockx.com/api/products/c81d9ca8-a97e-42d7-b236-6ece6532d694/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

coral_pink_8W = 'https://stockx.com/api/products/fad1a840-a992-4315-becc-d92eaf4e1974/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

cream_350_9 = 'https://stockx.com/api/products/85367bf7-70e3-4e01-8ead-9027e314aa64/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

black_350_7 = 'https://stockx.com/api/products/dcc838bc-558b-4ce6-abdb-10c405e345f8/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

true_form_350_65 = 'https://stockx.com/api/products/b68c797c-37a4-40d1-bd46-f3eefacafda1/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

antlia_350_7 = 'https://stockx.com/api/products/7ef14a7d-de5a-41dd-a69a-26f8d15fce61/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

bone_white_500_75 = 'https://stockx.com/api/products/473bc814-af7b-4dd2-869e-36f10e340965/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

vanta_700_85 = 'https://stockx.com/api/products/93e3b3d0-cd1f-49b5-97be-d51a2b940997/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

utility_black_700_45 = 'https://stockx.com/api/products/c0974c44-1b3c-42fc-89d4-7e09790cb1e0/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

jordan1_travis_8 = 'https://stockx.com/api/products/e9dabc77-6697-4ef3-81d4-70859fa2e4db/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

jordan1_la_to_chi_8 = 'https://stockx.com/api/products/500fddfa-a381-4811-a909-95e252576c5c/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

asics_8 = 'https://stockx.com/api/products/60f58ffc-abbb-4be5-84ea-06d0f7b7498c/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

dunk_parra_75 = 'https://stockx.com/api/products/32b1cfb2-b4fe-4512-b5ce-611c06055438/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

dunk_blazer_8 = 'https://stockx.com/api/products/97a3a252-bc15-4512-81e2-33922b3fffdf/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

af1_travis_5c = 'https://stockx.com/api/products/50244db7-019c-43a3-8a49-9b768a9e9f7f/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

vapor_street_85 = 'https://stockx.com/api/products/8dfff9d6-0212-4c48-9904-80b9e2779db8/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

parka_liberty_red_m = 'https://stockx.com/api/products/c9a47456-76fa-4532-82fb-4bf5b4c8e722/activity?state=480&currency=EUR&limit=10&page=1&sort=createdAt&order=DESC&country=FR'

def getPrices(url,retail_price):
  
  global total_profit 
  global total_sales
  
  headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    
  }
  
  r = requests.get(url, headers=headers)
  
  json = r.json()
  
  last_price = json["ProductActivity"][0]["localAmount"]*0.88-5
  
  print("Taille : " + str(json["ProductActivity"][0]["shoeSize"]))

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

  for i in range(9):
    print(printPrices(i) + printDate(i) + printTime(i))
    
  
  print("Retail price : " + str(retail_price))
  print("--> stockx payout = " + str(last_price-retail_price))
  print("--> ROI = " + str((last_price-retail_price)/retail_price*100))
  
  total_profit = total_profit + last_price-retail_price
  total_sales += last_price
 
  print("\n")
  
  
print("JORDAN DIA 40")
getPrices(jordan_dia_7,120)
print("RUBBER DUNK 41")
getPrices(rubber_dunk_8,190)
print("YEEZY 350 NATURAL 38 2/3")
getPrices(natural_6,220)
print("MOCHA 40")
getPrices(mocha_7,160)
print("LUCKY 36.5")
getPrices(lucky_6W,160)
print("BANNED MID 40")
getPrices(banned_mid_40,125)
print("PHARELL 38")
getPrices(pharell_6,110)
print("DUNK HIGH 37.5")
getPrices(dunk_high_platinum_5,110)
print("DUNK HIGH 38")
getPrices(dunk_high_platinum_55,110)
print("DUNK HIGH 38.5")
getPrices(dunk_high_platinum_6,110)
print("YEEZY BRED 42")
getPrices(yeezy_bred_85,220)
print("YEEZY BRED 44")
getPrices(yeezy_bred_10,220)
print("ARCTIC GS 36.5")
getPrices(jordan_pink_low_45Y,75)
print("METALLIC GOLD 40")
getPrices(metallic_gold_7,160)
print("CORAL PINK 38.5")
getPrices(coral_pink_7W,130)
print("CORAL PINK 39")
getPrices(coral_pink_75W,130)
print("CORAL PINK 39.5")
getPrices(coral_pink_8W,130)
print("350 CREAM 42 2/3")
getPrices(cream_350_9,220)
print("350 BLACK 40")
getPrices(black_350_7,220)
print("350 TRUE FORM 39 1/3")
getPrices(true_form_350_65,220)
print("350 ANTLIA 40")
getPrices(antlia_350_7,220)
print("500 BONE WHITE 40 2/3")
getPrices(bone_white_500_75,200)
print("700 VANTA 42")
getPrices(vanta_700_85,270)
print("700 UTILITY BLACK 36 2/3")
getPrices(utility_black_700_45,300)
print("JORDAN 1 TRAVIS 41")
getPrices(jordan1_travis_8,190)
print("JORDAN 1 LA TO CHI 41")
getPrices(jordan1_la_to_chi_8,160)
#print("ASICS 41.5")
#getPrices(asics_8,140)
print("DUNK PARRA 40.5")
getPrices(dunk_parra_75,100)
print("BLAZER PARRA 41")
getPrices(dunk_blazer_8,100)
print("AF1 TRAVIS 21")
getPrices(af1_travis_5c,60)
print("VAPORSTREET 42")
getPrices(vapor_street_85,90)
print("PARKA LIBERTY TNF SUPREME RED M")
getPrices(parka_liberty_red_m,420)
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()
#print("")
#getPrices()


print(total_profit)
print(total_sales)

