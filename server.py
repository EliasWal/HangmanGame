import socket, time


def hangman(word_given, def_given,cl1, cl2):
    guessed = ["_"] * len(word_given)
    attempts_left = 6
    
    word_given=word_given.lower()

    cl2.sendall(f"Definition: {def_given}".encode())

    while "_" in guessed and attempts_left > 0:
        aux = " ".join(guessed)
        cl2.sendall(f"{aux} {attempts_left}".encode())
        cl1.sendall(f"{aux} {attempts_left}".encode())
        guess = cl2.recv(1024).decode().lower()
        print(guess)

        if guess in word_given:
            for i in range(len(word_given)):
                if word_given[i] == guess:
                    guessed[i] = guess
        else:
            attempts_left -= 1

    if "_" not in guessed:
        cl2.sendall(f"You won! The word was {word_given}".encode())
        cl1.sendall(f"You won! The word was {word_given}".encode())
    else:
        cl2.sendall(f"You lost! The word was {word_given}".encode())
        cl1.sendall(f"You lost! The word was {word_given}".encode())

	

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("127.0.0.1",1235))
	s.listen()
	
	print("Waiting for first client to connect")
	(client1, address1) = s.accept()
	print("Client 1 connected at address:",address1)
	
	print("Waiting for second client to connect")
	client1.sendall("Wait for second client to connect. Think about a word!".encode())
	(client2, address2) = s.accept()
	print("Client 2 connected at address:", address2)
	
	client1.sendall("Word:".encode())
	word = client1.recv(1024).decode()
	print("Word:",word)
	
	client1.sendall("Definition:".encode())
	definition = client1.recv(1024).decode()
	print("Definition:",definition)
	
	hangman(word,definition,client1,client2)
	
	client1.close()
	client2.close()
	s.close()
	print("Server closed")

if __name__ == "__main__":
	main()
