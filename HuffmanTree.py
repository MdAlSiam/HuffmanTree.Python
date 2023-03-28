class HuffmanTree:
    """
    A class to represent an Huffman Tree
    Attributes
    ----------
    char : str
        The characters represented by this tree
    count : int
        The count of how many times char occurred in the text
    left : HuffmanTree/None
        The left HuffmanTree below this one
    right : HuffmanTree/None
        The right HuffmanTree below this one
    bit : bool
        The bit symbol used to reach this HuffmanTree (either True/False for 1/0)


    General Structure
                         HuffmanTree (char,count,bit)
                          /    \
                      left    right
                        /        \
                HuffmanTree      HuffmanTree

    Default Structure
                         HuffmanTree (char,count,None)
                          /    \
                      left    right
                        /        \
                     None         None
    """

    # PART1 (constructor)
    def __init__(self, char, count, left=None, right=None, bit=None):
        """
        Constructs a Huffman Tree
        :param char: the char to be stored in the tree
        :param count: the count of how many times that char occurred in the text
        :praram left: a link to a left HuffmanTree (default None)
        :param right: a link to a right HuffmanTree (default None
        :param bit: a boolean bit that stores if this tree was reached with a 0 (False) or a 1 (True) (default None)
        """
        self.char = char
        self.count = count
        self.left = left
        self.right = right
        self.bit = bit 

    # PART2 (order)
    def __lt__(self, other): 
        """
        Compares one HuffmanTree to another HuffmanTree 
        :param other: HuffmanTree other that is being compared to the current HuffmanTree self
        :return: True or False depending on conditions
        """
        if self.count > other.count:
            # This method should return True if the count for self is greater than that of other
            return True
        elif self.count < other.count:
            # This method should return False if the count for self is less than that of other
            return False
        else:
            # If the counts are the same, then it should return True 
            # if self’s char is greater than that of other, 
            # otherwise False
            if self.char > other.char:
                return True
            else:
                return False

    # PART3 (string)
    def __str__(self):
        """
        produce a string of the form "(char,count,left char,right char,bitstring)"
        :return: string
        """
        str = "("
        str += repr(self.char)
        str += ","
        str += f"{self.count}"
        str += ","
        str += self.left.char if self.left is not None else "None"
        str += ","
        str += self.right.char if self.right is not None else "None"
        str += ","
        str += "1" if self.bit is True else "1"
        str += ")"
        return str 

    # PART3 (representation)
    def __repr__(self):
        """
        produce a string of the form "HuffmanTree(char,count,left,right,bit)"
        :return: string
        """
        str = "HuffmanTree("
        str += repr(self.char)
        str += ","
        str += repr(self.count)
        str += ","
        str += self.left.char if self.left is not None else "None"
        str += ","
        str += self.right.char if self.right is not None else "None"
        str += ","
        str += repr(self.bit)
        str += ")"
        return str

    # PART5 (equality)
    def __eq__(self, other):
        """
        This method compares one HuffmanTree to another HuffmanTree and allows to decide if they are equal (==)
        :param other: an other Huffman Tree to compare
        :return: None
        """
        if other == None:
            # should return False if other is None
            return False
        elif self.char == other.char and self.left == other.left and self.right == other.right:
            # This method should return True if the char, left, and right of self/other are all equal
            return True
        else:
            # Otherwise, if should return False
            return False

# PART1 (make_trees)
def make_trees(dictionary):
    """
    Loops through all symbols (keys) in the dictionary and creates a default HuffmanTree 
    :param dictionary: dictionary which stores each symbol from the input file as a key char such that 
    dictionary[char] = count, where count is how many times that symbol occurred in the file
    :return: a list of created Huffman trees
    """
    # List of Huffman Trees created for each characters
    HuffmanTrees = [] 
    # Loop through the keys of the dictionary
    for a_key in dictionary.keys():
        # Create a Huffman Tree for the character in the key
        print("Count:", a_key, dictionary[a_key])
        a_node = HuffmanTree(a_key, dictionary[a_key])
        HuffmanTrees.append(a_node)
    return HuffmanTrees

# PART4 (merge)
def merge(t1, t2):
    """
    Merges two Huffman Tree
    :param t1: Huffman Tree
    :param t2: Huffman Tree
    :return: a new Huffman merging t1 and t2
    """
    char = t1.char + t2.char
    count = t1.count + t2.count
    left = t1
    right = t2
    bit = None

    merged_tree = HuffmanTree(char, count, left, right, bit)

    if t1.count == t2.count:
        if t1.char < t2.char:
            t1.bit = 0
            t2.bit = 1
        else:
            t1.bit = 1
            t2.bit = 0
    elif t1.count < t2.count:
        t1.bit = 0
        t2.bit = 1
    else:
        t1.bit = 1
        t2.bit = 0

    return merged_tree

