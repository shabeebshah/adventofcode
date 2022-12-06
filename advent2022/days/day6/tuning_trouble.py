def find_start(length):
    datastream = open('datastream.txt').read()
    return next(i for i in range(length, len(datastream)) if len(set(datastream[i-length:i])) == length)


print(find_start(4))
print(find_start(14))