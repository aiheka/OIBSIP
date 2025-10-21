import random
import string
print("Random Password Generator")
lenght=int(input("Enter password lenght:"))
characters=string.ascii_letters+string.digits+string.punctuation
password= ' '.join(random.choice(characters) for i in range(lenght))
print("Generated password is :",password)