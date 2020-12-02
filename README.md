# Learning Python

## Description
In this repo I explored a new language, namely Python. I was already familiar with it, however it had been a very long time since I've used Python.

## Resources
I used this [OpenSource.com](https://opensource.com/article/19/5/python-3-default-mac#what-to-do) to help learn how to install Python using homebrew.

To learn the new syntax I visited the trusty [w3schools.com](https://www.w3schools.com/python/python_reference.asp) and used a physical textbook I had on my shelf, "Hello World! Computer Programming for Kids and Other Beginners" by Warren and Carter Sande.

## Notes of Interest

### Object Attributes
Objects in Python are crazy to me. You do not need to define every attribute in the class definition, they can just be added later.

    class Ball:
        def getBallProps(self):
            print(self.__dict__)

    myBall = Ball()
    myBall.color = 'red'

### List Mutation
I can't say I'm a huge fan of the fact that list mutation is the default and find the built-in list methods to be unhelpful.

`reversedTestArr = testArr.copy().reverse()`

To me, `print(reversedTestArr)` should print the array reversed, not 'none'.