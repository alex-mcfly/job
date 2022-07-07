# print(task("111111111110000000000000000"))
# >> OUT: 10

def task(array):
    return array.index('0') - 1

if __name__ == '__main__':
    print(task('111111111110000000000000000'))
