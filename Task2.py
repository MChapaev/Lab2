def build_genealogy_tree(pairs):
    tree = {}
    for child, parent in pairs:
        tree[child] = parent
        if parent not in tree:
            tree[parent] = None

    return tree


def is_ancestor(tree, ancestor, descendant):
    while descendant in tree and tree[descendant] is not None:
        if tree[descendant] == ancestor:
            return True
        descendant = tree[descendant]
    return False


def process_queries(tree, queries):
    results = []
    for a, b in queries:
        if is_ancestor(tree, a, b):
            results.append(1)
        elif is_ancestor(tree, b, a):
            results.append(2)
        else:
            results.append(0)
    return results


# Main
def main():
    print('Provide multiline (empty line to stop):')
    data = [
        ("Alexei", "Peter_I"),
        ("Anna", "Peter_I"),
        ("Elizabeth", "Peter_I"),
        ("Peter_II", "Alexei"),
        ("Peter_III", "Anna"),
        ("Paul_I", "Peter_III"),
        ("Alexander_I", "Paul_I"),
        ("Nicholaus_I", "Paul_I")
    ]

    queries = [
        ("Peter_I", "Paul_I"),
        ("Paul_I", "Peter_I"),
        ("Alexei", "Elizabeth")
    ]

    tree = build_genealogy_tree(data)
    results = process_queries(tree, queries)
    for res in results:
        print(res)


if __name__ == '__main__':
    main()
