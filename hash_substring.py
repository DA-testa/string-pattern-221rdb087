# python 3
def read_input():
    input_type = input().strip().lower()
    if input_type == "i":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == "f":
        filename = input()
        with open(filename, "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    else:
        raise ValueError("Invalid input type")
    return pattern, text


def print_occurrences(output):

    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash(pattern)
    t_hash = hash(text[:p_len])

    occurrences = []
    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if text[i:i+p_len] == pattern:
                occurrences.append(i)
        if i < t_len - p_len:
            t_hash = hash(text[i+1:i+1+p_len])

    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


