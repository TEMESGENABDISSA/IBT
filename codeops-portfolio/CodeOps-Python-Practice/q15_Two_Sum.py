def two_sum(nums,target):
    
    seen={}


    for index,value in enumerate(nums):

        needed=target-value


        if needed in seen:

            return [
                seen[needed],
                index
            ]


        seen[value]=index