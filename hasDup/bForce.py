def hasDup(ints):
    for i in range(0, len(ints)):
        for j in range(i+1, len(ints)):
            if ints[i] == ints[j]:
                print("True")
                return True
    print("False")
    return False

ints = [1,2,3,4,5,1,2,7]
hasDup(ints)
