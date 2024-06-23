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
    return new_list  # This loop differs from that above because it utilizes two different lists

result = copy([4, 9, 2, 1])
