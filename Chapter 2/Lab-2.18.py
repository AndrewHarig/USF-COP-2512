#rounding will be require so math needs to be imported
import math

#splits the input into multiple variables
people1, slices1, pizza_cost1 = input().split()

#assigning the variables to proper type
people1 = int(people1)
slices1 = float(slices1)
pizza_cost1 = float(pizza_cost1)

#takes the number f people multiplies them by the slices per person then divides by 8, the number of slices per pie
#this is then rounded up as we can only order whole pizza and are ok with leftovers
num_pies1 = int(math.ceil((people1 * slices1)/8))
#the cost of all the pizzas is the cost per pizza time the number of pizzas
pies_cost1 = num_pies1 * pizza_cost1
#tax is 7%
tax1 = pies_cost1 * 0.07
#delivery is 20% on top of the price and tax
delivery1 = (pies_cost1 + tax1) * 0.2
#the total is the cost of pizzas, tax and deliver all added together
total1 = pies_cost1 + tax1 + delivery1

#prints answers as required
print("Friday Night Party")
print(f"{num_pies1} Pizzas: ${pies_cost1:.2f}")
print(f"Tax: ${tax1:.2f}")
print(f"Delivery: ${delivery1:.2f}")
print(f"Total: ${total1:.2f}")

#repeat steps from first pizza party
people2, slices2, pizza_cost2 = input().split()

people2 = int(people2)
slices2 = float(slices2)
pizza_cost2 = float(pizza_cost2)

num_pies2 = int(math.ceil((people2 * slices2)/8))
pies_cost2 = num_pies2 * pizza_cost2
tax2 = pies_cost2 * 0.07
delivery2 = (pies_cost2 + tax2) * 0.2
total2 = pies_cost2 + tax2 + delivery2

print("\nSaturday Night Party")
print(f"{num_pies2} Pizzas: ${pies_cost2:.2f}")
print(f"Tax: ${tax2:.2f}")
print(f"Delivery: ${delivery2:.2f}")
print(f"Total: ${total2:.2f}")

#repeat steps from first or second pizza party
people3, slices3, pizza_cost3 = input().split()

people3 = int(people3)
slices3 = float(slices3)
pizza_cost3 = float(pizza_cost3)

num_pies3 = int(math.ceil((people3 * slices3)/8))
pies_cost3 = num_pies3 * pizza_cost3
tax3 = pies_cost3 * 0.07
delivery3 = (pies_cost3 + tax3) * 0.2
total3 = pies_cost3 + tax3 + delivery3

print("\nSunday Night Party")
print(f"{num_pies3} Pizzas: ${pies_cost3:.2f}")
print(f"Tax: ${tax3:.2f}")
print(f"Delivery: ${delivery3:.2f}")
print(f"Total: ${total3:.2f}")

#the total for the weekend is the total from all the nights combined
weekend_total = total1 + total2 + total3

print(f"\nWeekend Total: ${weekend_total:.2f}")

