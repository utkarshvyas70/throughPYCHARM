f=open("demofile.txt","r")
print(f.read())

#you want to read certain number of characters only
f=open("demofile.txt","r")
print(f.read(24))

#want to read only first line
f=open("demofile.txt","r")
print(f.readline())
f.close()

#want to read many lines
f=open("demofile.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

#open file and append content
f=open("demofile.txt","a")
f.write("fjkvnnvfjndfjvnijvndivjnndvidnin")
f.close()
f=open("demofile.txt","r")
print(f.read())

#open the file and overwrite
f=open("demofile.txt","w")
f.write("fvfvdfvdvdfv")
f.close()
f=open("demofile.txt","r")
print(f.read())
