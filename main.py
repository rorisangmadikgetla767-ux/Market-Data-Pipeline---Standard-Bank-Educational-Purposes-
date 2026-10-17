import yfinance as yf
from schemas import PriceBar
from decimal import Decimal
import pandas as pd
from pydantic import ValidationError

# Checking the Standard bank stock w yfinance - SBK.JO
ticker = yf.Ticker('SBK.JO')
data = ticker.history(period="1y")

bars = []
skipped = 0
rejected = 0
for date, row in data.iterrows():
    # I have to do a Nan Check , meaning checking missing values
    #Below is my first attempt at NaN check(NaN = Not a Number)
    if pd.isna(row['Close']):
        skipped += 1
        print(skipped)
        print('skipping', date)
        continue
    
    try:
        bar = PriceBar(
            symbol='SBK.JO',
            date=date.date(),
            open = Decimal(str(row['Open'])),
            high = Decimal(str(row['High'])),
            low = Decimal(str(row['Low'])),
            close= Decimal(str(row['Close'])),
            volume=int(row['Volume'])
            
        )
        bars.append(bar)
    except ValidationError:
        print('Rejected', date)
        rejected += 1
       
    
        
        
    
    
    bars.append(bar)
print(skipped, 'rows skipped')
print(bars[0])