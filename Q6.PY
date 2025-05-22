#l="hello world" append the duplicate element[l,o]

D= "hello world"
duplicates = []
for char in D:
    if D.count(char) > 1 and char not in duplicates and char != " ":
        duplicates.append(char)
print(duplicates)