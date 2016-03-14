#!/bin/python3

# from setuptools import setup, find_packages

# compile qt ui
from PyQt5.uic import compileUiDir
compileUiDir('qt', False, lambda dir, mod: ('moc', mod))

# compile qt rcs
from subprocess import check_output
f = open('rsclist_rc.py', 'w')
f.write(check_output(['pyrcc5', 'rsclist.qrc']).decode())
f.close()

# py -> executable
# print(check_output(['pyinstaller', '-F', '-i',
#                     'img/logo.ico', 'mochi-player.py']).decode())


# setup(
#     name='Mochi Player',
#     version='0.1.0',
#     author='u8sand',
#     author_email='u8sand@gmail.com',
#     description='The mpv based media player',
#     license='GPLv2',
#     keywords='media player mochi mpv',
#     url='https://github.com/mochi-player/mochi-player',
#     packages=['src'],
#     include_package_data=True,
#     install_requires=[],
#     package_data={},
# )
