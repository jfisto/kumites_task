import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent
KUMITE_DIR = BASE_DIR / "src" / "kumite"

print(KUMITE_DIR)