"""
Given a list of file names with extension, sort them based on the extension
"""

import os
files = ['cat_pictures.zip', 'fluffy.jpg', 'meow.mp3', 'ascii_cat.txt', 'dog_pic.zip']
files = sorted(files, key=lambda x: os.path.splitext(x)[1])
print(files)
