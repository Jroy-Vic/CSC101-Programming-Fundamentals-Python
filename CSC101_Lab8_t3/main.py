# Purpose: Find the average of each sublist in a list of list (2D)
# Input: list[list[int]]
# Output: list[float]
# Example Input: [[1,2], [7,5,4], [2], [9,0]]
# Example Output: [1.5, 5.33, 2.0, 4.5]

def avg_of_sub_lists(some_list: list[list[int]]) -> list[float]:
    avg_list = []
    for sub_list in some_list:
        total = 0
        terms = len(sub_list)
        for value in sub_list:
            total = total + value
        avg = total / terms
        avg_list.append(avg)
    return avg_list


def avg_of_neighbors(list_in: list[list[int]]) -> list[float]:
    avg_list = []
    for sub_idx in range(len(list_in)):

        total_prev = 0
        len_prev = 0
        if sub_idx - 1 >= 0:
            len_prev = len(list_in[sub_idx - 1])
            for value in list_in[sub_idx - 1]:
                total_prev = total_prev + value

        total_curr = 0
        len_curr = len(list_in[sub_idx])
        for value in list_in[sub_idx]:
            total_curr = total_curr + value

        total_next = 0
        len_next = 0
        if sub_idx + 1 < len(list_in):
            len_next = len(list_in[sub_idx + 1])
            for value in list_in[sub_idx + 1]:
                total_next = total_next + value

        avg = (total_next + total_curr + total_prev) / (len_curr + len_next + len_prev)
        avg_list.append(avg)
    return avg_list

def test(list_in) -> float:
    avg_list = []
    for sub_idx in range(len(list_in)):
        
        if sub_idx == 0:
            total = 0
            total_len = len(list_in[sub_idx]) + len(list_in[sub_idx + 1])
            for value in list_in[sub_idx]:
                total = value + total
            for value in list_in[1]:
                total = value + total
            avg = total / total_len
            avg_list.append(avg)
        elif sub_idx == len(list_in) - 1:
            total = 0
            total_len = len(list_in[sub_idx]) + len(list_in[sub_idx - 1])
            for value in list_in[sub_idx]:
                total = value + total
            for value in list_in[sub_idx - 1]:
                total = value + total
            avg = total / total_len
            avg_list.append(avg)
        else:
            total = 0
            total_len = len(list_in[sub_idx]) + len(list_in[sub_idx - 1]) + len(list_in[sub_idx + 1])
            for value in list_in[sub_idx]:
                total = value + total
            for value in list_in[sub_idx - 1]:
                total = value + total
            for value in list_in[sub_idx + 1]:
                total = value + total
            avg = total / total_len
            avg_list.append(avg)
    return avg_list



if __name__ == '__main__':
    main_list = [[1,2], [7,5,4], [2], [9,0]]
    avgs_of_main_list = avg_of_sub_lists(main_list)
    print(avgs_of_main_list)
    avgs_of_neighbors = avg_of_neighbors(main_list)
    print(avgs_of_neighbors)
    avgs = test(main_list)
    print(avgs)
