# Magic Potion

## Question

Welcome to **Magic Potion**! Here is the problem statement:

Sabrina the witch has a list of magical ingredients that she uses to create potions. Each ingredient has a unique magical power level.

The list of ingredients is sorted in increasing order based on their magical power levels.

One day, Sabrina received an order for a magic potion. The order specified the exact magical power level required. Now, Sabrina needs to choose some ingredients from her list such that the sum of their magical power levels equals the required level.

Write a Python function


```python
function find_ingredients(ingredients: List[int], required_power: int)
```

that takes in two parameters:

`ingredients` (a list of integers) representing the magical power levels of the ingredients.

`required_power` (an integer) representing the required magical power level for the potion.

The function should return a list of ingredients (their power levels) that sum up to the required power. Only one solution is required in the case of multiple solutions. If there is no solution, return an empty list.

Note: You can use each ingredient only once.

Here is an example input:

```python
find_ingredients([1, 2, 3, 4, 5], 5)
```

The list of ingredients' power levels is `[1, 2, 3, 4, 5]` and the required power is `5`

Therefore, your function should return:

```python
[2, 3] or [1, 4]
```
as both combinations sum up to 5.

Here are some criteria for marking someone's code:

- Correctness: Does the code produce correct results for all test cases?
- Readability: Is the code easy to read and understand?
- Efficiency: Does the code run efficiently?
- Style: Does the code follow good coding style and conventions?

Here is a sample solution in Python:
```python
def find_ingredients(ingredients, required_power):
    ingredient_dict = {}

    for ingredient in ingredients:
        if required_power - ingredient in ingredient_dict:
            return [required_power - ingredient, ingredient]
        ingredient_dict[ingredient] = True

    return []
```
