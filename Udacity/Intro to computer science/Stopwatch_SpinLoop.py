import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1

#print time_execution('1 + 1')
#print time_execution('spin_loop(10 ** 4)')[1]]

### making a big index
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def make_string(p):
    s = ""
    for e in p:
        s = s + e
    return s

def make_big_index(size):
    index =[]
    letters = ['a','a','a','a','a','a','a','a']
    while len(index) < size:
        word = make_string(letters)
        add_to_index(index, word, 'fake')
        for i in range(len(letters) - 1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break
            else:
                letters[i] = 'a'
    return index

#print make_big_index(3)

def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

index10000 = make_big_index(10000)
print time_execution('lookup(index10000, "udacity")')
#if input size * 10,then time also  *10
