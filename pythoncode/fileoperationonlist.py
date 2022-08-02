f=open("sbc.txt","w")
list=["python\n","javascript\n","mysql\n","oracle"]
f.writelines(list)
print("list written to files successfully")
f.close()
