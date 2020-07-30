#include <sys/socket.h>
#include <arpa/inet.h>	
#include <unistd.h>	
#include <fcntl.h>
#include <iostream>
#include <string.h>
#include <chrono>

#include <iostream>
#include <chrono>

int main(void) {
        
    struct sockaddr_in server;
    int sock;
    
    char buffer[2056];
    int byte_count;
    
    server.sin_addr.s_addr = inet_addr("81.169.145.90");
    server.sin_family = AF_INET;
	server.sin_port = htons(80);

    sock = socket(AF_INET, SOCK_STREAM, 0);

    connect(sock, (struct sockaddr *)&server, sizeof(server));

    char *header = "GET / HTTP/1.1\r\nHost: www.pieterboersma.nl\r\n\r\n";
    
    send(sock, header, strlen(header), 0);
    auto start = std::chrono::high_resolution_clock::now();

    byte_count = recv(sock, buffer, sizeof(buffer), 0);

    auto end = std::chrono::high_resolution_clock::now();

    int time = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() / 1000;

    float amount = 1000 / time;

    std::cout << (1000 / time) * byte_count / 1000 << " MB / second" << std::endl;

    //std::cout << buffer << std::endl; 
    return 0;
}