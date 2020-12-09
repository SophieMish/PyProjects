import os


def iter_files(path):
    folder = []
    for i in os.walk(path):
        folder.append(i)
    for address, dirs, files in folder:
        for file in files:
            print(address + file, sep='/')


iter_files('C:/Users/User/PycharmProjects/iad1')