import itertools
import re
import argparse
import random

def combinator(inputfile, outputfile, counts = None):
	with open(inputfile,'r') as file:
		text = file.read()
	pattern = re.compile(r'[\[\]]+')
	split1 = list(filter(None, pattern.split(text)))
	#print(split1)
	split2 = [_i.split('|') for _i in split1]
	#print(split2)
	all_vars = list(itertools.product(*split2))
	random.shuffle(all_vars)
	if not counts:
		pass
	else:
		all_vars = all_vars[0:counts]
	with open(outputfile,'w') as file:
		for _i in all_vars:
			# print(''.join(_i),'\n')
			file.write(''.join(_i)+'\n' +'_'*50+'\n')

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--inputfile", type=str,
						help="Input file")
	parser.add_argument("-o", "--outputfile", type=str,
						help="Outfut file")
	parser.add_argument("-c", "--count", type=int,
						help="Variants in output file")

	args = parser.parse_args()
	inputfile = args.inputfile
	outputfile = args.outputfile
	counts = args.count
	
	combinator(inputfile, outputfile, counts)
