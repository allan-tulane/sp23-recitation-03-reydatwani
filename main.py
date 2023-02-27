"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
    ### TODO
    xvec = BinaryNumber(x).binary_vec
    yvec = BinaryNumber(y).binary_vec

    t = pad(xvec, yvec)
    xvec = t[0]
    yvec = t[1]

    l1 = ["1"]
    l0 = ["0"]
    t = pad(l1, xvec)
    l1 = t[0]
    t = pad(l0, yvec)
    l0 = t[0]
    l2 = [l1, l0]
  
    if (xvec in l2 and yvec in l2):
      return xvec * yvec
    else:
      x_left = xvec[0:len(xvec)//2]
      x_right = xvec[len(xvec)//2:]
      y_left = yvec[0:len(yvec)//2]
      y_right = yvec[len(yvec)//2:]

      n = len(xvec)
      two = BinaryNumber(2)
      
      p1 = quadratic_multiply(bit_shift(two,n),quadratic_multiply(x_left, y_left))
      p2 = quadratic_multiply(bit_shift(two,n//2),quadratic_multiply(x_left, y_right) + quadratic_multiply(x_right,y_left))
      p3 = quadratic_multiply(x_right, y_right)
      return p1 + p2 + p3
    ###



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000


    
    

