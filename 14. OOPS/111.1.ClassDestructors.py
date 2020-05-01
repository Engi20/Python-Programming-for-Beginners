import time

class Demo:
    def __init__(self):
        print('Constructor - Initialization: ',id(self))

    def display(self):
        for i in range(5):
            time.sleep(1)
            print(i)

    def __del__(self):
        print('Destructor - Clean up Process: ',id(self))

D = Demo()
D.display()

D1 = Demo()
D2 = Demo()
D3 = Demo()


