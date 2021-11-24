import os
import random

# file = '../testfile.txt'
# if not os.path.exists(file):
#     open(file, 'w').close()
# try:
#     with open(file, 'r') as reader:
#         print('before:')
#         print(reader.read())
# except FileNotFoundError:
#     print('file not found')
#
# content = ''
# for i in range(0, 100):
#     random_char = chr(random.randint(ord('A'), ord('Z')))
#     if random.randint(0, 15) == 0:
#         content += '\n'
#     content += random_char
# with open(file, 'w') as writer:
#     writer.write(str(content))
