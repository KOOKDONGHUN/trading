import os

print(os.getcwd()) # C:\Users\국동훈\study\Trading

print(os.listdir()) # ['.git', '.vscode', 'python'] 현재 경로에 존재하는 파일의 목록들을 출력한다.

print(os.listdir('C:/Users/국동훈/study')) # ['bokeh-notebooks', 'study', 'study_bokeh', 'subTest', 'Trading'] 
                                           # 해당하는 경로 하단의 목록을 출력 list의 형태로 반환됨

for i in os.listdir('C:/Anaconda3'):
    if i.endswith('exe'):
        print(i)
'''python.exe
pythonw.exe
Uninstall-Anaconda3.exe
venvlauncher.exe
venvwlauncher.exe
_conda.exe'''