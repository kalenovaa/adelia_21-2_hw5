import os
from envparse import env

env.read_envfile('settings.env')
money = int(os.getenv('MY_MONEY'))
print(money)