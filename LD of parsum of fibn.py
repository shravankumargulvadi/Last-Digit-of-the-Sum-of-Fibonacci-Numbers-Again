
# coding: utf-8

# In[11]:


import numpy as np
def LD_parsum_fib(j, k):
    
    j=j-1
    a=np.random.randint(1, 10000, 3)
    b=np.random.randint(1, 10000, 3)
    a[0]=0
    b[0]=0
    sumj=0
    sumk=0
    if j>0:
        a[1]=1
        sumj=1
        i=indexfinder(10)
        if j<=i:
            for j in range(2, j+1):
                a[2]=(a[0]+a[1])%10
                a[0]=a[1]
                a[1]=a[2]
                sumj=sumj+a[2]
        if j>i:
            sumj=sumfinderj(i)
            sumj=int(j/(i))*sumj+sumfinderj(j%(i))
            
    if k>0:
        b[1]=1
        sumk=1
        i=indexfinder(10)
        if k<=i:
            for k in range(2, k+1):
                b[2]=(b[0]+b[1])%100
                b[0]=b[1]
                b[1]=b[2]
                sumk=sumk+b[2]
        if k>i:
            sumk=sumfinderk(i)
            sumk=int(k/(i))*sumk+sumfinderk(k%(i))
    #print(sumj)
    #print(sumk)
    sum= abs(sumk-sumj)    
    return sum%10
def sumfinderk(m):
    a=np.random.randint(1, 10000, 3)
    a[0]=0
    sum=0
    if m>0:
    
        a[1]=1
        sum=1
        for q in range(2, m+1):
            a[2]=(a[0]+a[1])%100
            a[0]=a[1]
            a[1]=a[2]
            sum=sum+a[2]
    #print(sum)            
    return sum%100
def sumfinderj(m):
    a=np.random.randint(1, 10000, 3)
    a[0]=0
    sum=0
    if m>0:
    
        a[1]=1
        sum=1
        for q in range(2, m+1):
            a[2]=(a[0]+a[1])%10
            a[0]=a[1]
            a[1]=a[2]
            sum=sum+a[2]
    #print(sum)            
    return sum%10
def indexfinder(m):
    i=1
    a=0
    f=np.random.randint(1, 100, 2)
    f[0]=0
    f[1]=1
    while a!=1:
        f=np.float64(f)
        z=f[1]
        f[1]=f[0]+f[1]
        f[0]=z
        f[0]=f[0]%m
        f[1]=f[1]%m
        
        a=(f[0])+(f[1])
        a=np.float64(a)
        
        
        if a==1:
            #print('completed index \n')
            #print(i+1)
            return i+1
        else:
            i=i+1
            #print(i)
if __name__ == '__main__':
    input_n = 2
    input_numbers = [int(x) for x in input().split()]
    print(LD_parsum_fib(input_numbers[0],input_numbers[1]))

