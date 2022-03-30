from pkg_resources import invalid_marker


invalid_values = [
    {'title': '', 
    'description': 'Your variable names should always be descriptive to provide a minimum context: a variable name should tell you in words what the variable stands for.', 
    'additional_content': ''
    },

    {'title': '      ', 
    'description': 'Your variable names should always be descriptive to provide a minimum context: a variable name should tell you in words what the variable stands for.', 
    'additional_content': ''
    },

    {'title': 'Non-explicit variable names', 
    'description': '', 
    'additional_content': ''
    }
]
valid_values = [ {
    'title': 'Non-explicit variable names', 
    'description': '''Your variable names should always be descriptive to provide a minimum context: a variable name should tell you in words what the variable stands for.
        This makes the code easier to understand for other developers and easier to debug for you.''',
    'additional_content': ''' 
        # bad practices

        df = pd.read_csv("./customer_reviews.csv")
        x = df.groupby("country").agg({"satisfaction_score": "mean"})
        
        x = data[["f1", "f2", "f3"]]
        y = data["target"]

        # good practice

        customer_data = pd.read_csv("./customer_reviews.csv")
        average_satisfaction_per_country = customer_data.groupby("country").agg({"satisfaction_score": "mean"})

        # good practice

        features = data[["f1", "f2", "f3"]]
        target = data["target"]'''},
    {
    'title': 'Not iterating directly over the elements of an iterator',
    'description': ''' This is a quite common anti-pattern. You don’t necessarily need to iterate over the indices of the elements in an iterator if you don’t need them. You can iterate directly over the elements.
        This makes your code more pythonic.''',
    'additional_content': ''' 
        list_of_fruits = ["apple", "pear", "orange"]

        # bad practice

        for i in range(len(list_of_fruits)):
            fruit = list_of_fruits[i]
            process_fruit(fruit)
                
        # good practice

        for fruit in list_of_fruits:
            process_fruit(fruit)'''
    },
    {
    'title': 'else clause on loop without a break statement',
    'description': '''The else clause of a loop is executed when the loop sequence is empty. When a loop specifies no break statement, the else clause will always execute, because the loop sequence will eventually always become empty. Sometimes this is the intended behavior, in which case you can ignore this error. 
        But most times this is not the intended behavior, and you should therefore review the code in question. ''',
    'additional_content': '''The code below demonstrates some potential unintended behavior that can result when a loop contains an else statement yet never specifies a break statement. contains_magic_number() iterates through a list of numbers and compares each number to the magic number. If the magic number is found then the function prints The list contains the magic number. If it doesn’t then the function prints This list does NOT contain the magic number. When the code calls the function with a list of range(10) and a magic number of 5, you would expect the code to only print The list contains the magic number. However, the code also prints This list does NOT contain the magic number.
    This is because the range(10) list eventually becomes empty, which prompts Python to execute the else clause.

        def contains_magic_number(list, magic_number):
            for i in list:
                if i == magic_number:
                    print("This list contains the magic number")
            else:
                print("This list does NOT contain the magic number")

        contains_magic_number(range(10), 5)
        # This list contains the magic number.
        # This list does NOT contain the magic number.
        Best practices
        Insert a break statement into the loop
        If the else clause should not always execute at the end of a loop clause, then the code should add a break statement within the loop block.

        def contains_magic_number(list, magic_number):
            for i in list:
                if i == magic_number:
                    print("This list contains the magic number.")
                    # added break statement here
                    break
            else:
                print("This list does NOT contain the magic number.")

        contains_magic_number(range(10), 5)
        # This list contains the magic number.'''

    }
]
invalids_id = [ 
    ' ', 'invalid-id', 'invalid parameter id', '@@@@@!@32jfasdf90', 'fadfasd0fdsfds-dsfsdafsde3488'
]
