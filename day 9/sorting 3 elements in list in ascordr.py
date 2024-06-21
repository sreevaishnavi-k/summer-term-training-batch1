li=[4,9,8,2,14,3,5,6]
for i in range(len(li)-2):
    if li[i]>li[i+1]:
        li[i],li[i+1]=li[i+1],li[i]
    if li[i]>li[i+2]:
        li[i],li[i+2]=li[i+2],li[i]
    if li[i+1]>li[i+2]:
        li[i+1],li[i+2]=li[i+2],li[i+1]
print(li)
    