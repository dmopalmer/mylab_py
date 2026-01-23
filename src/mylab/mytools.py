"""
Miscellaneous tools
dmopalmer@gmail.com

"""

from datetime import datetime
import datetime as dt
from dateutil.parser import parse as parsedate

def parse_as_utc(datein: str | datetime):
    if isinstance(datein, str):
        datein = parsedate(datein, default=parsedate("00:00Z"))
    else:
        datein = datein.replace(tzinfo=datetime.UTC)
    return datein

__all__ = ['parsedate', 'parse_as_utc']
