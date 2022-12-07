class Node:
    def __init__(self, file_name, parent=None, size=0, is_dir=False):
        self.parent = parent
        self.children = {}
        self.file_name = file_name
        self.size = size
        self.is_dir = is_dir

    def add_child(self, child):
        self.children[child.file_name] = child
        self.size += child.size
        curr = self
        while curr.parent:
            curr.parent.size += child.size
            curr = curr.parent

    def __iter__(self):
        yield self
        for child in self.children.values():
            yield from child


def populate_file_system():
    data = map(str.split, open('terminal_commands.txt').readlines())
    root = Node("/", None, 0, True)
    current = root

    for command in data:
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '/':
                    current = root
                elif command[2] == '..':
                    current = current.parent
                else:
                    child = Node(command[2], current, 0, True)
                    current.add_child(child)
                    current = child
        elif command[0] == 'dir':
            child = Node(command[1], current, 0, True)
            current.add_child(child)
        else:
            size = command[0]
            name = command[1]
            child = Node(name, current, int(size), False)
            current.add_child(child)
    return root


root = populate_file_system()

print(sum(dir.size for dir in root if dir.is_dir and dir.size <= 100000))

size_to_delete = 30000000 - (70000000 - root.size)
print(min(dir.size for dir in root if dir.is_dir and dir.size > size_to_delete))
