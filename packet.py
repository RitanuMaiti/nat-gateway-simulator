class Packet:
    def __init__(
        self,
        source_ip,
        source_port,
        destination_ip,
        destination_port,
        protocol="TCP",
        data=""
    ):
        self.source_ip = source_ip
        self.source_port = source_port
        self.destination_ip = destination_ip
        self.destination_port = destination_port
        self.protocol = protocol
        self.data = data

    def __str__(self):
        return (
            f"{self.protocol} | "
            f"{self.source_ip}:{self.source_port} -> "
            f"{self.destination_ip}:{self.destination_port}"
        )