import yfinance as yf
from schemas import PriceBar
from decimal import Decimal

# Checking the Standard bank stock w yfinance - SBK.JO
ticker = yf.Ticker('SBK.JO')
data = ticker.history(period="1y")

bars = []
for date, row in data.iterrows():
    bar = PriceBar(
        symbol='SBK.JO',
        date = date.date(),
        open=Decimal(str(row['Open'])),
        high=Decimal(str(row['High'])),
        low= Decimal(str(row['Low'])),
        close= Decimal(str(row['Close'])),
        volume=int(row['Volume'])
        
        
    )
    bars.append(bar)
print(bars[0])