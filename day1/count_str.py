str1=input()
str2=''
i=0
count=1
for i in range(len(str1)-1):
    if str1[i]==str1[i+1]:
        count=count+1
        i=i+1
    else:
        str2=str2+str1[i]+str(count)
        count=1
        i=i+1
str2=str2+str1[-1]+str(count)
print(str2)