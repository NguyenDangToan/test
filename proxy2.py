import socket

# Khởi tạo socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(5)

# Chờ kết nối từ các ứng dụng
while True:
    try:
        connection, address = server_socket.accept()
        print("Received connection from", address)

        # Lấy dữ liệu từ kết nối
        data = connection.recv(1024)
        print("Received data:", data)

        # Tạo kết nối đến proxy
        proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_socket.connect(("127.0.0.1", 8081))

        # Gửi dữ liệu đến proxy
        proxy_socket.sendall(data)
        

        # Nhận dữ liệu từ proxy
        proxy_data = proxy_socket.recv(1024)
        print("Received data from proxy:", proxy_data)

        # Gửi dữ liệu đến ứng dụng
        connection.sendall(proxy_data)
    
    except Exception as e:
        print("Error:", e)
        continue

    # Đóng kết nối
    connection.close()
    proxy_socket.close()
