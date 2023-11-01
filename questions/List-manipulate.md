# RANDLIST

## Question

Welcome to **RANDLIST**! Here is the problem statement:

You must input a number to determine the length of a list that will contain random numbers from 1-100. The last element of the list should be removed 3 times and you must return the list to be displayed in highest value to lowest value order. 

## Input


```python
input_len = input("What is the list length: )
#EXAMPLE USER INPUT = 8

the_list = [4,23,13,2,1,6,56,82]
```

Therefore, your function should return:

```python
[1,2,4,13,23]
```

Here are some criteria for marking someone's code:

- Correctness: Does the code produce correct results for all test cases?
- Readability: Is the code easy to read and understand?
- Efficiency: Does the code run efficiently?
- Style: Does the code follow good coding style and conventions?

Here is a sample solution in Python:

```python
import random

input_len = input("What is the list length: )
the_list = []

for i in range(input_len)
    x = rand.randint(1,100)
    the_list.append(x)
    print("the list is" + the_list)  

def manipulate(the_list: list) -> list:
    for a in range (3):
        if len(the_list) ==0:
            break
        else:
            the_list.pop()
    
    the_list.sort(reverse = True)

    return the_list



```