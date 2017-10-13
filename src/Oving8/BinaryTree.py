class BinaryTree:
    nodes = []

    def __init__(self):
        self.nodes = []

    def get_parent(self, node_index):
        try:
            return self.nodes[(node_index - 1) >> 1]
        except IndexError:
            return None

    def get_left_child(self, node_index):
        try:
            return self.nodes[(node_index << 1) + 1]
        except IndexError:
            return None

    def get_right_child(self, node_index):
        try:
            return self.nodes[(node_index + 1) << 1]
        except IndexError:
            return None
