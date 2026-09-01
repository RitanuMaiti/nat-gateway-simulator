from packet import Packet
from nat_entry import NATEntry
from statistics import NetworkStatistics


class NATGateway:

    def __init__(self, private_ip, public_ip):

        self.private_ip = private_ip
        self.public_ip = public_ip

        # NAT connection table
        self.translation_table = {}

        # Starting public port
        self.next_public_port = 40000

        # Network statistics
        self.statistics = NetworkStatistics()

    # ==========================================
    # OUTBOUND NAT / PAT
    # ==========================================

    def translate_outbound(self, packet):

        self.statistics.packet_sent()

        private_key = (
            packet.source_ip,
            packet.source_port,
            packet.destination_ip,
            packet.destination_port,
            packet.protocol
        )

        # Check whether connection already exists
        if private_key not in self.translation_table:

            public_port = self.next_public_port
            self.next_public_port += 1

            entry = NATEntry(
                private_ip=packet.source_ip,
                private_port=packet.source_port,

                public_ip=self.public_ip,
                public_port=public_port,

                destination_ip=packet.destination_ip,
                destination_port=packet.destination_port,

                protocol=packet.protocol
            )

            self.translation_table[private_key] = entry

            self.statistics.connection_created()

            print("\n[NAT] New connection created")
            print(f"[NAT] {entry}")

        else:

            entry = self.translation_table[private_key]

            entry.update_activity()

            print("\n[NAT] Existing connection found")

        # Create translated packet
        translated_packet = Packet(
            source_ip=entry.public_ip,
            source_port=entry.public_port,

            destination_ip=packet.destination_ip,
            destination_port=packet.destination_port,

            protocol=packet.protocol,
            data=packet.data
        )

        self.statistics.packet_translated()

        return translated_packet

    # ==========================================
    # INBOUND / REVERSE NAT
    # ==========================================

    def translate_inbound(self, packet):

        # Search for matching NAT connection
        for entry in self.translation_table.values():

            if (
                packet.destination_ip == entry.public_ip
                and
                packet.destination_port == entry.public_port
                and
                packet.source_ip == entry.destination_ip
                and
                packet.source_port == entry.destination_port
                and
                packet.protocol == entry.protocol
            ):

                entry.update_activity()

                self.statistics.packet_received()

                print("\n[NAT] Existing connection found")
                print("[NAT] Performing reverse translation")

                translated_packet = Packet(
                    source_ip=packet.source_ip,
                    source_port=packet.source_port,

                    destination_ip=entry.private_ip,
                    destination_port=entry.private_port,

                    protocol=packet.protocol,
                    data=packet.data
                )

                return translated_packet

        # No matching NAT entry
        self.statistics.packet_dropped()

        print("\n[NAT] No matching connection found")
        print("[NAT] Packet DROPPED")

        return None

    # ==========================================
    # REMOVE EXPIRED CONNECTIONS
    # ==========================================

    def remove_expired_entries(self, timeout_seconds=10):

        expired_keys = []

        for key, entry in self.translation_table.items():

            if entry.is_expired(timeout_seconds):

                print("\n[NAT] Connection expired")
                print(f"[NAT] Removing: {entry}")

                self.statistics.connection_expired()

                expired_keys.append(key)

        # Remove expired entries
        for key in expired_keys:

            del self.translation_table[key]

    # ==========================================
    # CHECK EXPIRATION
    # ==========================================

    def show_expired_check(self):

        print("\n========== CHECKING NAT EXPIRATION ==========")

        self.remove_expired_entries()

        print("=============================================")

    # ==========================================
    # SHOW NAT TABLE
    # ==========================================

    def show_translation_table(self):

        print("\n========== NAT CONNECTION TABLE ==========")

        if not self.translation_table:

            print("No active connections.")

        else:

            for entry in self.translation_table.values():

                print(entry)

        print("==========================================")

    # ==========================================
    # SHOW STATISTICS
    # ==========================================

    def show_statistics(self):

        self.statistics.show_statistics()