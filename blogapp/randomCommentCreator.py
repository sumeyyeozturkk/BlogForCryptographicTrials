import random
import string 
from collections import Counter

def random_generator(size, chars=string.ascii_letters):
	return ''.join(random.choice(chars) for x in range(size))

def frequency_of_letters(random_generator):
	return Counter(random_generator)