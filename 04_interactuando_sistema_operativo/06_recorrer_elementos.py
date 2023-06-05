import os

directorio=os.getcwd()

with os.scandir(path=directorio) as itr:
    for i in itr:
        # print(dir(i))
        if i.is_file():
            print(f"Es un archivo --> {i.name}")
        else:
            print(f"no es un archivo {i.name}")