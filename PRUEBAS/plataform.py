from platform import platform, machine, system, version
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr, end= ' ')

print()

print(machine())
print(system(), end=' ')
print(version())

print(platform())
print(platform(1))
print(platform(0, 1))