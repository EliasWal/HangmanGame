import socket,time

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("127.0.0.1",1235))
	
	#Receive definition from server
	response = s.recv(1024).decode()
	print(response)
	
	while True:
		response = s.recv(1024).decode()
		print("Hei: " , response)

		if "You won!" in response or "You lost!" in response:
			break
			
		input_char = input("Enter the next letter: ")
		s.sendall(input_char.encode())
		
	s.close()
	
if __name__ == '__main__':
    main()
