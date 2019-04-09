#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:21:31 2019

@author: Jacques
"""

from iexfinance.stocks import get_historical_data
from datetime import datetime

start = datetime(2017,1,1)
end = datetime(2018,1,1)
data = get_historical_data("AAPL", start=start, end=end, output_format="pandas")

import numpy as np
import pandas as pd
#Type your code here
infy = pd.read_csv('infy_data.csv')

print (infy.head ()) # You will see the top 5 rows
print ('\n')
print (infy.tail ()) # You will see the bottom 5 rows

infy_close = infy[['Date', 'Close Price']]
