"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    W = eval(input("Enter rectangle width: "))
    L = eval(input("Enter rectangle length: "))
    area = W * L
    print(area)


def calc_volume():
    H = eval(input("Enter rectangle height: "))
    W = eval(input("Enter rectangle width: "))
    L = eval(input("Enter rectangle length: "))
    V = W * L * H
    print(V)



def shooting_percentage():
    Total_shots = eval(input('Enter how many shots the player took: '))
    Made = eval(input('Enter how many shots the player made: '))
    percentage = (Made / Total_shots) * 100
    print('The player made', percentage, '% of their shots.')


def coffee():
    pass


def kilometers_to_miles():
    pass


if __name__ == '__main__':
    pass
