import heapq
from functools import total_ordering
import os
# a node has char and freq
class HeapNode:
    def  __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq
    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq

# a huffman tree     
class Huffman:
    def __init__(self, path): 
        self.path = path
        self.heap = []
        self.reverseMapping = {}
        self.code = {}
        
    #check all character in str -> count the number of occurrences of that character
    #=> array 
    def makefreqDict(self, str):
        freq = {}   # frequency
        for char in str:        #character
            if not char in freq:
                freq[char] = 0
            else:
                freq[char] +=1
        return freq
    #
    def makeHeap(self, freq):
        for key in freq:
            node = HeapNode(key, freq[key])
            heapq.heappush(self.heap, node)
            
    def mergeNodes(self):
        while(len(self.heap)>1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)
            
    def makeCodeSP(self,root, currentCode):
        if(root == None):
            return
        if(root.char != None):
            self.code[root.char] = currentCode
            self.reverseMapping[currentCode] = root.char
            return
            
        #huffman tree: 0 -> node left and 1 -> node right
        self.makeCodeSP(root.left, currentCode + '0')
        self.makeCodeSP(root.right, currentCode + '1')
        
    def makeCodes(self):
        root = heapq.heappop(self.heap)
        currentCode = ''
        self.makeCodeSP(root, currentCode)
    def get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.code[character]
        return encoded_text


    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text


    def get_byte_array(self, padded_encoded_text):
        if(len(padded_encoded_text) % 8 != 0):
            print("Encoded text not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            b.append(int(byte, 2))
        return b


    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()

            freq = self.makefreqDict(text)
            self.makeHeap(freq)
            self.mergeNodes()
            self.makeCodes()

            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)

            b = self.get_byte_array(padded_encoded_text)
            output.write(bytes(b))

        print("Compressed")
        return output_path

# đây là phần decompression
    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_text = padded_encoded_text[8:] 
        encoded_text = padded_encoded_text[:-1*extra_padding]

        return encoded_text

    def decode_text(self, encoded_text):
        currentCode = ""
        decoded_text = ""

        for bit in encoded_text:
            currentCode += bit
            if(currentCode in self.reverseMapping):
                character = self.reverseMapping[currentCode]
                decoded_text += character
                currentCode = ""

        return decoded_text


    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"

        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""

            byte = file.read(1)
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_text = self.remove_padding(bit_string)

            decompressed_text = self.decode_text(encoded_text)
			
            output.write(decompressed_text)

        print("Decompressed")
        return output_path

path = "data.txt"

h = Huffman(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)

    