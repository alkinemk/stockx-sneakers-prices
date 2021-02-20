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
python3 src/scraper.py --keywords your keywords
```
*Example*

```
python3 src/scraper.py jordan 1 mocha
```

This will look for the 250 last sales of the Jordan 1 Mocha.

By default, it will retrieve the last 250 sales but can be less if there has not been that many.

## Current features
- [x] Ask for keywords (argparse)
- [x] Retrieving last sales  
- [x] Saving data as a csv file
- [x] Dataframes creation (pandas)
- [x] Charts creations (matplotlib)

## Upcoming features  
- [ ] machine learning models implementation (sklearn)
- [ ] deep learning implementation to predict prices (tensorflow)

### CLI UX (argparse)

It asks the user for the keywords.

### Retrieving last sales   

Getting data using `Requests` python module

### Saving them to a file

Simple .csv format saving  

### Plots creation

Plots creation will be created grouping sales by periods (7-day or 1-month for instance) and saved as a .png file