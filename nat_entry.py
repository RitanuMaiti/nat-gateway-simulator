from datetime import datetime


class NATEntry:

    def __init__(
        self,
        private_ip,
        private_port,
        public_ip,
        public_port,
        destination_ip,
        destination_port,
        protocol
    ):
        self.private_ip = private_ip
        self.private_port = private_port

        self.public_ip = public_ip
        self.public_port = public_port

        self.destination_ip = destination_ip
        self.destination_port = destination_port

        self.protocol = protocol

        self.state = "ACTIVE"

        self.created_at = datetime.now()
        self.last_activity = datetime.now()

    def update_activity(self):
        self.last_activity = datetime.now()
        self.state = "ACTIVE"

    def is_expired(self, timeout_seconds=10):

        current_time = datetime.now()

        elapsed_time = (
            current_time - self.last_activity
        ).total_seconds()

        if elapsed_time >= timeout_seconds:
            self.state = "EXPIRED"
            return True

        return False

    def __str__(self):

        return (
            f"{self.private_ip}:{self.private_port} "
            f"-> "
            f"{self.public_ip}:{self.public_port} "
            f"-> "
            f"{self.destination_ip}:{self.destination_port} "
            f"[{self.protocol}] "
            f"[{self.state}]"
        )