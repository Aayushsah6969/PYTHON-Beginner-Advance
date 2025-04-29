set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)  # or set1 | set2
# Result: {1, 2, 3, 4, 5, 6}

# Intersection
intersection_set = set1.intersection(set2)  # or set1 & set2
# Result: {3, 4}

# Difference
difference_set = set1.difference(set2)  # or set1 - set2
# Result: {1, 2}

# Symmetric Difference
sym_diff = set1.symmetric_difference(set2)  # or set1 ^ set2
# Result: {1, 2, 5, 6}