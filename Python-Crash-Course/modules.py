import datetime
from time import time
from camelcase import CamelCase

today = datetime.date.today()
print(today)

# from datetime import date

# today = date.today()

timestamp = time()
print(timestamp)

c = CamelCase()
print(c.hump('hello world peace love'))
