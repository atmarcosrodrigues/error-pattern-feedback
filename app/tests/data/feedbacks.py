
invalid_values = [
    {'title': '', 
    'message': 'Your variable names should always be descriptive to provide a minimum context: a variable name should tell you in words what the variable stands for.',     
    },

    {'title': '      ', 
    'message': 'Your variable names should always be descriptive to provide a minimum context: a variable name should tell you in words what the variable stands for.', 
    },

    {'title': 'Attention to variable names', 
    'message': ''' ''',
    }
]

valid_values = [
    {'title': 'Feedback Instructional', 
    'message': ''' Create separate functions to organize the code. Use better names for variables. ''', 
    },
    {
    'title': 'How to access values from dict?',
    'message': ''' 
    # get vs [] for retrieving elements
    my_dict = {'name': 'Jack', 'age': 26}

    # Output: Jack
    print(my_dict['name'])

    # Output: 26
    print(my_dict.get('age'))

    # Trying to access keys which doesn't exist throws error
    # Output None
    print(my_dict.get('address'))

    # KeyError
    print(my_dict['address'])'''
    },
    {'title': 'Attention before concatenate String and int', 
    'message': '''
In Python Python, if you try to concatenate string and int using + operator, you will get a runtime error.
    text = 'Year is '
    year = 2018
    print(text + year)

    Output:
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str

The easiest way is to convert int to a string using str() function.
    print(s + str(y))

Using % Operator
    print("%s%s" % (s, y))

Using format() function
We can use string format() function too for concatenation of string and int.
    print("{}{}".format(s, y))

Using f-strings
    print(f'{s}{y}')
'''

    },

    {'title': 'List comprehensions', 
    'message': '''You can loop through the elements in a list in a single line in a very comprehensive way.
Let’s see that in action in the following example: numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8]''', 
    }, 

    {'title': 'String Formatting (str.format)',
    'message': '''Python 3 introduced a new way to do string formatting that was also later back-ported to Python 2.7. This “new style” string formatting gets rid of the %-operator special syntax and makes the syntax for string formatting more regular. Formatting is now handled by calling .format() on a string object.
You can use format() to do simple positional formatting, just like you could with “old style” formatting:
>>> name="Peter"
>>> 'Hello, {}'.format(name)
'Hello, Peter'
>>> 'User: {name}, age: {age} years old.'.format(name="Mary", age=25)
'User: Mary, age: 25 years old.'
'''
    }
]