import heapq
from collections import defaultdict

# Hàm đổi ký tự Ascii sang mã nhị phân :
def convert_string_to_binary(ch):
	n = ord(ch)
	tmp = f'{n:08b}'
	b = [0]*(8)
	for i in range(0,len(tmp)):
		b[i] = int(tmp[i])
	return b

# Hàm đổi mã nhị phân sang ký tự Ascii
def convert_binary_to_string(b):
	s = 0
	n = len(b)-1
	i = 0
	while(n > -1):
		if(b[n] != 0):
			s += pow(2,i)
		i += 1
		n -= 1

	return s

def list_dict(list_d):
	d = defaultdict(int)
	for i in list_d:
		d[i] += 1
	return d

# Hàm mã hóa Huffman
def encodingHuffman(data):
	list_frequency = list_dict(data)
	heap = [[weight, [symbol, '']] for symbol, weight in list_frequency.items()]
	heapq.heapify(heap)
	while len(heap) > 1:
		min_left = heapq.heappop(heap)
		min_right = heapq.heappop(heap)
		for bit in min_left[1:]:
			bit[1] = '0' + bit[1]
		for bit in min_right[1:]:
			bit[1] = '1' + bit[1]
		heapq.heappush(heap, [min_left[0] + min_right[0]] + min_left[1:] + min_right[1:])
	heap_temp = heapq.heappop(heap)[1:]
	result = sorted(heap_temp)
	#result = sorted(heap_temp, key = lambda p : (len(p[-1]), p))
	return result,list_frequency

# Hàm chuyển kí tự sang mã nhị phân
def decode(l):
	result = ""
	for i in l:
		t = str((convert_string_to_binary(i))).replace(" ","")
		t = t.replace(",","")
		t = t.replace("[","")
		t = t.replace("]","")
		result += t + " "
	return result

# Hàm nén và giải nén bằng cây Huffman
def Encoding_Decoding(file_input,file_output):
	from dahuffman import HuffmanCodec
	inp = open(file_input,"r")
	data = inp.read()
	inp.close

	list_frequency = list_dict(data)
	codec = HuffmanCodec.from_data(list_frequency)

	encoded = codec.encode(data)
	f = open("output_bin.txt","wb")
	f.write(encoded)
	f.close()

	f1 = open("output_bin.txt","rb")
	bi = f1.read()
	f1.close()

	t = codec.decode(bi)
	result = ""
	for i in t:
		result += i
	f_out = open(file_output, "w")
	f_out.write(result)
	f_out.close()
	#codec.print_code_table()
 

# Demo cây Huffman

data = "The frog at the bottom of the well drifts off into the great ocean"
huff, frequency = encodingHuffman(data)[0], encodingHuffman(data)[1]
print("Binary    " + "Symbol".ljust(7) + "   Frequency".ljust(10) + " Huffman Code")
i = 0
for p in huff:
	print(decode(data[i]),p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
	i += 1

# Demo nén và giải nén file

#Với data.txt là file cần nén và file output.txt là file được giải nén từ file nén là output_bin.txt

#Encoding_Decoding("data.txt","output.txt")


