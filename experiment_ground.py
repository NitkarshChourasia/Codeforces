# # def hello_world():
# #     # Read the number of words
# #     n = int(input())

# #     # Process each word
# #     for _ in range(n):
# #         word = input().strip().lower()

# #         # Check if the word is too long
# #         if len(word) > 10:
# #             # Abbreviate the word
# #             abbreviated_word = word[0] + str(len(word) - 2) + word[-1]
# #             print(abbreviated_word)
# #         else:
# #             # Word is not too long, print it as is
# #             print(word)


# # print(hello_world())

# class Solution:
#     def hello_world(self):
#         # Read the number of words
#         n = int(input())

#         # Process each word
#         for _ in range(n):
#             word = input().strip().lower()

#             # Check if the word is too long
#             if len(word) > 10:
#                 # Abbreviate the word
#                 abbreviated_word = word[0] + str(len(word) - 2) + word[-1]
#                 print(abbreviated_word)
#             else:
#                 # Word is not too long, print it as is
#                 print(word)

#     def smallerNumbersThanCurrent(self, nums):
#         result_list = []
#         for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if i != j and nums[j] < nums[i]:
#                     count += 1
#             result_list.append(count)
#         return result_list

# # Create an instance of the Solution class
# solution = Solution()

# # Call the hello_world method
# solution.hello_world()

# # Call the smallerNumbersThanCurrent method
# nums = [5, 2, 6, 1]
# print(solution.smallerNumbersThanCurrent(nums))


# def bit_manipulation(runs: int) -> int:
# Read the number of runs
# runs = int(input())
# runs = int(input())
# i = 0
# # Process each run
# for _ in range(runs):
#     # Read the number of bits
#     read_line = input()

#     if "++" in read_line:
#         i += 1
#     elif "--" in read_line:
#         i -= 1
# print(i)

# dim_x, dim_y = map(int, input().split())
# board_size = dim_x * dim_y
# PIECE_SIZE = 1 * 2

# while True:
#     if board_size % 2 != 0:
#         board_size -= 1
#     else:
#         break
# print(board_size // PIECE_SIZE)

# n, k = map(int, input().split())
# # n, k = 8, 5
# # take an space separated input of n integers and convert to list
# arr = list(map(int, input().split()))
# COUNT = 0
# # arr = [10, 9, 8, 7, 7, 7, 5, 5]
# # duplicates and higher then it
# # COUNT = k
# # i = k
# # # print(i, k)
# # # array starts with index 0
# # # print(arr[i], arr[k - 1])
# # # while True this condition below true:

# # LOOP_COUNTER = 0
# # # ! Define a max loops for while

# # # ! Len starts from 1
# # # ! array starts from 0
# # while LOOP_COUNTER < len(arr):  # This is risky business here.
# #     if arr[k - 1] <= 0 and k != len(
# #         arr
# #     ):  # * For zero cases everywhere and negative cases
# #         COUNT = 0
# #         break
# #     # if all(element == 0 for element in arr):
# #     #     COUNT = 0
# #     # break
# #     elif i != len(arr):
# #         if arr[i] == arr[k - 1]:  # and i < len(arr):
# #             COUNT += 1
# #             i += 1

# #     elif i == len(arr):
# #         reverse = arr[::-1]
# #         compare_to = arr[k - 1]
# #         for ele in reverse:
# #             # zero to focus on
# #             if ele != 0 and (ele == compare_to or ele > compare_to):
# #                 COUNT += 1
# #     else:
# #         break
# #     LOOP_COUNTER += 1
# # # Understand the question more properly for the cases of same number
# # print(COUNT)

# ### What if all are n > 0 and all are same

# # Confirm to this test case yaar
# # 5 5
# # 3 2 1 0 0
# compare_to = arr[k - 1]
# for ele in arr:
#     if ele >= compare_to and ele > 0:
#         COUNT += 1
# print(COUNT)


# INPUT_LOOP_COUNT = 5
# for _ in range(INPUT_LOOP_COUNT):
#     # Read the number of bits
#     arr = input()
#     if "++" in read_line:
#         i += 1
#     elif "--" in read_line:
#         i -= 1

