def match(string):
    state = 0
    for char in string:
        if state == 0 and char == 'a':
            state = 1
        elif state == 1 and char == 'b':
            state = 2
    return state == 2

print(match("hello world"))  
print(match("ab"))  
print(match("aab"))  
print(match("abab"))
