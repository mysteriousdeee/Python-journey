from time import ctime
from pathlib import Path
import shutil

path = Path("packages")
path.exists()
path.is_file()
path.is_dir()

# print(path.name)
# print(path.parent)
# print(path.absolute)
# print(path)
# path.unlink()

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob("*.py")]
print(py_files)

print(path.stat())
print(ctime(path.stat().st_ctime))

# print(path.read_text())
# path.write_text("....")
target = Path() / "__init__.py"
# target.write_text(path.read_text())

shutil.copy(path, target)
