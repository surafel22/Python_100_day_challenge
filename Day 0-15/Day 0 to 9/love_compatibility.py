name_1 = input("what is your name ")
name_2 = input("what is your partner name ")
name = name_1 + name_2
lower_name = name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e_1 = lower_name.count("e")

f_digit = int(t + r + u + e)
s_digit = int(l + o + v + e )

digit_int1 =f"{f_digit}{s_digit}"
print(digit_int1)
digit_int = int(digit_int1)
if digit_int < 10 or digit_int >= 90:
    print("you are like coke and mentos")
else:
    print("it is alright")

print(type(digit_int))