class Solution:
    def find_frequency(self, arr):
        dict={}
        max=0
        for i in arr:
            if i in dict:
                dict[i]+=1
                if max<dict[i]:
                    max=dict[i]
            else:
                dict[i]=1
        return dict, max
        

obj=Solution()
arr=[1,1,2,3,4,4,4,5,5,6,7,8,8,8]
result, max=obj.find_frequency(arr)
print(result, max)