from persiantools.jdatetime import JalaliDate, JalaliDateTime
import pytz

# now = JalaliDateTime(1402, 5, 19, 12, 56, 0, 0, pytz.utc).strftime("%c")
# # now = now.split()
# # print(now[0])
# print(now.split()[0])

now = JalaliDateTime(1402, 5, 19, 12, 56, 0, 0, pytz.utc).strftime("%d")
print(now)
