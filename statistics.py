class NetworkStatistics:

    def __init__(self):

        self.packets_sent = 0
        self.packets_translated = 0
        self.packets_received = 0
        self.packets_dropped = 0

        self.connections_created = 0
        self.connections_expired = 0

    # =================================
    # PACKET EVENTS
    # =================================

    def packet_sent(self):
        self.packets_sent += 1

    def packet_translated(self):
        self.packets_translated += 1

    def packet_received(self):
        self.packets_received += 1

    def packet_dropped(self):
        self.packets_dropped += 1

    # =================================
    # CONNECTION EVENTS
    # =================================

    def connection_created(self):
        self.connections_created += 1

    def connection_expired(self):
        self.connections_expired += 1

    # =================================
    # DISPLAY STATISTICS
    # =================================

    def show_statistics(self):

        print("\n")
        print("============================================")
        print("             NETWORK STATISTICS")
        print("============================================")

        print(f"Packets Sent        : {self.packets_sent}")
        print(f"Packets Translated  : {self.packets_translated}")
        print(f"Packets Received    : {self.packets_received}")
        print(f"Packets Dropped     : {self.packets_dropped}")

        print("--------------------------------------------")

        print(f"Connections Created : {self.connections_created}")
        print(f"Connections Expired : {self.connections_expired}")

        print("============================================")