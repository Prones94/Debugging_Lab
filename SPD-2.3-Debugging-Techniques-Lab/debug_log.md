# Debug Log

**Explain how you used the the techniques covered (Trace Forward, Trace Backward, Divide & Conquer) to uncover the bugs in each exercise. Be specific!**

In your explanations, you may want to answer:

- What is the expected vs. actual output?
- If there is a stack trace, what useful information does it contain?
- Which technique did you use, on which line numbers?
- What assumptions did you have about each line of code, and which ones were proven to be wrong?

_Example: I noticed that the program should show pizza orders once a new order is made, and that it wasn't showing any. So, I used the trace forward technique starting on line 13. I discovered the bug on line 27 was caused by a typo of 'pzza' instead of 'pizza'._

_Then I noticed another bug ..._

## Exercise 1
When submitting the order for a new pizza, there was a typeerror for topping. Regardless of either choosing no toppings or all the toppings options there is the type error. Using trace backward, Using Trace Forward, I saw that the error occured on line 79, where pizza.toppings.apend(PizzaTopping(topping=topping_str)). I noticed in order.html that pizza_size should be saying size instead.

## Exercise 2

[[Your answer goes here!]]

## Exercise 3
Merge Sort:
What I expected from the output in the merge sort should be a sorted array, however after running it I realized that there was an index error at line 37. Knowing this, I decided to use a trace forward using the debugging console. On line 22, i had to assume that i and j were used as the left and right index pointers for the left and right sub arrays. After knowing that I was able to determine that line 24 and 27 were switched, as the left side was going to be smaller than the right side and that would continually make the index larger until the index was out of range.
Binary Search:
The expected output should be 4, where 5 is. However I received a TypeError: the list indices must be integers or slices, not floats. I can assume that somewhere in the code there is a float for an index. Therefore I used the Trace Forward method on this function. On line 49, we see the mid variable being created, however its not doing a floor division (//) operator, hence the floating number. Upon fixing that, I noticed that developer made a typo on line 52, when he said if the target element is equal to the mid. On line 47, we need to change the greater than sign to a greater than or equal symbol. On line 61, we need to change the return low to low = mid + 1.
