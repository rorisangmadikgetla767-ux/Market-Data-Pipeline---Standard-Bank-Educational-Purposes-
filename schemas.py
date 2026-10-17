from datetime import date
from decimal import Decimal
from pydantic import BaseModel, model_validator

class PriceBar(BaseModel):
    symbol: str
    date: date
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int
    @model_validator(mode='after')
    def check_high_low(self):
        if self.high < max(self.open, self.close):
            raise ValueError('high can not be lower than close or low')
        else:
            return self
            
        
    

    

    
