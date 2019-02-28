#!/usr/bin/python3

from collections import Counter

class TagsModel:
    def __init__(self, tagList):
        self.tags = tagList

    def get_number_of_common_tags(self, tags: list) -> int:
        return [{'tagName': x, 'occurrences': self.tags.count(x)} for x in tags]
    
    def __str__(self):
        return ''.join(self.tags)
    
class PhotoModel:
    def __init__(self, idx, typeOfPhoto, tags):
        self.type = typeOfPhoto
        self.tags = tags
        self.index = idx

    def get_tag_model(self):
        return self.tags

    def get_number_of_common_tags(self, tags: list) -> int:
        return [{'tagName': x, 'occurrences': self.tags.count(x)} for x in tags]

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
    

parser = Parser('e_shiny_selfies.txt')
photos = parser.get_photos()
