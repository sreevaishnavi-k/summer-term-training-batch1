y=360
m=30
w=6
d=65476
y1=d//y
print(y1,"years",end=" ")
rm=d%y
m1=rm//m
print(m1,"months",end=" ")
rd=d%m
w1=rd//w
print(w1,"weeks",end=" ")
rdd=d%w
d1=rdd//1
print(d1,"days")