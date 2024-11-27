#1
# Create 5 lists with corresponding number of elements
list1 = [1]
list2 = [2, 3]
list3 = [4, 5, 6]
list4 = [7, 8, 9, 10]
list5 = [11, 12, 13, 14, 15]

# Print all elements using positive and negative indices
print("List1 (positive indices):", list1)
print("List1 (negative indices):", list1[::-1])

print("List2 (positive indices):", list2)
print("List2 (negative indices):", list2[::-1])

print("List3 (positive indices):", list3)
print("List3 (negative indices):", list3[::-1])

print("List4 (positive indices):", list4)
print("List4 (negative indices):", list4[::-1])

print("List5 (positive indices):", list5)
print("List5 (negative indices):", list5[::-1])

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_result = numbers[1] + numbers[-1]

diff_result = numbers[-2] - numbers[0]

product_result = numbers[4] * numbers[5]

print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", product_result)

#3
listn = ["good", "is", "programming"]

positive_sentence = listn[2] + " " + listn[1] + " " + listn[0]
print("Using positive indices:", positive_sentence)

negative_sentence = listn[-1] + " " + listn[-2] + " " + listn[-3]
print("Using negative indices:", negative_sentence)

#4

sample_list = [10, 20, 30, 40, 50]

print("Original list:", sample_list)

sample_list[2] = 35
sample_list[3] = 45

print("Updated list:", sample_list)


