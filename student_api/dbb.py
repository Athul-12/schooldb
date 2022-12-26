class operation:
    def add(self,input1,input2):
        if type(input1)== str and type(input2)== str:
            result = input1 + input2
            print('result after concatination is',result)
        elif type(input1)==int and type(input2)==int:
            result = input1 + input2
            print('result after addition is', result)

        else:
            print('invalid input')
class A:
    def display(self):
        print('from class A')

class B(A):
    def display(self):
        print('from class B')

obj = operation()
obj.add('athul','krishna')