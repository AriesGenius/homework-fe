import re


class ClassComponet:
    def __init__(self, name, title):
        self.name = name
        self.title = title

components = []
with open('database.txt') as f:
    for line in f:
        if 'ClassComponet' in line:
            try:
                name = line.split('=')[0]
                title = line.split('=')[1].strip().replace("ClassComponet", "").split(',')
            except ValueError:
                continue




for component in components:
    print(component.name, component.title)
