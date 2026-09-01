from packet import Packet


class InternetServer:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def receive_packet(self, packet):
        print(f"\n[SERVER] {self.name} received packet")
        print(f"[SERVER] {packet}")

        # Create a response
        response = Packet(
            source_ip=self.ip,
            source_port=packet.destination_port,
            destination_ip=packet.source_ip,
            destination_port=packet.source_port,
            protocol=packet.protocol,
            data="HTTP Response: Hello from Internet Server!"
        )

        print("[SERVER] Sending response")

        return response

    def __str__(self):
        return f"{self.name} ({self.ip})"