# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests        #导入requests包



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    url = 'http://www.cntour.cn/'
    strhtml = requests.get(url)  # Get方式获取网页数据
    print(strhtml.text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
