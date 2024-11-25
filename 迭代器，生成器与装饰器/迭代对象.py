import sys

list_t = ["天云赐福","寒樱赐福","清音赐福"]

cc = iter(list_t)

while True :
    try :
        print(next(cc))
    except StopIteration:
        sys.exit()

