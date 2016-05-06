import re

# string = "not integer -1 -4 5 8 10 11 12.5"
# ints = re.findall(r'-?\d+', string)
# ints = list(map(int, ints))
# avg = sum(ints) / len(ints)
# print(avg)

ipaddr = "192.168.1.1"
if re.match(r"(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]){3}", ipaddr) is not None:
    print("Valid IP")
else:
    print("Invalid IP")