class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1=[]
        list2=[]
        list3=[]
        for num in nums:
            if num>pivot:
                list2.append(num)
            elif num<pivot:
                list1.append(num)
            else:
                list3.append(num)
        return (list1+list3+list2)

        



        