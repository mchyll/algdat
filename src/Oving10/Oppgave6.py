import re


print(re.match(".*\d.*", "7") is not None)

print(re.match("\d{2}/\d{2}/\d{4}", "12/34/9898") is not None)

print(re.match(".{10,}", "asdssab bab") is not None)

print(re.match(".*[^a-åA-Å].*", "aaåbbab") is not None)
