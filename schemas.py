from datetime import date
from decimal import Decimal
from pydantic import BaseModel
class PriceBar(BaseModel):
    symbol: str
    date: date
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int
    

    
