import os 
import sys

sys.path.append("..")
print(sys.path)
from ..shop.models import Product

print('hey')
print(os.getcwd())

print(sys.path)



new = Product()
print(new)