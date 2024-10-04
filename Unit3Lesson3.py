items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
for i in range(len(items)): 
    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)):
    if(sizes[i]==len(items[i])):
      print("Since %s has a size of %d this is True" % (items[i], sizes[i]))
    else:
      print("Since %s does not have a size of %d this is False" % (items[i], sizes[i]))
