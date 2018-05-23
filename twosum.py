def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    #use list index as the hash_table value and list item as  hash_table key
    hash_table = {}
    for i, num in enumerate(nums):
        if target - num in hash_table:
            return  hash_table[target-num] , i
        hash_table[num] = i




if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print (twoSum(nums, target))