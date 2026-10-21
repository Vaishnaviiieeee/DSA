# WAC TO PRINT MAKE FREQUENCY ZERO OF AN ARRAY
# n = 125367489
# freq = [0] * 10

# while n > 0:
#     digit = n % 10
#     freq[digit] += 1
#     n //= 10

# for i in range(10):
#     print(f"Frequency of {i}: {freq[i]}")

# WAC TO PRINT MAKE accurance of FREQUENCY ZERO OF AN ARRAY
# def Countfreq(n):
#     freq = [0] * 10

#     while n != 0:
#         last_digit = n % 10
#         freq[last_digit] += 1
#         n //= 10

#     n = 1335566879

#     rev

 

    # return freq


#  find two numbers are Anagram number
# def anagram(n1, n2):
#     freq1 = {}
#     freq2 = {}

#     while n1 > 0:
#         digit = n1 % 10
#         freq1[digit] = freq1.get(digit, 0) + 1
#         n1 = n1 // 10

#     while n2 > 0:
#         digit = n2 % 10
#         freq2[digit] = freq2.get(digit, 0) + 1
#         n2 = n2 // 10

#     if freq1 == freq2:
#         return True
#     else:
#         return False

# n1 = 1221
# n2 = 1212

# if anagram(n1, n2):
#     print("Anagram Numbers")
# else:
#     print("Not Anagram Numbers")

def get_max(*num):
    if len(num)== 0:
        return None
    max_num = num[0]
    for n in num:
        if n > max_num:
            max_num = n
    return max_num

print (get_max (3,12,32,9,21)) 
print (get_max ('Arush','Payal','Zalina','Yogesh'))       