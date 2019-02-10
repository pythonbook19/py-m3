import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from db import list_users
from db import query_user_last_seen
from datetime import timedelta, datetime as dt

def check_user_is_active(username):
    last_seen = query_user_last_seen(username)
    delta = last_seen - dt(year = 2018, month = 7, day = 12)
    if  delta.days < 180  :
        return True
    else:
        return False
print (check_user_is_active('anton4'))
