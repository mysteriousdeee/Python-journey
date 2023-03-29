from pathlib import Path
from zipfile import ZipFile

with ZipFile("files.zip", 'w') as zip:
    for path in Path("packages").rglob("*.*"):
        zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("packages/subpackage/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
