# pip install pytz
# .\.env\Scripts\activate
# pip install pytz
# trocar para interpretador '.env':venv

import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)