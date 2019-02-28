#!/usr/bin/python3

from collections import Counter
    
class PhotoModel:
    def __init__(self, idx, typeOfPhoto, tags):
        self.type = typeOfPhoto
        self.tags = tags
        self.index = idx
        self.exclude_tags = []

    def get_tag_model(self):
        return self.tags

    def get_number_of_common_tags(self, tags: list) -> list:
        return [{'tagName': x, 'occurrences': tags.count(x)} for x in self.tags]

    def _get_score_for_common_tags(self, tags):
        score = 0
        for element in tags:
            score += element['occurrences']
        return score
    
    def _get_score_for_excluded_tags(self, tags):
        score = 0
        for element in tags:
            if element['occurrences'] == 0:
                score += 1
        return score
    
    def get_common_tags(self, tags):
        tags_and_occurrences = self.get_number_of_common_tags(tags)
        l = []
        for tag in tags_and_occurrences:
            if tag['occurrences'] >= 1:
                l.append(tag['tagName'])
        return l
    
    def get_exclude_tags(self, tags):
        tags_and_occurrences = self.get_number_of_common_tags(tags)
        l = []
        for tag in tags_and_occurrences:
            if tag['occurrences'] == 0:
                l.append(tag['tagName'])
        return l

    def get_score(self, photo) -> int:
        common_tags = self._get_score_for_common_tags(self.get_number_of_common_tags(photo.get_tag_model()))
        exclude_tags = self._get_score_for_excluded_tags(self.get_number_of_common_tags(photo.get_tag_model()))
        exclude_tags_photo = photo._get_score_for_excluded_tags(photo.get_number_of_common_tags(self.tags))
        return (min(common_tags, exclude_tags, exclude_tags_photo), self.get_common_tags(photo.get_tag_model()), self.get_exclude_tags(photo.get_tag_model()))

class PhotoListModel:
    def __init__(self, photos):
        self.photos = photos
        self.exclude_tags = []
    
    def dump_list(self):
        for element in self.photos:
            print(element.index, element.type, element.tags)
    
    def _get_first_picture_of(self, t):
        idx = -1
        i = 0
        for element in self.photos:
            if element.type == t:
                idx = i
                pic = element
                break
            idx += 1
        return pic

    def get_first_horizontal_picture(self):
        return self._get_first_picture_of('H')

    def get_first_vertical_picture(self):
        return self._get_first_picture_of('V')

    def get_picture_with_most_score(self, photo):
        idx = -1
        current_score = 0
        i = 0
        for element in self.photos:
            score = photo.get_score(element)
            if score[0] >= current_score:
                idx = i
                current_score = score[0]
                if element.type == 'V':
                    element.exclude_tags = score[2]
            i += 1
        if idx > -1:
            pic = self.photos[idx]
        return None if idx == -1 else pic
    
    def get_picture_vertical(self, to_exclude):
        idx = -1
        i = 0
        for element in self.photos:
            if element.type == 'V':
                has_tag = False
                for tag in to_exclude:
                    if element.tags.count(tag) > 0:
                        has_tag = True
                if not has_tag:
                    idx = i
                    break
            i += 1
        if idx > -1:
            pic = self.photos[idx]
        return None if idx == -1 else pic

class SlideModel:
    def __init__(self, photos):
        self.photos = photos
    
    def get_photo(self):
        return self.photos

class Parser:
    def __init__(self, fileName: str):
        with open(fileName, 'r') as fd:
            fileContent = [x for x in fd]
            i = 0
            self.photos = []
            for element in fileContent[1:]:
                e = element.replace('\n', '').split(' ')
                idx = i
                typeOfPhoto = e[0]
                nbOfTags = int(e[1])
                tags = e[2:]
                self.photos.append(PhotoModel(idx=idx, typeOfPhoto=typeOfPhoto, tags=tags))
                i += 1
    
    def get_photos(self) -> list:
        return self.photos
    

"""parser = Parser('a_example.txt')
photos = PhotoListModel(photos=parser.get_photos())

for photo in photos.photos:
    print('REF:', photo.index, photo.type, photo.tags)
    for photo_compared in photos.photos:
        print('\t COMPARE WITH:', photo_compared.index, photo_compared.type, photo_compared.tags)
        print('\t\tSCORE: ', photo.get_score(photo_compared))

v = photos.get_first_vertical_picture()
print(v.index, v.tags)

v2 = photos.get_picture_with_least_score_vertical(v)
print(v2.index, v2.tags)"""

"""for photo in photos:
    print('REF:', photo.index, photo.type, photo.tags)
    for photo_compared in photos:
        print('\t COMPARE WITH:', photo_compared.index, photo_compared.type, photo_compared.tags)
        print('\t\tSCORE: ', photo.get_score(photo_compared))"""
