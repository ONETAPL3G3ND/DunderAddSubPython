class Client:
    def __init__(self, ip: str, name: str) -> None:
        self.ip = ip
        self.name = name

    def SendMessage(self, text):
        print(f"[{self.ip}] {text}")


class Server:
    def __init__(self):
        self.clients = []

    def __add__(self, other: Client) -> None:
        self.clients.append(other)
        print(f"New client connected: {other.name}")

    def __sub__(self, other: Client) -> None:
        self.clients.remove(other)
        print(f"Client disabled: {other.name}")

    def GetAllClient(self) -> list:
        return self.clients

    def SendMessageToIP(self, ip: str, text: str) -> None:
        for client in self.clients:
            if client.ip == ip:
                client.SendMessage(text)
                break
        else:
            raise Exception


if __name__ == "__main__":
    server = Server()
    client1 = Client("192.168.2.3", "Kilka")
    client2 = Client("192.168.3.1", "Vasya")
    client3 = Client("192.168.5.1", "Sanya")

    server + client1
    server + client2
    server + client3

    print(server.GetAllClient())
    server.SendMessageToIP("192.168.3.1", "hi")

    server - client2

    server.SendMessageToIP("192.168.3.1", "hello")

