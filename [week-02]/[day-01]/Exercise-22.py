a = 24
out = 0

print(out)

b = 13
out2 = ""
if b > 10 and b < 20:
    out2 = "Sweet!"
elif b < 10:
    out2 = "More!"
elif b > 10:
    out2 = "Less!"

print(out2)

c = 123
credits = 100
is_bonus = False
if credits >= 50 and is_bonus == False:
    c -= 2
elif credits < 50 and is_bonus == False:
    c -= 1

print(c)

d = 8
time = 120
out3 = ""
if d%4==0 and time <= 200:
    out3 = "Check"
elif time > 200:
    out3 = "Time out"
else:
    out3 = "Run Forest Run!"

print(out3)