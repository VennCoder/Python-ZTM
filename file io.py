# Open the file in read and write mode
with open(r'C:\Users\aksha\Desktop\txt.txt', mode='r+') as nyu:
    # Read and print the content of the file directly
    nyu.write(input("Write something: "))
    nyu.seek(0)
    print(nyu.read())
