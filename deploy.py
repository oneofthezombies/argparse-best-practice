from shutil import rmtree
from subprocess import run
from pathlib import Path
from itertools import chain
from more_itertools import consume


dirnames = ['build', 'dist']
paths = map(lambda path: Path(path), dirnames)
outputs = chain(paths, Path().glob('*.egg-info'))
exists = filter(lambda path: path.exists(), outputs)
deletes = map(lambda path: rmtree(path), exists)
consume(deletes)

run(['python3', 'setup.py', 'sdist', 'bdist_wheel']).check_returncode()
run(['python3', '-m', 'twine', 'upload', 'dist/*']).check_returncode()
