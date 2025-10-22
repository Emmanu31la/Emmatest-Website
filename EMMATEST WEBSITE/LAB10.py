print("Hello world")
a = 12
b =14
print(a+b)

#LAB 1:
#Creating sets

A = {1,2,3,4}
B = {3,4,5,6,7}

#PERFORMING A UNION
union_set = A|B
print("Union:", union_set)

#INTERSECTION
intersectin_set = A & B
print("Intersection:", intersectin_set)

#DIFFERENCE
difference_set = A - B
print("Difference:", difference_set)

#Performing symmetric difference
symmetric_difference_set = A^B
print("Symetric Difference:", symmetric_difference_set)

# Checking subset and superset
is_A_subset_of_B = A.issubset(B)
is_A_superset_of_B= A.issuperset(B)
print("Is A a subset of B?", is_A_subset_of_B)
print("Is A a superset of B?", is_A_superset_of_B)