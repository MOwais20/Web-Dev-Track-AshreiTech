# Python Basics Quiz - Answers & Explanations

## Multiple Choice Questions (MCQs)

**1. Which of the following is a valid variable name in Python?**
- **Answer:** b) name_2
- **Explanation:** Variable names cannot start with a number, contain hyphens, or special characters like @. `name_2` is valid.

**2. What is the output of the following code?**
```python
a = 5
b = 2
print(a * b)
```
- **Answer:** b) 10
- **Explanation:** 5 multiplied by 2 is 10.

**3. Which data type is used to store a collection of items in order and is mutable (Changeable)?**
- **Answer:** b) list
- **Explanation:** Lists are ordered and mutable. Tuples are ordered but immutable.

**4. What will be the output of this code?**
```python
fruits = ["apple", "banana", "mango"]
print(fruits[1])
```
- **Answer:** b) banana
- **Explanation:** List indices start at 0, so index 1 is the second item: "banana".

**5. Which function is used to take input from the user in Python?**
- **Answer:** a) input()
- **Explanation:** The `input()` function reads a line from user input.

**6. What is the correct way to define a function in Python?**
- **Answer:** c) def greet():
- **Explanation:** Functions are defined using `def` followed by the function name and parentheses.

**7. What is the output of the following code?**
```python
student = {"name": "Ali", "age": 15}
print(student["age"])
```
- **Answer:** c) 15
- **Explanation:** The value for the key "age" is 15.

**8. Which of the following is an immutable (Unchangeable) data structure?**
- **Answer:** c) tuple
- **Explanation:** Tuples cannot be changed after creation. Lists, dictionaries, and sets are mutable.

**9. What will this code print?**
```python
for i in range(1, 4):
    print(i)
```
- **Answer:** a) 1 2 3
- **Explanation:** `range(1, 4)` generates 1, 2, 3 (end is exclusive).

**10. What is the output of this code?**
```python
x = 3
if x > 2:
    print("Yes")
else:
    print("No")
```
- **Answer:** a) Yes
- **Explanation:** 3 is greater than 2, so "Yes" is printed.

---

## Short Answer & Coding Questions

**11. Write a Python code to print all items in a list called `colors` using a for loop.**
```python
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
```
- **Explanation:** The for loop iterates through each item in the list and prints it.

**12. What is a dictionary in Python? Give an example.**
- **Answer:** A dictionary is a collection of key-value pairs.
- **Example:**
```python
student = {"name": "Ali", "age": 15, "city": "Karachi"}
```
- **Explanation:** Dictionaries use curly braces and store data as key-value pairs.

**13. Write a function named `greet` that takes a name as input and prints a greeting message.**
```python
def greet(name):
    print("Hello, " + name + "!")
```
- **Explanation:** The function takes a parameter and prints a greeting using string concatenation.

**14. Write a for loop that prints numbers from 1 to 5.**
```python
for i in range(1, 6):
    print(i)
```
- **Explanation:** `range(1, 6)` generates numbers 1 to 5 (6 is not included).

**15. What is the difference between a list and a tuple in Python?**
- **Answer:**
  - List: Ordered, mutable (can be changed), uses square brackets `[]`.
  - Tuple: Ordered, immutable (cannot be changed), uses parentheses `()`.
- **Explanation:** Lists can be modified after creation, tuples cannot.

**16. Write a Python code snippet to create a dictionary named `book` with keys `title`, `author`, `year`, and `keywords`, and assign appropriate values to each.**
```python
book = {
    "title": "Python Basics",
    "author": "John Doe",
    "year": 2025,
    "keywords": ["python", "programming", "basics"]
}
```
- **Explanation:** The dictionary contains string, integer, and list values.

**17. How do you write a comment in Python? Give an example.**
```python
# This is a comment
```
- **Explanation:** Comments start with `#` and are ignored by Python.

**18. Write the code for the following pseudo code, which prints numbers from 1 to 6 using a while loop:**
```python
count = 1
while count <= 6:
    print("Count:", count)
    count += 1
```
- **Explanation:** The while loop continues as long as `count` is less than or equal to 6, printing and incrementing each time.

---

Well done reviewing the answers and explanations!
