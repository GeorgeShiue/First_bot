import datetime

time = input()
time2 = datetime.datetime.now().strftime("%Y%m%d")
final = time2 + time
final_time = datetime.datetime.strptime(final, "%Y%m%d%H%M")
print(final_time)
print(final_time.strftime("%H:%M"))