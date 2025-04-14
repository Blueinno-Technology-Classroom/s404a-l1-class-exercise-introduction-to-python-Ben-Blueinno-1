# print('''    =/\                 /\=
#     / \\'._   (\_/)   _.'/ \\
#    / .''._'--(o.o)--'_.''. \\
#   /.' _/ |`'=/ " \='`| \_ `.\\
#  /` .' `\;-,'\___/',-;/` '. '\\
# /.-'       `\(-V-)/`       `-.\\
# `            "   "            `''')

age = input('How old are you? ')

age = int(age)

print(f'You are {age} years old')

if age < 18:
    print('You are a teen')
elif age < 65:
    print('You are an adult')
else:
    print('You are an elderly')
