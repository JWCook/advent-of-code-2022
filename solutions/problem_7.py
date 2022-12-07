from dataclasses import dataclass, field
from logging import getLogger

from solutions import INPUTS_DIR

logger = getLogger(__name__)


@dataclass
class Node:
    name: str = field()


@dataclass
class Directory(Node):
    parent: 'Directory' = field(default=None)
    children: list['Node'] = field(default_factory=list)
    total_size: int = field(default=None)

    def add_node(self, node: 'Node'):
        self.children.append(node)

    def get_node(self, name: str) -> 'Node':
        for child in self.children:
            if child.name == name:
                return child
        raise ValueError(name)

    def get_size(self) -> int:
        if not self.total_size:
            self.total_size = sum(child.get_size() for child in self.children)
        return self.total_size

    def get_subdirs(self) -> list['Directory']:
        return [child for child in self.children if isinstance(child, Directory)]


@dataclass
class File(Node):
    size: int = field(default=0)

    def get_size(self) -> int:
        return self.size


def count_directory_sizes(cmd_output: str) -> Directory:
    root = Directory(name='/')
    pwd = root
    for line in cmd_output.splitlines():
        line = line.strip()
        if line == '$ cd /' or line == '$ ls':
            pass
        elif line.startswith('$ cd '):
            name = line[5:]
            if name == '..':
                pwd = pwd.parent
            else:
                pwd = pwd.get_node(name)
        elif line.startswith('dir '):
            pwd.add_node(Directory(name=line[4:], parent=pwd))
        elif line[0].isdigit():
            size, name = line.split()
            pwd.add_node(File(name=name, size=int(size)))
        else:
            raise ValueError(line)
    return root


def get_subdir_totals(root: Directory, lvl: int = 0) -> int:
    total = 0
    sz = root.get_size()
    if sz <= 100000:
        total += sz
    padding = '  ' * lvl
    logger.info(f'{padding} {root.name}: {sz}')

    for subdir in root.get_subdirs():
        total += get_subdir_totals(subdir, lvl=lvl + 1)
    return total


if __name__ == '__main__':
    with open(INPUTS_DIR / 'input_7') as fp:
        data = fp.read()
    root = count_directory_sizes(data)
    total = get_subdir_totals(root)
    logger.info(f'Part 1: {total}')
