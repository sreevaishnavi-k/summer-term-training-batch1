s=7659
h=3600
m=60
h1=s//h
print(h1,"hrs :",end=" ")
rm=s%h
m1=rm//m
print(m1,"min :",end=" ")
rs=s%m
ss=rs//1
print(ss,"sec",end=" ")
