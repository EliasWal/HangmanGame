import socket,time

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("127.0.0.1",1235))
	
	msg = s.recv(1024).decode()
	print(msg)
	
	# Send to server required infos
	q1 = s.recv(1024).decode()
	print(q1)
	word = input()
	s.send(word.encode())
	
	q2 = s.recv(1024).decode()
	print(q2)
	definition = input()
	s.send(definition.encode())
	
	while True:
		response = s.recv(1024).decode()
		if "You won!" in response:
			print("Client 2 won the game!")
			break
		elif "You lost!" in response:
			print("Client 2 lost the game!")
			break
		else:
			print("Status: ", response)
	
	s.close()

if __name__ == "__main__":
	main()
