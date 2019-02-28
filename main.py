#!/usr/bin/python3

import sys

def print_credits():
	print("This project has been made by a koala and an epitech student.")

if __name__ == "__main__":
	if len(sys.argv) == 2 and sys.argv[1] == "credits":
		print_credits()