#from os import path

import datetime

d = datetime.date(2016, 7, 24)
today = datetime.date.today()

#print(d)
#print(today)
#print(today.year)
#print(today.day)

#print(today.weekday()) #monday - 0; sunday - 6
#print(today.isoweekday()) #monday - 1; sunday - 7

tdelta = datetime.timedelta(days=7)

# print(today + tdelta)
# print(today - tdelta)

#date = date + timedelta
#timedelta = date1 + date2

bday = datetime.date(2017, 5, 9)

till_bday = bday - today

#print(till_bday) #days to birth day
#print(till_bday.total_seconds()) #in seconds


#t = datetime.time(9, 30, 45, 100000)

# print(t)
# print(t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
tdelta_7 = datetime.timedelta(days=7)
tdelta_12 = datetime.timedelta(hours=12)

# print(dt + tdelta_7)

# print(dt + tdelta_12)

# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

#https://youtu.be/eirjjyP2qcQ?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&t=726