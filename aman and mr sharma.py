d=int(input())
count=0
for i in range(0,d):
   r,x=input().split(' ')
   c=(44*int(r))/7
   w=100*int(x)
   if w>=c:
      count+=1
   else:
      count+=0
print(count)
      
