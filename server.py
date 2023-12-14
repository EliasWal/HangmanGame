import socket, time

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("127.0.0.1",1234))
	s.listen()
	
	print("Waiting for first client to connect")
	(client1, address1) = s.accept()
	print("Client 1 connected at address:",address1);
	
	print("Waiting for second client to connect")
	(client2, address2) = s.accept()
	print("Client 2 connected at address:", address2);
	
	client1.close();
	client2.close();
	s.close();
	print("Server closed")

if __name__ == "__main__":
	main()
