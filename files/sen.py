with open ("info.txt","r") as file:
     data=file.read()
     data=data.replace(" ","+")


with open ("info.txt","w") as file:
   file.write(data)

