# Roy Vicerra - Lab 3 Task 2

def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num
    return total  # num = 4, total = 4
                  # num = 9, total = (4) + 9 = 13
                  # num = 2, total = (13) + 2 = 15
                  # num = 1, total = (15) + 1 = 16

result = tally([4, 9, 2, 1])

# ~~~~~~

# Roy Vicerra - Lab 3 Task 2

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])  # idx = 0, new_list = [4]
                                    # idx = 1, new_list = [4,9]
                                    # idx = 2, new_list = [4,9,2]
                                    # idx = 3, new_list = [4,9,2,1]
    return new_list  # This loop differs from that above in three ways: 1) it utilizes two different lists,
                     # 2) it returns a list instead of an int, and 3) it uses "dummy" variables from range(4)
                     # instead of from the list itself.

result = copy([4, 9, 2, 1])

# ~~~~~~

# Roy Vicerra - Lab 3 Task 2

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)
    return new_list  # value = 4, new_list = [5]
                     # value = 9, new_list = [5, 10]
                     # value = 2, new_list = [5, 10, 3]
                     # value = 1, new_list = [5, 10, 3, 2]

result = increment_all([4, 9, 2, 1])
