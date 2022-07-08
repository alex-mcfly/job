# print(task(1,1,2,2,3,3,4,4))
# >> OUT: False

def correct_sides(x1, y1, x2, y2, x3, y3, x4, y4):
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2), min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

def task(x1, y1, x2, y2, x3, y3, x4, y4):
    x1, y1, x2, y2, x3, y3, x4, y4 = correct_sides(x1, y1, x2, y2, x3, y3, x4, y4)
    if (x3 >= x2) or (x1 >= x4) or (y3 >= y2) or (y1 >= y4):
        return False, 0
    else:
        l = max(x1, x3)
        r = min(x2, x4)
        b = max(y1, y3)
        t = min(y2, y4)

        area = (r - l) * (t - b)
        return True, area

if __name__ == '__main__':
    cors = [int(cor) for cor in input().split()]
    print(task(*cors))
