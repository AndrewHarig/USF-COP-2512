#takes first input input as a int named quarters
quarters = int(input())
#takes second input input as a int named dimes
dimes = int(input())
#takes third input input as a int named nickels
nickels = int(input())
#takes fourth input input as a int named pennies
pennies = int(input())

#dollars is set to the number of coins times there value all added together. It is set as a float because the answer need to keep it's decimals
dollars = float((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01))

#dollars is printed with 2 decimal places
print(f'Amount: ${dollars:.2f}')
