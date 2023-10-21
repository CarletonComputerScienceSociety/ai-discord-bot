# Kart Kourse

## Question

Welcome to **Kart Kourse**! Here is the problem statement:

You are given a list of racers' names in the position they start the race in and a list of
position changes. Your task is to write a function that returns the new order of
the racers after applying the position changes.

## Input

toes

```python
racers = ["Mario", "Luigi", "Peach", "Yoshi", "Toad"]
position_changes = [2, 1, -1, 0, -2]
```

The first element in `position_changes` indicates that the racer in the second
position (Mario) advances two places. The second element indicates that the
racer in the third position (Peach) advances one place. The third element
indicates that the racer in the fourth position (Yoshi) moves down one place.
The fourth element indicates that the racer in the fifth position (Toad) stays
in place. The fifth element indicates that the racer in the first position
(Mario) moves down two places.

Therefore, your function should return:

```python
["Peach", "Mario", "Luigi", "Yoshi", "Toad"]
```

Here are some criteria for marking someone's code:

- Correctness: Does the code produce correct results for all test cases?
- Readability: Is the code easy to read and understand?
- Efficiency: Does the code run efficiently?
- Style: Does the code follow good coding style and conventions?

Here is a sample solution in Python:

```python
def apply_position_changes(racers, position_changes):
    new_racers = racers.copy()
    for i, change in enumerate(position_changes):
        new_index = i + change
        if new_index < 0:
            new_index = 0
        elif new_index >= len(new_racers):
            new_index = len(new_racers) - 1
        new_racers.remove(racers[i])
        new_racers.insert(new_index, racers[i])
    return new_racers
```

I hope this helps! Let me know if you have any further questions.

Source: Conversation with Bing, 2023-10-20 (1) tynker gallery | Tynker.
https://www.tynker.com/community/galleries/mario-kart/63580202218b2c53bb390b31/.
(2) Hour of Code: Mario's Secret Adventure. https://code.hatchxr.com/. (3) Data
Sets: Mario Kart - OpenIntro.
https://openintro.org/blog/article/data-set-mariokart/. (4) mario-kart · GitHub
Topics · GitHub. https://github.com/topics/mario-kart?l=python. (5) CS50 Week 6
- Mario in Python (More Comfortable) - DEV Community.
https://dev.to/attommy98/cs50-week-6-mario-in-python-more-comfortable-3b4b. (6)
rosepadilla546/mario.py — Python — NumWorks.
https://my.numworks.com/python/rosepadilla546/mario. (7) Mario KART - Microsoft
MakeCode. https://makecode.com/_TAjH3x2cr423. (8) 12 Mario Kart Quizzes,
Questions, Answers & Trivia - ProProfs.
https://www.proprofs.com/quiz-school/topic/mario-kart.