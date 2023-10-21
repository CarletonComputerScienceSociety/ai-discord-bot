# Zelda's Quest

## Question

Welcome to **Zelda's Quest**! Here is the problem statement:

You are on a quest to save the kingdom of Hyrule from the evil Ganon. You have
been tasked with collecting the three pieces of the Triforce, which will give
you the power to defeat Ganon and restore peace to the land. You have already
collected two pieces of the Triforce, but you need to find the third piece.

You have received a clue that says: "The third piece of the Triforce is hidden
in a secret location. To find the third piece, you must defeat the final boss. To
defeat the final boss, you must complete a puzzle. The puzzle involves a
list of numbers that are related to the Triforce."

You have been given a list of integers. Your task is to write a function that
returns the sum of all the even numbers in the list.

Here is an example input:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The even numbers in this list are `2`, `4`, `6`, and `8`. Therefore, your
function should return:

```python
20
```

Here are some criteria for marking someone's code:

- Correctness: Does the code produce correct results for all test cases?
- Readability: Is the code easy to read and understand?
- Efficiency: Does the code run efficiently?
- Style: Does the code follow good coding style and conventions?

Here is a sample solution in Python:

```python
def sum_even_numbers(numbers):
    return sum([number for number in numbers if number % 2 == 0])
```
