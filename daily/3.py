
import sys
import site

print("Python Version:", sys.version)
print("\nSite Packages Paths:")
for path in site.getsitepackages():
    print(path)

try:
    import pyscreeze
    print("\npyscreeze found!")
    print(pyscreeze.__file__)
except ImportError:
    print("\npyscreeze not found.")
