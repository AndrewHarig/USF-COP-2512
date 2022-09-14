#this is an overly complex solution because at the time I did not know the split function could be used on inputs

#takes the first input and creates a string
string1 = input()
#splits that string into a list
list1 = list(string1.split())
#makes the list values into floats
num_list1 = list(map(float, list1))

#makes carpet cost the first number in the input
carpet_cost1 = float(num_list1[0])
#makes length the second number in the input
length1 = int(num_list1[1])
#makes width the second number in the input
width1 = int(num_list1[2])

#area of carpet is equal to lenght times width
carpet1 = length1 * width1

#cost for the room is equal to the carpet cost times the area. There is also a 20% overhead
room_cost1 = carpet_cost1 * carpet1 * 1.2
#labor cost 75 cents per sqr foot
labor_cost1 = carpet1 * 0.75
#tax is 7% and is put on labor and the room cost
tax1 = (labor_cost1 + room_cost1)*0.07
#the total is equal to the rooms cost plus labor plus tax
total_cost1 = room_cost1 + labor_cost1 + tax1

#prints all the info need .2f means it goes out to 2 decimal places
print('Order #1')
print(f'Room: {carpet1} sq ft')
print(f'Carpet: ${room_cost1:.2f}')
print(f'Labor: ${labor_cost1:.2f}')
print(f'Tax: ${tax1:.2f}')
print(f'Cost: ${total_cost1:.2f}')

#all previous steps are repeated for the second set of inputs
string2 = input()
list2 = list(string2.split())
num_list2 = list(map(float, list2))

carpet_cost2 = float(num_list2[0])
length2 = int(num_list2[1])
width2 = int(num_list2[2])

carpet2 = length2 * width2

room_cost2 = carpet_cost2 * carpet2 * 1.2
labor_cost2 = carpet2 * 0.75
tax2 = (labor_cost2 + room_cost2)*0.07
total_cost2 = room_cost2 + labor_cost2 + tax2

print(f'\nOrder #2')
print(f'Room: {carpet2} sq ft')
print(f'Carpet: ${room_cost2:.2f}')
print(f'Labor: ${labor_cost2:.2f}')
print(f'Tax: ${tax2:.2f}')
print(f'Cost: ${total_cost2:.2f}')

#all previous steps are repeated for the third set of inputs
string3 = input()
list3 = list(string3.split())
num_list3 = list(map(float, list3))

carpet_cost3 = float(num_list3[0])
length3 = int(num_list3[1])
width3 = int(num_list3[2])

carpet3 = length3 * width3

room_cost3 = carpet_cost3 * carpet3 * 1.2
labor_cost3 = carpet3 * 0.75
tax3 = (labor_cost3 + room_cost3)*0.07
total_cost3 = room_cost3 + labor_cost3 + tax3

print(f'\nOrder #3')
print(f'Room: {carpet3} sq ft')
print(f'Carpet: ${room_cost3:.2f}')
print(f'Labor: ${labor_cost3:.2f}')
print(f'Tax: ${tax3:.2f}')
print(f'Cost: ${total_cost3:.2f}')

#the total cost of everything is all 3 totals added together. All values are floats so total_cost will be a float
total_cost = total_cost1 + total_cost2 + total_cost3

#prints the total sales to 2 decimal places
print(f'\nTotal Sales: ${total_cost:.2f}')
