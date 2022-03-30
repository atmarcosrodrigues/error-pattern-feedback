from pkg_resources import invalid_marker


invalid_values = [
    {'title': '', 
    'answer': 'content'
    },

    {'title': '      ', 
    'answer': 'content'
    },
]
valid_values = [

    {'title': 'Remove Duplicates', 
    'answer': '''
# this one uses a for loop
def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))
    '''
    },
    {'title': 'Response Divisors', 
    'answer': '''
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
    '''
    },
    {
    'title': 'Fibonacci',
    'answer': '''def get_fibo(num):
    if num == 0:
        fibo_list = []
    if num == 1:
        fibo_list = [1]
    if num >= 2:
        fibo_list = [1,1]
    for i in range(num-2):
        fibo_list.append(fibo_list[i]+fibo_list[i+1])
    return fibo_list
print(get_fibo(int(input("How many Fibonacci numbers do you want? "))))''',
    }
]
