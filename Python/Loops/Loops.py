<h1><img src=../../global_images/logo.png width="100" />🔁 Loops 🔁<img src=../../global_images/logo.png width="100" /></h1>

Often when we are coding, we find ourselves wanting to repeat very similar tasks over and over again.

Luckily, we have tools at our disposal to automate this kind of repetition for us - LOOPS! This is good, because one of the fundamental principles of good code is "DRY" - Don't Repeat Yourself.

A loop statement lets us define a block of code that will be executed multiple times. This process of doing something multiple times is called _**iterating**_, and each "turn" or repetition is called _**an iteration**_. 

There are two types of loop in Python: `for` loops, and `while` loops. Today we will look at them both.

<h2>Table of Contents</h2>

- [⏱️ `while` Loops ⏱️](#️-while-loops-️)
- [➿ `for` Loops ➿](#-for-loops-)
- [💡 Tips for Understanding Loops 💡](#-tips-for-understanding-loops-) 
  - [📈 Draw A Flowchart 📈](#-draw-a-flowchart-)
  - [✍️ Do It By Hand ✍️](#️-do-it-by-hand-️)
- [🧙 Loop Tricks 🧙](#-loop-tricks-)
  - [🎠 Harnessing The Power Of Infinite While 🎠](#-harnessing-the-power-of-infinite-while-)
  - [🏌️ The `range()` Function 🏌️](#️-the-range-function-️)
  - [🧵 Iterating Over A String 🧵](#-iterating-over-a-string-)
  - [🔂 The `enumerate()` Function 🔂](#-the-enumerate-function-)
  - [🪺 Nested Loops 🪺](#-nested-loops-)

---
---

## ⏱️ `while` Loops ⏱️
A while loop lets us execute some chunk of code repeatedly, for as long as some Boolean expression evaluates to `True`. 

This means that if there's some task we want to accomplish by repeatedly running the same block of code, we can define a `while` loop that keeps running for as long as the task is incomplete. Here's what that might look like:

```py
count = 0

while count <= 10:
    count = count + 1
    print(count)
```

![](./img/count_while.png)

> [!NOTE]  
> There are a few things worth noting here:
> - The Boolean expression we've used here is `count <= 10`, but *any* expression that evaluates to a Boolean is fine to use.
> - Just like with `if` statements and functions, we are using an indented codeblock to define our loop. In a loop statement, the indented code will be executed repeatedly until the loop ends.

> [!IMPORTANT]
> Note that we *do* print out `11` here! The last time this code runs, at the beginning of the loop `count` is equal to `10`. Then we add `1` to it, and *then* we print the result.
>
> Take a moment to think through how this goes down.

> [!CAUTION]
> If we ever want our `while` loop to end, we have to make sure that each repetition of the loop gets us closer to changing the value of the Boolean expression to `False`. If the `count` variable decreased with every loop, the code would run forever!

---
---

## ➿ `for` Loops ➿
A `for` loop lets us execute some operation on every element of an iterable. 

For example, let's say we have a list of numbers, and we want to square them all. Here's how we might do that:

```py
numlist = [1, 9001, -3, 0]

for each_number in numlist:
    print(each_number*each_number)
```

![](./img/for_squares.png)

To continue the train analogy that we used in the lists content, I like to think of the `for` loop as a robot that moves along the train, performing some work on each element of its cargo:

![](img/for_analogy.drawio.png)
> It's a friendly robot, not a menacing one.

> [!NOTE]  
> In our `for` loop statement, we nominate a variable name. In this case, we chose `each_number` for our loop variable. 
>
> As the `for` loop runs, each element in the list gets assigned as the value of the `each_number` variable. Then the code in the loop block gets run. 

> [!CAUTION]  
> If the code in your loop block modifies the iterable that the loop is running on, this can lead to weird bugs! Try running this code and see what happens:
> ```py
> extendo_list = [0, ]
> 
> for each_number in extendo_list:
>   print(each_number)
>   extendo_list.append(each_number + 1)
> ```
>
> (If you ever need to kill a Python program that looks like it will run forever, you can hit `Ctrl`+`C` on a Windows machine, or `Cmd`+`C` on a Mac.)

---
---

## 💡 Tips for Understanding Loops 💡
These are some handy ways to get your head around loops, either while you're learning the concept, or when you're troubleshooting a bug.

---

### 📈 Draw A Flowchart 📈
Here's what's happening in [our example loop while loop from above](#️-while-loops-️):

![](./img/while_flow.drawio.png)

---

### ✍️ Do It By Hand ✍️
It can be helpful to work through the code "by hand" to get the hang of how the loop works. Pretend you are the interpreter, grab a pen and paper, and do what the code says, line by line. 

Here's [the while loop from above](#️-while-loops-️), worked through by hand.

| Step # | `count` value | Action                                                                                                                              |
| ------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1      | N/A           | set `count` to `0`                                                                                                                  |
| 2      | `0`           | check if `count <= 10` -> `True` -> begin loop                                                                                      |
| 3      | `1`           | add `1` to `count`                                                                                                                  |
| 4      | `1`           | print `1` <br><br>(now we are at the end of the codeblock, so we go back the `while` statement to check if we should iterate again) |
| 5      | `1`           | check if `count <= 10` -> `True` -> continue loop                                                                                   |
| ...    | ...           | ...                                                                                                                                 |

Give it a go!

---
---

## 🧙 Loop Tricks 🧙
Some handy techniques that might help you out!

### 🎠 Harnessing The Power Of Infinite While 🎠
Sometimes a loop that runs forever can work in our favour. If we actually DO want our loop to run forever, we can easily set that up:

```py
while True:
    # Do stuff
```

Keep in mind that the opposite is true too: if our Boolean *never* evaluates to `True`, then the code in the block won't be executed at all.

```py
while False
    # Doesn't matter what I put here - it'll never get run... :(
```

---

### 🏌️ The `range()` Function 🏌️
Very often we want to iterate over a collection of numbers (say, the integers from `0` to `10`). We've already seen how do do that with a `while` loop, but that method involved a little bit of boring, "boilerplate" code. We had to set up the `count` variable, and include the code to increment its value by `1` in each loop. That's a lot of effort to just count to ten.

The `range()` function lets you automatically generate an iterable full of numbers with a single command.

- `range(10)` will give a range containing the numbers from `0` up to (but not including) `10`
- `range(3, 12)` will give a range containing the numbers from `3` up to (but not including) `12`
- `range(0, 20, 2)` will give a range containing every second number from `0` up to (but not including) `20`

> [!NOTE]  
> A `range` isn't a list. It is its own data type. Try printing each of the expressions in the above dot points. You'll notice that what you get back doesn't look like a list!
>
> ![](./img/range.png)
>
> That's because Python is lazy - until you actually do something with the elements in the `range` sequence, it won't create them. This is just something it does to save time and memory. If you want to actually see the numbers in the range, you'll need to convert it to a list first. Try running this instead:
>
> ```py
> # Create a range
> my_range = range(0, 20, 2)
> 
> # Convert the range to a list
> my_list = list(my_range)
> 
> # Print the list
> print(my_list)
> ```
> 
> ![](./img/rangelist.png)

The power of `range()` isn't just limited to maths. If we wanted to print the lyrics to Fatboy Slim's 1998 smash hit "The Rockafeller Skank", we could do it in just a few lines of code:

```py
for num in range(27):
    print("Check it out now;")
    print("The funk soul brother.")
    print("Right about now;")
    print("The funk soul brother.")
    print("...")
```
![](./img/rockerfella.png)

The printed lyrics continue offscreen for 27 verses. Truly, the voice of a generation.

> [!NOTE]  
> Notice that we don't need to convert the range to a list before we use it.
> 
> You can also see that we don't have to actually use the `num` variable in our code block. We **could** use it if we wanted to, but it's not compulsory. Here we are just exploiting the fact that the loop will iterate 27 times in order to print the right number of verses.

---
 
### 🧵 Iterating Over A String 🧵
Remember how at the end of the lists content, we mentioned that some of the tricks that work with lists also work with strings? Well this is another one. We can use a `for` loop to iterate over a string if we want to do something with each letter in turn:

```py
name = "LOLA"

print(name)

for letter in name:
    print(letter)

print(name)
```
![](./img/lola.png)

---

### 🔂 The `enumerate()` Function 🔂
Sometimes when we are dealing with an iterable like a list, we want to access each element in turn AND know what that element's index is.

The `enumerate()` function will take an iterable, and pair each item in that iterable up with its index. Check it out:

```py
alphabet = ["a", "b", "c", "d", "e"]

for index, letter in enumerate(alphabet):
    print(f"{letter} is at position {index} in the alphabet!")

![](./img/alphabet.png)

```

---

### 🪺 Nested Loops 🪺
The last brain-bender we'll give you for today is this: it's totally ok to put one loop inside another loop.

Here's what that might look like:

```py
iterations = ["first", "second", "third"]

print("Starting the outer loop!")

for outer_number in iterations: # outer loop
    print("Starting the inner loop!")

    for inner_number in iterations: # inner loop
        print(f"The outer loop is on its {outer_number} iteration, while the inner loop is on its {inner_number} iteration.")
    
    print("Inner loop complete!")

print("Outer loop complete!")
```

![](./img/times.png)

What's happening here? 

Remember, in any loop, Python executes the code inside its code block until it has satisfied the conditions we gave it. This means that here Python will run the code inside the outer loop three times. 

The code inside the outer loop is... the inner loop! So the inner loop's `print` statement will be run *nine* times - three times for each iteration of the outer loop. 

Once again, it might be helpful to work through this loop by hand to see how the values for `inner_number` and `outer_number` change.

> Of course, you can nest `while` loops too, and you can mix and match!
