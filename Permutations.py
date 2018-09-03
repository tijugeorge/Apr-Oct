#Determine if a string is a permutation of another string.
from collections import defaultdict

class Permutations(object):
	def is_permutation(self, str1, str2):
		if str1 is None or str2 is None:
			return False
		return sorted(str1) == sorted(str2)
	
	def is_permutation1(self, str1, str2):
		if str1 is None or str2 is None:
			return False
		if len(str1) != len(str2):
			return False
		unique_counts1 = defaultdict(int)
		unique_counts2 = defaultdict(int)
		for char in str1:
			unique_counts1[char] += 1
		for char in str2:
			unique_counts2[char] += 1
		#print(unique_counts1, unique_counts2)
		return unique_counts1 == unique_counts2


ss = Permutations()
print(ss.is_permutation1('aat', 'ata'))
