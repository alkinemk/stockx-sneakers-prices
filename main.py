import requests 
from getPrices import getPrices, getUrl

s = requests.session()
keywords = input("Welcome ! Enter keywords and press enter\n")
size = input("Now enter size and press enter\n")
numberOfSales =  input("Finally enter the number of sales you want\n")
numberOfSales = int(numberOfSales)

def getAPIurl():

  headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en;q=0.5",
    "x-algolia-api-key": "6bfb5abee4dcd8cea8f0ca1ca085c2b3",
    "x-algolia-application-id": "XW7SBCT9V6"
  }
  
  
  response = s.post(url = "https://xw7sbct9v6-dsn.algolia.net/1/indexes/products/query",headers=headers, json = {"query":keywords,"facets":"*","filters":""})
  
  json_data = response.json()
  url = json_data["hits"][0]["url"]
  api_url = "https://stockx.com/api/products/"+url
  
  return(api_url)
  
getPrices(getAPIurl(),size,numberOfSales)
  
  

  

