a_b = input()
a_c = input()
b_c = input()
if a_b == '=' and a_c == '=':
    print('abc\nacb\nbac\nbca\ncab\ncba')
elif a_b == '=':
    if a_c == '>':
        print('cab\ncba')
    else:
        print('abc\nbac')
elif a_c == '=':
    if a_b == '>':
        print('bac\nbca')
    else:
        print('acb\ncab')
elif b_c == '=':
    if a_b == '>':
        print('bca\ncba')
    else:
        print('abc\nacb')
else:
    if a_b == '>':
        if b_c == '>':
            print('cba')
        elif a_c == '>':
            print('bca')
        else:
            print('bac')
    elif a_b == '<':
        if b_c == '<':
            print('abc')
        elif a_c == '>':
            print('cab')
        else:
            print('acb')