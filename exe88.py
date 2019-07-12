bb,cc=input().split()
cc=int(cc)
aa=list(map(int,input().split())) 
sum=0
for i in range(0,cc):
  sum+=aa[i]
print(sum)
