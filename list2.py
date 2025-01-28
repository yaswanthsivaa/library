#6

# strs = ['str1','str2','str3','str4','str5','str6']

# inp = input('enter a word in above occurences:  ')

# print(strs.count(inp))


#7

# value = [i**2 for i in range(1,51) if i %2 == 0]

# print(value)

#8
# value = [i**2 for i in range(1,51) if i%2 != 0]

# print(value)

#9

# nested = []

# listing = ['str1','str2',['str3','str4']]

# def flatThem(List):
#   for item in List:
#     if isinstance(item,list):
#       flatThem(item)
#     else:
#       nested.append(item)
# flatThem(listing)

# print(nested)

#10

nums = [1,2,1,2]
setting = {}
for i in nums:
  for j in nums:
    if i == j:
      set.add(j)
for k in setting:
  k.rfind()