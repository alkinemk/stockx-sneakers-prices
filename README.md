Simple requests based program to retrieve specific data from StockX

# Requirements
-python installed on your computer  
-change the python file according to what product you would like to get info from (links are always in the form `https://stockx.com/api/products/name_of_your_product`)  
-you can get the name_of_your_product by analysing get requests in the Network tab of your developer tools  
-once you have it use `getPrices(link_to_your_product,'your_desired_size',number_of_sales)`

# Commands

```
git clone
```

```
cd stockx-sneakers-prices
```

```
python main.py
```

# TODO

-using beautifulsoup to retrieve product only from a few keywords rather than hard-pasting it  
-making it more interactive (shell interaction) and completely automated
