Simple requests CLI based program to get last sales of a product from StockX

## Requirements

*Python 3*  
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
python main.py --keyword your keywords --sizes your sizes --sales salesNumber --save boolean
```
*Exemple*

```
python main.py jordan 1 mocha --sizes 8 9 10 --sales 20 --save True
```

This will look for the 20 last sales of the Jordan 1 Mocha in size 8, 9 and 10.

## Current features
- [x] Ask for keywords  
- [x] Ask for several sizes
- [x] Ask for the amount of sales
- [x] Retrieving last sales  
- [x] CLI UX (argparse)
- [x] Saving data as a csv file
- [x] Plots creation (pandas) to better vizualize sales

## Upcoming features  
- [ ] sklearn implementation (forecasting model)
- [ ] tkinter GUI
- [ ] colorway and shoe model addition as predictors

### CLI UX (argparse)

You will have to provide different arguments to make the program work, all of them are required except for the `--save` one
Upon launch, you will be asked keywords, size and the number of sales as well as the possibility
Keywords have to match the product you are trying to get data from.  
The amount of sales are the total amount of sales you want to be displayed.  

### Retrieving last sales   

Getting data using `Requests` python module

### Saving them to a file

Simple .csv format saving  

### Plots creation

Plots creation will be created grouping sales by 7-days-period and saved as a .png file