#!/usr/bin/env python3
# encoding: utf-8

import sys

def udvozol(nev):
	if nev == 'Batman' or nev == 'Robin':
		print('Denevérveszély!')
	else:
		print('Hello ' + nev + '!')

def main():
	name = sys.argv[1]
	if name == 'Batman':
		print('Denevérveszély!')
	else:
		udvozol(name)
	
		
if __name__ == '__main__':
	main()
	
	
