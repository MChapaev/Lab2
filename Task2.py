def read_multiline():
    arr = []
    while True:
        text = input()
        if text:
            arr.append(text)
        else:
            break
    return arr


def find_synonyms(arr):
    synonyms = []
    for line in arr:
        words = line.split(' ')
        if len(words) > 1:
            if words[0].lower() in words[1].lower():
                synonyms.append(words[0])
    return synonyms


# Main
def main():
    print('Provide multiline (empty line to stop):')
    arr = read_multiline()
    print(find_synonyms(arr))


if __name__ == '__main__':
    main()
