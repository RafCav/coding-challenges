"""
https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
"""

if __name__ == '__main__':
    N = int(input())

    commands = [input().strip() for _ in range(N)]  # Save command into a list

    result = []
    for command in commands:
        c = command.split()  # split the string (default whitespaces)

        # Command 1: insert e i (Insert integer e at position i)
        if c[0] == 'insert':
            result.insert(int(c[1]), int(c[2]))
        # Command 2: print (Print the list)
        elif c[0] == 'print':
            print(result)
        # Command 3: remove e (Delete the first occurrence of integer e)
        elif c[0] == 'remove':
            result.remove(int(c[1]))
        # Command 4: append e (Insert integer e at the end of the list)
        elif c[0] == 'append':
            result.append(int(c[1]))
        # Command 5: sort (Sort the list)
        elif c[0] == 'sort':
            result.sort()
        # Command 6: pop (Pop the last element from the list)
        elif c[0] == 'pop':
            result.pop()  # Delete the last item of the list
        # Command 7: reverse (Reverse the list)
        elif c[0] == 'reverse':
            result.reverse()  # Reverse the order of the list