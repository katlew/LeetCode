
# read file while loop
grocdat = open("grocery.txt", "rU")
line = grocdat.readline
while line:
	print(line)
	line = grocdat.readline()

# read file for loop
grocdat.close()
grocdat = open("grocery.txt","rU")
for line in grocdat:
	print(line)

# write to a file 
fh = open("blah.txt", "w")
varstr = "apple"
vardig = 1
varflt = 1.543232432				# %g < -4
array = [1, 2, 3]
fh.write("I ate %3.1f" % (varflt))	# 1.5
fh.close()

# string manipulation
grocdat = open("grocery.txt","rU")
line = grocdat.readline()
line.strip()		# gets rid of white space on beginning and end
line.strip().split('\t')		# delimiter \t line[0], line[1], line[2]
print line


mydict = {}
grocdat = open("grocery.txt","rU")
line = grocdat.readline()
for line in fh:
	if line.startswith('Product'):
		continue
	# set default
	# manipulate data structure setdefault(key, value)
	# dictionry that holds dictionaries
	# {Product : {Quantity: Price}, Product2 ..etc etc.}
	fields = line.strip().split('\t')
	mydict.setdefault(fields[0],dict()).setdefault('quantity',fields[1])
	mydict.setdefault(fields[0],dict()).setdefault('price', fields[2])

# dictionary with list, append so don't ovewrite duplicates
for line in fh:
	if line.startswith('Product'):
		continue
		fields = line.strip().split('\t')
		mydict.setdefault(fields[0],dict()).setdefault('quantity',list()).append(fields[1])
		mydict.setdefault(fields[0],dict()).setdefault('price', list()).append(fields[2])


for line in fh:
	if line.startswith('Product'):
		continue
		fields = line.strip().split('\t')
		mydict.setdefault(fields[0],dict()).setdefault('quantity',list()).append(int(fields[1]))
		mydict.setdefault(fields[0],dict()).setdefault('price', list()).append(float(fields[2]))
