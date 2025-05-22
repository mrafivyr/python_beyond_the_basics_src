import sys
import reader.reader as rr

print(dir(rr))
print(rr.__name__)
print(rr.__file__)
rc = rr.Reader(sys.argv[1])
try:
    print(rc.read())
finally:
    rc.close()
