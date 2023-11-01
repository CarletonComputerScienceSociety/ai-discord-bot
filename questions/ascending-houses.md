# Ascending Houses

## Question
You want to visit your friends house, however their street does not have any addresses! Instead, the height of the houses are in sorted order, from the lowest house starting index `0` and the tallest house on the last index. 

Suppose you are given a list, `height[]`, of each house on the street, and your friend gives you the height of his house `h`. What is the index of where your friend lives, starting from the smallest house? 

Note: His house is guranteed to be in `height[]`

## Sample Inputs
Input 1
```python
height[] = [3, 5, 7, 9, 11, 12, 16, 23, 30]
h = 7

output = 2
```
Input 2
```python
height[] = [1, 5, 19, 31, 40]
h = 1

output = 0
```

## Sample solution using Binary Search
```python
def ascending_houses(height[]: int[], h: int):
    l,r = 0, len(height) - 1
	while l < r:
		mid = l + (r - l) // 2
		if h < height[mid]:
			r = mid - 1
		elif h > height[mid]:
			l = mid + 1
		else:
			return mid
```

