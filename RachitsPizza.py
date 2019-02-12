toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']

prices = [2,6,1,3,2,7,2]

num_pizzas = len(toppings)

print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

pizzas = list(zip(prices,toppings))
pizzas.sort()

cheapest_pizza = pizzas[0]
print(cheapest_pizza)

most_expensive_pizza = pizzas[-1]
print(most_expensive_pizza)

two_dollar_slices = prices.count(2)
print(two_dollar_slices)