# * This is one way to solve, but it doesn't said to return the whole matrix just the moves of it.
# MIN_MOVES = 0
# for _ in range(5):
#     arr = list(map(int, input()))
# if 1 in arr:
#     # print(arr.index(1))
#     location = arr.index(1)
#     while True:
#         if location's [a,b] (b) == 3:
#             break
#         elif location's [a,b] (b) > 3:
#             b -= 1
#             MIN_MOVES += 1
#         elif location's [a,b] (b) < 3:
#             b += 1
#             MIN_MOVES += 1
#     while True:
#         if location's [a, b] (a) == 3:
#             break
#         elif location's [a, b] (a) > 3:
#             a -= 1
#             MIN_MOVES += 1
#         elif location's [a, b] (a) < 3:
#             a += 1
#             MIN_MOVES += 1
#     print(MIN_MOVES)

# # * Creating a dictionary of arrays
# variables = {}
# for i in range(1, 5 + 1):
#     variables[f"array_{i}"] = []

# # * Taking input of arrays
# for key in variables:
#     variables[key] = list((map(int, input().split())))

# MIN_MOVES = 0
# ROW_COUNT = 0
# COLUMN_COUNT = 0
# # ! This section has error in it.
# for key, value in variables.items():
#     try:
#         ROW_COUNT += 1
#         # print("value_index", value.index(1))
#         # print("row_count", ROW_COUNT)
#         if value.index(1) >= 0:
#             COLUMN_COUNT = value.index(1) + 1
#             # print(COLUMN_COUNT)
#             break
#     except ValueError:
#         pass

# # print(ROW_COUNT, COLUMN_COUNT)

# # print(type(COLUMN_COUNT))
# # * This section is working fine
# while ROW_COUNT != 3:
#     if ROW_COUNT < 3:
#         MIN_MOVES += 1
#         ROW_COUNT += 1
#     elif ROW_COUNT > 3:
#         MIN_MOVES += 1
#         ROW_COUNT -= 1
#     # elif ROW_COUNT == 3:
#     #     break

# while COLUMN_COUNT != 3:
#     if COLUMN_COUNT < 3:
#         MIN_MOVES += 1
#         COLUMN_COUNT += 1
#     elif COLUMN_COUNT > 3:
#         MIN_MOVES += 1
#         COLUMN_COUNT -= 1
#     # elif COLUMN_COUNT == 3:
#     #    break

# print(MIN_MOVES)


# # Read the matrix input
# matrix = [list(map(int, input().split())) for _ in range(5)]

# # Find the position of the number 1
# row, col = None, None
# for i in range(5):
#     for j in range(5):
#         if matrix[i][j] == 1:
#             row, col = i, j

# # Calculate the minimum number of moves
# moves = abs(row - 2) + abs(col - 2)

# # Output the result
# print(moves)


# Laaanat hai yaar ki itna simple implementation ko maine itna complex kar diya
# bc itna dimaag lagaya? aurr kya result nikla?

# # create a dictionary of alphabets with values of their index
# ALPHA = "abcdefghijklmnopqrstuvwxyz"
# alphabets = {}
# i = 0
# for char in ALPHA:
#     i += 1
#     alphabets[char] = i

# # print(alphabets)
# # matrix = [list(map(int, input().split())) for _ in range(5)]
# # variables = {}
# # for i in range(1, 2+1):
# #     variables[f"input_string_{i}"] = input()

# # !lower
# variables = {f"input_string_{i}": input().lower() for i in range(1, 2 + 1)}

# hashmap = {}

# # value and thier value
# arr_1, arr_2 = [], []

# for char in variables["input_string_1"]:
#     if char in alphabets:
#         arr_1.append(alphabets[char])

# for char in variables["input_string_2"]:
#     if char in alphabets:
#         arr_2.append(alphabets[char])

# # compare the values

# # Update the same position and then add theem all and see what is the output and then it is done
# real_range = min(len(arr_1), len(arr_2))

# for i in range(real_range):
#     if arr_1[i] > arr_2[i]:
#         # Update arr_1[i] and arr_2[i] at the same position
#         arr_1[i] = 1
#         arr_2[i] = -1
#         break
#     elif arr_1[i] < arr_2[i]:
#         arr_1[i] = -1
#         arr_2[i] = 1
#         break
#     elif arr_1[i] == arr_2[i]:
#         arr_1[i] = 0
#         arr_2[i] = 0
#         break

# sum_1 = sum(arr_1)
# sum_2 = sum(arr_2)

