from packet import Packet


class Host:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def create_packet(self, destination_ip, destination_port, source_port):
        packet = Packet(
            source_ip=self.ip,
            source_port=source_port,
            destination_ip=destination_ip,
            destination_port=destination_port,
            protocol="TCP"
        )

        return packet

    def __str__(self):
        return f"{self.name} ({self.ip})"