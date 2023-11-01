# The P versus NP Problem

## Background Info

Imagine, for instance, that you have an unsorted list of numbers, and you want to write an algorithm to find the largest one. 
The algorithm has to look at all the numbers in the list: there’s no way around that. But if it simply keeps a record of the largest 
number it’s seen so far, it has to look at each entry only once. The algorithm’s execution time is thus directly proportional to the 
number of elements it’s handling — which computer scientists designate N. Of course, most algorithms are more complicated, and thus 
less efficient, than the one for finding the largest number in a list; but many common algorithms have execution times proportional 
to N2, or N times the logarithm of N, or the like.

A mathematical expression that involves N’s and N2s and N’s raised to other powers is called a polynomial, and that’s what the “P” in 
“P = NP” stands for. P is the set of problems whose solution times are proportional to polynomials involving N's.

Obviously, an algorithm whose execution time is proportional to N3 is slower than one whose execution time is proportional to N. But such 
differences dwindle to insignificance compared to another distinction, between polynomial expressions — where N is the number being raised 
to a power — and expressions where a number is raised to the Nth power, like, say, 2N.

If an algorithm whose execution time is proportional to N takes a second to perform a computation involving 100 elements, an algorithm whose 
execution time is proportional to N3 takes almost three hours. But an algorithm whose execution time is proportional to 2N takes 300 
quintillion years. And that discrepancy gets much, much worse the larger N grows.

NP (which stands for nondeterministic polynomial time) is the set of problems whose solutions can be verified in polynomial time. But as far as 
anyone can tell, many of those problems take exponential time to solve. Perhaps the most famous exponential-time problem in NP, for example, is 
finding prime factors of a large number. Verifying a solution just requires multiplication, but solving the problem seems to require systematically 
trying out lots of candidates.

## Question
Does P equal NP?
or
If the solution to a problem can be verified in polynomial time, can it be found in polynomial time?


