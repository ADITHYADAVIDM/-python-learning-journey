from pathlib import Path


path = Path("ecommerce")
print(path.exists())
path.mkdir()
path.rmdir()

path1 = Path()
print(path1.glob('*')) # for all files and dirs
print(path1.glob('*.*')) # for all files
print(path1.glob('*.py')) # for files of specific extension

# glob returns 'generator objects'. To access the contents you need to iterate over it.

for file in path1.glob('*'):
    print(file)