check = input("Enter a alphabet:")

if check.isalpha() and len(check) == 1:
    if check.lower() in ['a','e','i','o','u']:
        print("it is a vowel")
    else:
        print("it is a Consonant")
else:
      print("Please enter a single valid alphabet.")