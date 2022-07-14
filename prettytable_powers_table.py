from prettytable import PrettyTable
x = PrettyTable()

def sq(a):
    return a * a

def q(a):
    return a ** 3


while True:
    i = input('What number would you like to go up to? ')
    if i.isdigit():
        i = int(i)
        break
    elif i.lstrip('-').isdigit():
        print(f'Is {i} a negative number...? smh')
        continue
    print('Try using the number keys... smh')

# print('\n', 'Here is your table!', '\n' * 2, 'number | squared | cubed', '\n', '------ | ------- | -----')
x.title = 'Here is your table!'
x.field_names = ['number', 'squared', 'cubed']
# print(x)
counter = 0
next_time = i
while True:
    for n in range(counter + 1, i + 1):
        x.add_row([n, sq(n), q(n)])
#         print(f' {n}      |{sq(n)}       |{q(n)}')
    print(x)
    C = input('Continue...? (Y/N) ')   
    if C.upper() == 'Y':
        counter = i
        i = i + next_time
    else: break    
