'''
pups = []
temp = []
for _ in range(int(input("antal"))):
    pups.append([input("Name"), input("Score")])

pups.sort(key = lambda x: x[1], reverse = True)

print(pups)

for pup in pups:
    if pup[1] == pups[-2][1]:
        temp.append(pup)

temp.sort()
print(temp)
'''

a = 2
b = 3

print()
