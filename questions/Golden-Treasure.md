# The Golden Treasure

## Question

Welcome to **The Golden Treasure**

You are stranded on an island with one other person. To get back to land, you have to dig up a treasure. The only problem? The treasure is behind a very secure lock. The only way to break the lock is to ask The Second Monster to open it. The Second Monster demands you to solve a problem he has. Including 0, sum up all the elements at the indexes which divide evenly into 2 

## Input

Given a sample input list like this 
```python
numbers = [5,18,2,35,19,20,9]
```
Turn it into an output like 
```python
    sum = 5+2+19+9 
    sum = 35
```
You take the elements starting from 0 and then take every 2nd element after that. So it'd be 5+2+19+9

## Sample Solution
```python
list1 = [32,55,1,23,55,46,78]
sum = 0
for i in range(len(list1)):
    if i % 2 == 0:
        sum+=list1[i]
print(sum)
```
