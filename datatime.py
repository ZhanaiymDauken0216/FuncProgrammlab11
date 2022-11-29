import datetime

tdate=datetime.date(2022,11,29)
print("Date Format:",tdate)

tdate=datetime.date.today()
print("Today Date:",tdate)

print("Year:",tdate.year)
print("Month:",tdate.month)
print("Day:",tdate.day)

wday=tdate.weekday()
print("Weekday:",wday)

isowday=tdate.isoweekday()
print("ISO Weekday:",isowday)

tdelta=datetime.timedelta(days=5)
print("Time Delta:",tdate-tdelta)

ny=datetime.date(2022,1,1)
daypass=tdate-ny
print("No of Days Passed:",daypass.days)

ttime=datetime.time(6,30,45)
print("Time:",ttime)

hours=ttime.hour
print("Hours:",hours)

minutes=ttime.minute
print("Minutes:",minutes)

sec=ttime.second
print("Seconds:",sec)

ttime=datetime.datetime.today()
print("Today Date & Time:",ttime)

cdate=ttime.strftime("%Y/%m/%d")
print("Today Date:",cdate)

ctime=ttime.strftime("%H:%M:%S")
print("Current Time:",ctime)

datetostr="29 november 2022"
out=datetime.datetime.strptime(datetostr,"%d %B %Y").date()
print("Date:",out)
