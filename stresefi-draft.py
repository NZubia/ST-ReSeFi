
class Node:

    word = ""
    occurrences = 0
    childNodes = []

    # TODO: Create constructor
    # TODO: Redefine class

if __name__ == '__main__':

    # Word sequence to be split
    input = "A,B,C,D,E,A,B,C,D"
    word_separator = ","
    sentence_delimiter = ""

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
 
        for value in sentence:

            # Add value to hash table
            if value not in hash_table:
                hash_table[value] = len(hash_table)
            print(hash_table)

    print(hash_table)
