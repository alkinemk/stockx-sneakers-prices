Simple requests CLI based program to retrieve last sales of a product from StockX

## Requirements

- Python 3  
```
pip3 install -r requirements.txt
```

## Commands

```
git clone
```

```
cd stockx-sneakers-prices
```

```
python main.py
```

## Current features
- [x] Ask for keywords  
- [x] Ask for a size
- [x] Ask for the amount of sales
- [x] Retrieving last sales  


## Upcoming features  
- [ ] Saving them to a file  
- [ ] improve code readability and structure
- [ ] .csv file formatting
- [ ] Several sizes implementation
- [ ] Asking the user for confirmation
- [ ] Improving terminal UX and UI  
- [ ] Improving `README.md` file design
- [ ] Implementing a while loop   
- [ ] Graphs creation  
- [ ] Linear regression on the resell price of a product  

### Listening for keyword  

Upon launch, you will be asked keywords, size and the number of sales.  
Keywords have to match the product you are trying to get data from.  
The amount of sales are the total amount of sales you want to be displayed.  

### Retrieving last sales   

Getting data using `Requests` python module

### Saving them to a file

Simple .txt format saving  

