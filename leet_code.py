nums = [3, 3]
target = 6


def twoSum(nums, target):
    second_list = nums.copy()
    target_numbers = []

    while second_list:
        concurrent_num = second_list.pop(0)

        if len(target_numbers) == 2:
            break

        for x in range(len(second_list)):
            if concurrent_num + second_list[x] == target:
                target_numbers.append(concurrent_num)
                target_numbers.append(second_list[x])

    idx1 = nums.index(target_numbers[0]) if target_numbers else None
    nums.remove(target_numbers[0])
    idx2 = nums.index(target_numbers[1]) if target_numbers else None

    return [idx1, idx2 + 1]


print(twoSum(nums, target))#
