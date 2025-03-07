s = "Set operations in Python"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
c = sum(s.count(v) for v in set(s) & vowels)

print("Number of vowels:", c)