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
			#	print('REF:', p3.index, p3.type, p3.tags, p3.exclude_tags)
			head = photos.get_first_horizontal_picture()
			s = ''
			head_removed = False
			i = 0
			while len(photos.photos):
				print(len(photos.photos))
				if not head_removed:
					photos.photos.remove(head)
					s += str(head.index) + '\n'
					i += 1
				p_max = photos.get_picture_with_most_score(photo=head)
				if not p_max:
					break
				head = p_max
				head_removed = False
				if head.type == 'V':
					photos.photos.remove(head)
					p_vert_swag = photos.get_picture_vertical(to_exclude=head.exclude_tags)
					if p_vert_swag:
						s += str(head.index) + ' '
						head = p_vert_swag
					else:
						head_removed = True
			s = str(i) + '\n' + s.strip()
			print(s)
			with open('result.txt', 'w') as f:
				f.write(s)