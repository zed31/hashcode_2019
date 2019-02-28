#!/usr/bin/python3

import sys
import data_model

def print_credits():
	print("This project has been made by a koala and an epitech student.")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		if sys.argv[1] == "credits":
			print_credits()
		else:
			photos = data_model.PhotoListModel(data_model.Parser(sys.argv[1]).get_photos())
			print(photos.photos)