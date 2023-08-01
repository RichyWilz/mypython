# this function takes in a string and makes every first letter in it capital
def titlecase(str):
   array = str.split(" ")
   print(array)
   newarray = []
   i = 0
   for i in range(len(array)):
    newarray.append(array[i].upper() + array[i].slice(1).lower())
   return print(newarray)



titlecase("I'm a little off for today")
# the first commit. I'll try to change status
#my second commit. still didnt work, but will keep trying