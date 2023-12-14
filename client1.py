import socket,time

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("127.0.0.1",1234))
	
	# Send to server required infos
	q1 = s.recv(1024).decode()
	print(q1)
	word = input()
	s.send(word.encode())
	
	q2 = s.recv(1024).decode()
	print(q2)
	definition = input()
	s.send(definition.encode())


if __name__ == "__main__":
	main()