# if sum_1 > sum_2:
#     print(1)
# elif sum_1 < sum_2:
#     print(-1)
# elif sum_1 == sum_2:
#     print(0)


# # Read the input strings
# str1 = input().lower()
# str2 = input().lower()

# # Compare the strings lexicographically
# if str1 < str2:
#     print("-1")
# elif str1 > str2:
#     print("1")
# else:
#     print("0")


# user_input = input() SPLIT_USER_INPUT = user_input.split("+")
# SPLIT_USER_INPUT.sort()
# SPLIT_USER_INPUT = "+".join(SPLIT_USER_INPUT)
# print(SPLIT_USER_INPUT)


# user_input = input()
# output_string = user_input[0].upper() + user_input[1:]
# print(output_string)


# user_input = set(input())
# if len(user_input) % 2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")

# print("CHAT WITH HER!") if len(set(input())) % 2 == 0 else print("IGNORE HIM!")

# A. Stones on the table

# n = int(input())
# string_input = input()
# REMOVE_COUNTER = 0
# for i in range(n - 1):
#     if string_input[i] == string_input[i + 1]:
#         REMOVE_COUNTER += 1
# print(REMOVE_COUNTER)

# A. Bear and Big Brother
# limak, bob = map(int, input().split())
# i = 0
# while i != 10:
#     limak *= 3
#     bob *= 2
#     i += 1
#     if limak > bob:
#         break
# print(i)


# A. Elephant
# x = int(input())

# # test for five multiples
# STEPS = 0
# for i in range(5, 0, -1):
#     # remainder = x % i
#     if x >= i:
#         division = x // i
#         remainder = x // i
#         # print(f"x1: {x}")
#         x -= division * i
#         # print(f"x2: {x}")

#         # print(f"division: {division}, remainder: {remainder}")
#         STEPS += division
#         if remainder == 0:
#             break
#         elif remainder != 0:  # This line is unnecessary
#             continue
# print(STEPS)

# A. Soldier and Bananas

# initial_value, money_have, quantity_want = map(int, input().split())

# total_cost = 0
# for i in range(1, quantity_want + 1):
#     total_cost += initial_value * i

# to_borrow = total_cost - money_have
# print(0) if to_borrow <= 0 else print(to_borrow)


# A. Word
# str_input = input()
# hashmap = {"upper": 0, "lower": 0}

# arr_str = list(str_input)
# for char in arr_str:
#     if char.isupper():
#         # hashmap.setdefault("upper", 0)
#         hashmap["upper"] += 1
#         # hashmap["upper"] = hashmap.get("upper", 0) + 1
#     elif char.islower():
#         # hashmap.setdefault("lower", 0)
#         hashmap["lower"] += 1
#         # hashmap["lower"] = hashmap.get("lower", 0) + 1

# print(str_input.upper()) if hashmap["upper"] > hashmap["lower"] else print(
#     str_input.lower()
# )


# import numpy as np


# user_input = np.array(list(input()), dtype=int)
# user_input = list(input())
# print(user_input)

# user_input = input()
# ones = "1" * 7
# zeros = "0" * 7
# if (ones or zeros) in user_input:
#     print("YES")
# else:
#     print("NO")

# # ! IMPORTANT Revise it, please.

# n = int(input())
# coin_arr = list(map(int, input().split()))
# coin_arr.sort(reverse=True)

# output_key = 0
# total_value = sum(coin_arr)
# for i in range(n - 1):
#     # Use coin_arr[:i+1] instead of coin_arr[:1] to include the i-th element
#     output_key += 1
#     if sum(coin_arr[: i + 1]) > (total_value - sum(coin_arr[: i + 1])):
#         output_key = i
#         break

# # The length of the first part of the list where the sum becomes greater
# print(len(coin_arr[: output_key + 1]))

# # So the end i has to be handled.
# # So I struggle with this n - 1 cases.
# # So, I struggle with two-pointers.

# 318A- Even Odds


# 7 and 7 answer should be 6 but came 7 so what about odd below is for even
# n, k = map(int, input().split())

# # even_arr = [num for num in range(1, n + 1) if num % 2 == 0]
# # odd_arr = [num for num in range(n + 1) if num % 2 == 1]

# # sorted_arr = []
# # sorted_arr.extend(odd_arr)
# # sorted_arr.extend(even_arr)
# # # print(sorted_arr)
# # print(sorted_arr[k - 1])


