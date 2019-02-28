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
			p = photos.get_first_horizontal_picture()
			print('REF:', p.index, p.type, p.tags)
			p2 = photos.get_picture_with_most_score(photo=p)
			print('REF:', p2.index, p2.type, p2.tags, p2.exclude_tags)
			if p2.type == 'V':
				p3 = photos.get_picture_vertical(p2.exclude_tags)
				print('REF:', p3.index, p3.type, p3.tags, p3.exclude_tags)