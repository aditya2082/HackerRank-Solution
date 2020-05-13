'''
import re

for _ in range(int(input())):

    uid = input()

    # It must contain at least 2 uppercase English alphabet characters.
    c1 = len(re.findall(r"[A-Z]", uid)) >= 2

    # It must contain at least 3 digits (0-9).
    c2 = len(re.findall(r"[0-9]{3}", uid)) >= 3

    # It should only contain alphanumeric characters (a-z, A-Z & 0-9).
    c3 = len(re.findall(r"[a-zA-Z0-9]", uid)) == len(uid)

    # No character should repeat.
    c4 = len(set(uid)) == len(uid)

    # There must be exactly 10 characters in a valid UID.
    c5 = len(uid) == 10

    # must be valid all conditions
    print('Valid' if all([c1, c2, c3, c4, c5]) else 'Invalid')

'''
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

