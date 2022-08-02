with open("newfile.txt","r") as f:#with context manager file got automatically closed
    data=f.read()
    print(data)
    print("is file closed",f.closed)
print("is file closed",f.closed)    
