"""Project name :  Advanced Loop Training
    File name : main.py
    Programmer : Colin B. Chin Choy
"""

col = ""
row = ""


def drawBoard():
    chk = False
    xval = False
    yval = False
    while chk == False:
        x = input("Please enter the quantity of columns:- ")
        y = input("Please enter the quantity of rows:- ")
        try:
            col = int(x)
            xval = True
        except ValueError:
            print("Incorrect value entered.")
        except Exception as e:
            print("The error is ",str(e))
        finally:
            print("This is past it.....")
        try:
            row = int(y)
            yval = True
        except ValueError:
            print("Incorrect value entered.")
        except Exception as e:
            print("The error is ",e)
        finally:
            print("This is past it.....")
        if xval ==True and yval ==True:
            chk = True
    ro1 = (row*2)-1

    for i in range(0,ro1):
        if (int(i) % 2 == 0):
            print((" ")+(" "+" "+" "+"|")*(col-1))
        else:
            print(" "+("-"*((col*3)+(col-1))))

drawBoard()
print("True")
