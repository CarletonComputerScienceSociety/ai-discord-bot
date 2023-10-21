# Smallest Sum

## Question

Here is the problem statement:

Given a list of integers, you will need to find sum that can be created for a given list. For example, if the list was [1,6,9,4,3], the smallest sum of the list would be 4(3+1). Below is a way that you could go about finding smallest sum in an array:

    
    for(i in range(0,array.length)){
        for(j in range(0,array.length)){
            if((array[i]+array[j])<minSum){
                minSums = (array[i]+array[j])
            }
        }

    }

Create a solution to solving this problem efficiently.