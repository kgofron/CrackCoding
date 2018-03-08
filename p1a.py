MAX_CHARS = 26
def subStringsKDist(inputStr, num):
    # Return distinct substrings of input string of size K with K distinct characters
    strLen = len(inputStr)
    u = 0 # unique characters
    
    print("InputStr %s" % inputStr)
    print("stringLen %d" % strLen)
    pass

    # If there are not enough unique characters, show
    # an error message.
    if strLen < num:
        print "Not enough unique characters"
        return

    # Associative array to store the count
    count = [0] * MAX_CHARS
 
    # Tranversing the string and filling the count[] array of unique characters
    for i in xrange(num):
        if count[ord(inputStr[i])-ord('a')] == 0:
            u += 1
        count[ord(inputStr[i])-ord('a')] += 1
    print("count= %s" % count)

    # Otherwise take a window with first element in it.
    # start and end variables.
    curr_start = 0
    curr_end = 0    

subStringsKDist("abcd",3)
