import sys

class EncodingTable:
    """
    A class to represent an Encoding Table made from a Huffman Tree
    Attributes
    ----------
    encode : str
        The dictionary storing for each symbol "char" as binary bit string code "code"
    """

    def __init__(self, tree):
        """
        Constructs an EncodingTable using a HuffmanTree
        :param tree: The HuffmanTree to use to build the EncodingTable dictionary encode
        """
        # Create empty dictionary
        self.encode = {}
        # Launch recursive function to store values into self.encode dictionary
        self.recurse(tree, "")

    # PART 7 (recurse)
    def recurse(self, tree, code):
        """
        :param tree: the HuffmanTree tree to use to determine the codes
        :param code: the current string code created so far
        :return: None
        """

        # If the bit for the tree is not None, then modify the code to add a “1” if the bit was True 
        # or “0” if the bit was False
        if tree.bit != None:
            if tree.bit == True:
                code += "1"
            else:
                code += "0"

        # If the method reaches a HuffmanTree tree which has a None left and right sub-tree. 
        # Then store the current parameter code in the dictionary self.encode at the symbol tree.char.
        if tree.left == None and tree.right == None:
            self.encode[tree.char] = code
            return

        # Rucursive case
        if tree.left != None:
            self.recurse(tree.left, code)
        if tree.right != None:
            self.recurse(tree.right, code)

    # PART 6 (string)
    def __str__(self):
        """
        This method produces a string from the dictionary encode storing the encoding where each line in 
        the string is an entry such as
        'd':1110
        'e':1111
        'h':000
        'l':10
        'o':01
        'r':001
        'w':110
        :return: None
        """
        str = ""
        for a_key in sorted(self.encode.keys()):
            # print(f"DEBUG: {a_key} > {self.encode[a_key]}")
            str += f"{repr(a_key)}:{self.encode[a_key]}\n"
        return str 

    def encode_text(self, text):
        """
        Encodes the provided text using the internal encoding dictionary (turns each character symbol into a bit string)
        :param text: The string text to encode
        :return: A bit string "000100" based on the internal encode dictionary
        """
        output_text = ""
        # Loop through characters
        for char in text:
            # If one matches then encode into bitstring
            if char in self.encode:
                output_text += self.encode[char]
            else:
                sys.exit(f"Can't encode symbol {char} as it isn't in the encoding table:\n{self}")
        print(f"Input Text: {text}")
        print(f"Output Text: {output_text}")
        return output_text

