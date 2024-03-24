import re

txt = "vsm bba and bca college"
x = re.match("vsm", txt)
print(x.group())

txt = "vsm bba and bca college"
x = re.search("^vsm.*college$", txt)
print(x.group())

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "vsm bba and bca college"
x = re.sub("\s", "9", txt)
print(x)

txt = "vsm bba and bca college"
x = re.split("\s", txt)
print(x)
