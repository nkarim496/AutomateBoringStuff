# Global variables can be read from a local scope
roga = 7
def spam():
    print('spam()')
    print(roga)
spam()

def spam1(kopita):
    print('spam1()')
    print(roga)
    print(kopita)
spam1(17)
