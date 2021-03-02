import re
sum = 0

pattern = 'back'
if re.match(pattern, 'backup.txt'):
    sum += 1
    print("1...",sum)
if re.match(pattern, 'text.back'):
    sum += 2
    print("2...",sum)
if re.search(pattern, 'backup.txt'):
    sum += 4
    print("3...",sum)
if re.search(pattern, 'text.back'):
    sum += 8
    print("4...",sum)

print(sum)