# def driver(a, i):
#     diff = 2
#     return a + (i - 1) * diff


# odd_k = n / 2
# even_k = k > odd_k
# if even_k:
#     k = k - odd_k
#     EVEN = 2
#     output = driver(EVEN, k)
#     print(int(output))
# elif even_k != True:
#     ODD = 1
#     output = driver(ODD, k)
#     print(int(output))

# # print(even_k) # if this is True it is in even's range.


# # A. Wrong Substraction

# n, k = map(int, input().split())

# for i in range(k):
#     last_digit = n % 10

#     if last_digit  == 0:
#         n //= 10
#     else:
#         n -= 1

# print(int(n))


# A. Nearly Lucky Number

# # Want to learn it's optimal way.
# n = input()
# # distinct = set(n)
# # if '4' in distinct and '7' in distinct and len(distinct) == 2:
# four_count = n.count("4")
# seven_count = n.count("7")
# total_count = four_count + seven_count
# if total_count == 7 or total_count == 4:
#     print("YES")
# else:
#     print("NO")

# # Another precise way to do it.
# # Here, is the code below.

# n = input()
# if n.count("4") + n.count("7") in {4, 7}:
#     print("YES")
# else:
#     print("NO")


# n = int(input())
# scores = input()

# if scores.count("A") > scores.count("D"):
#     print("Anton")
# elif scores.count("D") > scores.count("A"):
#     print("Danik")
# else:
#     print("Friendship")


# n_friends, fence_height = map(int, input().split())
# friends_height_arr = list(map(int, input().split()))  # Error may throw

# width_road = 0

# for height in friends_height_arr:
#     if height > fence_height:
#         width_road += 2
#     else:
#         width_road += 1

# print(width_road)

# A. Beautiful Year

# year = input()
# # upper_range = 9000 - int(year)
# # print(upper_range)


# def increment_year(year_input):
#     year_input = int(year_input)
#     year_input += 1
#     year_input = str(year_input)
#     return year_input


# year = increment_year(year)
# # print(year)
# # print(set(year))
# # print(len(set(year)))
# # for _ in range(upper_range):
# while True:
#     if len(set(year)) == 4:
#         break
#     else:
#         year = increment_year(year)

# print(year)


# A. In Search of an Easy Problem

# n = int(input())
# n = input()
# responses = list(map(int, input().split()))

# if 1 in responses:
#     print("HARD")
# else:
#     print("EASY")


# n_rooms = input()

# A. Hulk
# ! Not completed
# try to use list comprehension

# One 900 problem and one 800 problem

# n = input()
# hate = "I hate"
# love = "I love"
# arr = []

# # * Can use odd-else with list-comprehension

# # from now on try to use lambda and list comprehensions in your programming journey
# ouput = [arr.update(x) ]
# # can use list comprehension and join

# print(f'')


# n = int(input())
# word = input().lower()

# is_pangram = True

# ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

# for char in ALPHABETS:
#     if char not in word:
#         is_pangram = False
#         break
# if is_pangram:
#     print("YES")
# else:
#     print("NO")

# A. Games
# Write the other method also of doing the list
# n = int(input())
# home_colors, guest_colors = [], []
# for _ in range(n):
#     h, g = map(int, input().split())
#     home_colors.append(h)
#     guest_colors.append(g)

# # # ?for loop to take input??

# # # intersection = sum(elem in home_colors for elem in guest_colors)
# # # print(intersection)

# # GAMES_RANGE = n * (n - 1)
# COUNT = 0
# # for i in range(GAMES_RANGE):
# #     index = i % n
# #     # print(f"index; {index} || i: {i}")
# #     if home_colors[index] in guest_colors:
# #         COUNT += 1
# # print(COUNT)

# for i in range(n):
#     for j in range(n):
#         if i != j and home_colors[i] == guest_colors[j]:
#             COUNT += 1

# print(COUNT)


# A. Amusing Joke

# # Taking inputs
# guest_name = input()
# host_name = input()
# pile = input()

# # Length and sorting
# total_chars = sorted(guest_name + host_name)
# pile_check_from = sorted(pile)
# total_length = len(total_chars)
# COUNT = 0

# # Main logic

# if total_length > len(pile):
#     loop_run = len(pile)
# else:
#     loop_run = total_length

