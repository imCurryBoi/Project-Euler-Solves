def decode(message, xor_values):
    return [message[i] ^ xor_values[i % len(xor_values)] for i in range(len(message))]

def read_ascii(message):
	return ''.join([chr(i) for i in message])

def read_file(f):
	msg = None
	with open(f, 'r') as file:
		for line in file:
			msg = line.split(',')
	return[int(i) for i in msg]

def write_file(txt, f):
	with open(f, 'a') as file:
		file.write(txt)
		file.close()

def clear_file(f):
	with open(f, 'w') as file:
		file.close()


message =  read_file('Message.txt')
console = 'Read.txt'
clear_file(console)

for i in range(97, 123):
	for j in range(97, 123):
		for k in range(97, 123):
			key = [i, j, k]
			decoded_message = decode(message, key)
			text = read_ascii(decoded_message)
			if (text.count('e') + text.count('E') + text.count('A') + text.count('a'))/len(text) > 0.15 and 'is' in text and 'are' in text: #filters to check for letter frequency and common words
				write_file(text, console)
				write_file(f' {i} {j} {k} ', console)
				write_file(str(sum(decoded_message)), console)
				write_file('\n', console)