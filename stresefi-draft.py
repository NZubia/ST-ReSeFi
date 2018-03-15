
class Node:

    # TODO: Complete class
    def __init__(self, word_reference=None):
        self.word_reference = word_reference
        self.tree_level = 0
        self.occurrences = 1
        self.childNodes = []


    # def node_into_children(self, current_node):
    #     for node in self.childNodes:
    #
    #         if node.word_reference == current_node.word_reference:
    #             return True
    #
    #     return False

    def add_node_to_children(self, node_to_add, parent_list):
        exists = False

        if len(self.childNodes) <= 0:
            if(self.word_reference):
                print(node_to_add.word_reference + "(" + str(id(node_to_add)) + ") is added to " + self.word_reference + "(" + str(id(self)) + ")")
            node_to_add.tree_level = self.tree_level + 1

            if node_to_add.tree_level <= MAX_LEVEL:
                self.childNodes.append(node_to_add)
                parent_list.append(node_to_add)
        else:
            for node in self.childNodes:
                if node.word_reference == node_to_add.word_reference:
                    node.occurrences += 1
                    exists = True
                    if node.tree_level <= MAX_LEVEL:
                        parent_list.append(node)

            if not exists:
                if node_to_add.tree_level <= MAX_LEVEL:
                    node_to_add.tree_level = self.tree_level + 1
                    self.childNodes.append(node_to_add)
                    parent_list.append(node_to_add)

    # def print_suffix_tree(self, root):
    #     if len(root.childNodes) <= 0:
    #         print(root.word_reference + " -> " + str(root.occurrences))
    #     for node in root.childNodes:

MAX_LEVEL = 2

if __name__ == '__main__':

    # Word sequence to be split
    # input = "can drive trucks safely, men drive cars safely, men can drive trucks"
    input = "can drive trucks safely, men drive cars safely, men can drive trucks"
    word_separator = " "
    sentence_delimiter = ","

    # Create split list
    sentence_split = input.split(sentence_delimiter) if sentence_delimiter != "" else input

    # Hash table creation
    # hash_table = set(split_list)
    hash_table = {}

    # Root Node creation
    root_node = Node()

    for sentence in sentence_split:
        # Create split list
        split_list = sentence.split(word_separator)

        # Clear parent list
        parent_list = []
 
        for value in split_list:

            if value != '':

                # TODO: Check what is more quick set or dict
                # Add value to hash table
                if value not in hash_table:
                    hash_table[value] = len(hash_table)

                # Create Node from value
                value_node = Node(value)

                # Add node to root node and parent list
                root_node.add_node_to_children(value_node, parent_list)

                print("Root node status:")
                for node in root_node.childNodes:
                    print(node.word_reference + "(" + str(id(node)) +")" + " -> " + str(node.occurrences))

                # parent_list.append(value_node)

                print("Parent list status")
                for node in parent_list:
                    print(node.word_reference + "(" + str(id(node)) +")")

                print()
                print()

                # Iterate parent list to add occurrences to nodes
                for node in parent_list[:-1]:
                    print("Current node in parent list: " + node.word_reference)
                    new_value_node = Node(value)
                    node.add_node_to_children(new_value_node, parent_list)
                    # parent_list.append(new_value_node)
                    parent_list.pop(0)
                print("--------------------------------")

    for node in root_node.childNodes:
        print(node.word_reference + "(" + str(id(node)) +")" + "-> " + str(node.occurrences))
        for child_node in node.childNodes:
            print("\t" + child_node.word_reference + "(" + str(id(child_node)) +")" + "-> " + str(child_node.occurrences))
            for last_child in child_node.childNodes:
                print("\t\t" + last_child.word_reference  + "(" + str(id(last_child)) +")" + "-> " + str(last_child.occurrences))
    # Switch keys and values to get the correct sequence
    # my_dict2 = {y: x for x, y in hash_table.items()}

