def majority_elementsII(nums):
    "using moore's voting algorithm"
    n=len(nums)
    ele1=-1
    ele2=-1
    cnt1=0
    cnt2=0
    for ele in nums:
        # new candidate 1 if cnt1 is 0
        if cnt1==0:
            ele1=ele
            cnt1+=1
        # new candidate 2 if cnt2 is 0
        elif cnt2==0:
            ele2=ele
            cnt2+=1
        # If the ele is equal to ele1 increment cnt1 by 1
        elif ele1==ele:
            cnt1+=1
        # If the ele is equal to ele2 incerement cnt2 by 2
        elif ele2==ele:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    res=[]
    cnt1 , cnt2 = 0, 0
    
    for ele in nums:
        if ele1==ele:
            cnt1+=1
        if ele2==ele:
            cnt2+=1
              
    if cnt1>n/3:
        res.append(ele1)
    if cnt2>n/3 and ele1!=ele2:
        res.append(ele2)
    # if len(res) == 2 and res[0] > res[1]:
    #     res[0], res[1] = res[1], res[0]
    
    return res
          
nums = [11, 33, 33, 11, 33, 11]
result=majority_elementsII(nums)
print("majority elements: ",result)