# introduction...
print('\nWelcome to the Maximum Revenue Finder by Patrick Cash')
print('This was developed to solve a tricky bonus economics question\n')

# declare some variables...
factors = {}
values = []
intercept = float(input('Please insert the intercept: '))
price_coefficient = float(input('Please provide the price coefficient: '))

# add the intercept to the values list...
values.append(intercept)

# add on as many factors as needed...
while True:
    a = input('Please enter another coefficient, if none type "none": ')
    if a == 'none':
        break
    b = input('Please enter the value for this coefficient: ')

    factors[float(a)] = float(b)

# solve for all factors except price...
for k, v in factors.items():
    factor = k * v
    values.append(float(factor))

# add all factors together...
total = sum(values)

# rearrange the equation...
if total < 0:
    new_total = abs(total)
else:
    new_total = total * -1

# divide by price coefficient to isolate the P variable...
vertical_intercept = new_total / price_coefficient
horizontal_intercept = total

# print the intercepts...
print('\nVertical Intercept: ' + str(vertical_intercept))
print('Horizontal Intercept: ' + str(horizontal_intercept) + '\n')

# find price that will provide max revenue...
price = .00001
total_rev = 0
last_rev = 0

while True:
    price_variable = price * price_coefficient
    quantity_demanded = total + price_variable
    total_rev = price * quantity_demanded
    if total_rev < last_rev:
        best_price = price - .00001
        break
    else:
        last_rev = total_rev
        price += .00001

print('Best Price: ' + str(best_price) + '\n')
