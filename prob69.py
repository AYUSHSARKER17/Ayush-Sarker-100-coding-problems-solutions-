# Problem 69 - Merge Two Lists

list1 = input("Enter first list (space separated): ").split()
list1 = [int(x) for x in list1]
list2 = input("Enter second list (space separated): ").split()
list2 = [int(x) for x in list2]

merged = list1 + list2
print("Merged list:", merged)
