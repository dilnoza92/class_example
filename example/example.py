import unittest
import numpy as np
import matplotlib.pyplot as plt

arr1=np.arange(1,10,1)
arr2=np.arange(2,20,2)
def create_graph(array1,array2,name):
    plt.plot(array1,array2)
    output="{}.png".format(name)
    plt.savefig(output)
    return output
print create_graph(arr1,arr2,'yusuf')
