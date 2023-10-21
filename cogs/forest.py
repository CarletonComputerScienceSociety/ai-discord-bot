import discord
from discord.ext import commands
from util.llmrequest import run


class ForestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def orca(self, ctx, *args):
        # Get the message from the user
        message = ' '.join(args)

        question = "What is a Python list?"
        facts = """
- 
Mutable: Python lists are mutable, which means you can change their content without changing their identity. You can modify a list by adding, removing, or changing elements.
Ordered: Python lists maintain a left-to-right sequential order of elements. The order in which you specify the elements when you define a list is an innate characteristic of that list and is maintained for that list’s lifetime.
Heterogeneous: A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are flexible to hold different types of elements.
Indexing: Each item in the list has an assigned index value starting from 0. Accessing elements in a list is called indexing.
Slicing: List slicing is a feature that enables accessing parts of sequences like strings, tuples, and lists. You can slice a list using the syntax list[start:stop].
Nested Lists: A list can contain any sort object, even another list (sublist), which in turn can contain sublists themselves, and so on. This is known as nested list.
Built-in Functions: Python includes the following list functions like len(list), max(list), min(list), list(seq), etc.
        """

        prompt = """
You are a bot that gives feedback on questions. You'll be given a question, and
a list of facts. You'll then be given an answer to the question from the
student.

You should respond to the student with feedback on their answer, based
on the list of facts from the question. Do not mention the list of facts.

Give your answer in bullet point format. Also compare student's answer and your
answer. 

Your answer should include references to the student's answer. To explain your answer, include a small Python code snippit in
markdown that provides an example. Also, don't use any complex terms, even if the facts state
them. Instead, be more clear and explain them a in more simple details.

Code snippits should look similar to this:

```python
# Here, we can see a list of values
a = [1, 2, 3]
```


---
Question: {question}
---
Facts: {facts}
---
Answer: {message}
---
Feedback:
        """.format(question=question, facts=facts, message=message)

        print(prompt)

        await ctx.send("Generating message...")

        result = run(prompt)
        result = result.replace('"', "'")
        await ctx.send(result)

def setup(bot):
    bot.add_cog(ForestCog(bot))
