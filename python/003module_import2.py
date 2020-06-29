print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

from os import listdir
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'listdir', 'os']

try :
    print(os.listdir()) # NameError: name 'os' is not defined
except :
    print('NameError: name \'os\' is not defined')
    print(listdir()) # ['.git', '.vscode', 'python']

import os

print(os.listdir()) # ['.git', '.vscode', 'python']

