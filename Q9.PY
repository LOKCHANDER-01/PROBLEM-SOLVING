#myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")
#get the palindromes

myStrings = ("demigod", "rewire", "madam", "fortran", "python", "xamarin", "salas", "PHP")
palindromes = tuple(word
                    for word 
                    in myStrings 
                    if word.lower() == word.lower()[::-1])
print(palindromes)