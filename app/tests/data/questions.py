
invalid_values = [
    {'title': '', 
    'description': 'Your variable names should always be descriptive to provide a minimum context: a variable name should tell you in words what the variable stands for.', 
    'content': ''
    },

    {'title': '      ', 
    'description': 'Your variable names should always be descriptive to provide a minimum context: a variable name should tell you in words what the variable stands for.', 
    'content': ''
    },

    {'title': 'Fibonacci', 
    'description': ''' ''', 
    'content': '''Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
    (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''
    }
]

valid_values = [
    {'title': 'List Remove Duplicates', 
    'description': ''' Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.''', 
    'content': 'Write two different functions to do this - one using a loop and constructing a list, and another using sets.'
    },

    {'title': 'Divisors', 
    'description': ''' Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)''', 
    'content': ''' The topics that you need for this exercise combine lists, conditionals, and user input. There is a new concept of creating lists.

        There is an easy way to progra mmatically create lists of numbers in Python.
        To create a list of numbers from 2 to 10, just use the following code:
        
            x = range(2, 11)
        Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10]. Note that the second number in the range() function is not included in the original list.

        Now that x is a list of numbers, the same for loop can be used with the list:

            for elem in x: 
                print elem'''
    },

    {'title': 'Fibonacci', 
    'description': '''Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
    ''', 
    'content': '''Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.
    (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''
    }
]