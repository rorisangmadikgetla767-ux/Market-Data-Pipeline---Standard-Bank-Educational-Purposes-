import yfinance as yf
from schemas import PriceBar
from decimal import Decimal

# Checking the Standard bank stock w yfinance - SBK.JO
ticker = yf.Ticker('SBK.JO')
data = ticker.history(period="1y")

bars = []
for date, row in data.iterrows():
    bar = PriceBar(
        symbol='SBK.JO'
        
    )