# for i in range(loop_run):
#     if total_chars[i] == pile_check_from[i]:
#         COUNT += 1

# # check_count = sum(char in pile for char in total_chars)
# # print(check_count)

# # Print statements
# if COUNT == total_length and total_length == len(pile):
#     print("YES")
# else:
#     print("NO")


# # A. I_love_%username%

# # Taking inputs
# n = int(input())

# arr = list(map(int, input().split()))
# # for _ in range(n):

# # arr.append(competition_score)

# HIGH, LOW = arr[0], arr[0]
# AMAZING_COUNT = 0
# for i in range(n):
#     if arr[i] < LOW:
#         LOW = arr[i]
#         AMAZING_COUNT += 1
#     elif arr[i] > HIGH:
#         HIGH = arr[i]
#         AMAZING_COUNT += 1

# print(AMAZING_COUNT)


# # A. I Wanna Be the Guy

# total_levels = int(input())
# little_x = list(map(int, input().split()))[1:]
# little_y = list(map(int, input().split()))[1:]

# full_levels = set(little_x + little_y)

# check = any(i not in full_levels for i in range(1, total_levels + 1))

# if check:
#     print("Oh, my keyboard!")
# else:
#     print("I become the guy.")


# A. YES or YES?

# n = int(input())

# for _ in range(n):
#     to_test = input().lower()
#     if to_test == "yes":
#         print("YES")
#     else:
#         print("NO")


# A. Remove Smallest

# n = int(input())
# j0 = 0
# j1 = 1
# for _ in range(n):
#     x = int(input())
#     # print(x)
#     list1 = sorted(list(map(int, input().split())))

#     for i in range(x):
#         # print(i)
#         if len(list1) >= 2:
#             if list1[j1] - list1[j0] <= 1:
#                 del list1[j1]
#             else:
#                 break
#         else:
#             print("YES")

# Will try next time.
# It took 45 minutes as of now.
# **FEEDBACK_ANALYSIS: Major distraction while reading and understanding the problem set ,...
# ** and getting up for fan ,...
# ** and also like stopping for gas and signal, it was like this.


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     list1 = sorted(set(map(int, input().split())))
#     i = 0
#     j = 1
#     truthy_list = []
#     # print(list1)
#     list_size = len(list1)
#     if list_size >= 2:  # is it possible to optimise it?

#         for __ in range(list_size - 1):
#             # print(list1[j], list1[i])
#             if list1[j] - list1[i] != 1:
#                 truthy_list.append(False)
#                 break
#             else:
#                 truthy_list.append(True)

#             i += 1
#             j += 1

#         if len(truthy_list) == 0:
#             print("YES")
#         else:
#             if all(truthy_list):
#                 print("YES")
#             else:
#                 print("NO")

#     else:
#         print("YES")

# Good program I wrote.
# *Index, counters, counters_updates are where mistakes happens.
# *setting i = 0, j = 1 which avoided two loops was the main challenge, here.

# *Favourite One.


# A. Again Twenty Five!

# k = input()
# print(25)


# A. Hit the Lottery

num_list = list(map(int, input()))

list_size = len(num_list)
multiplied_list = []
# will be used as index - finding.
i = 1
j = 0
for _ in range(list_size):
    x = list_size - i
    expo = 10**x

    multiplied_list.append(num_list[j] * expo)

    j += 1
    i += 1

# print(multiplied_list) # Debug statement to understand the program with much more depth.

bill_list = []

i = 0
for _ in range(list_size):
    module_num = multiplied_list[i] % 100
    if module_num != multiplied_list[i]:
        div_num = multiplied_list[i] // 100
        bill_list.append(div_num)
    else:
        if module_num >= 10 and module_num <= 90:
            module_num = multiplied_list[i] % 20
            div_num = multiplied_list[i] // 20
            if module_num == 10:
                bill_list.append(div_num)
                bill_list.append(1)
            else:
                bill_list.append(div_num)
        else:
            # if module_num <= 9:
            module_num = multiplied_list[i] % 5
            div_num = multiplied_list[i] // 5
            bill_list.append(div_num)
            if module_num > 0:
                bill_list.append(module_num)
    i += 1

print(sum(bill_list))

# * Good program I have wrote.
# * Tommorow write the learnings of it.
# * Thank you.

# * Favourite One.
