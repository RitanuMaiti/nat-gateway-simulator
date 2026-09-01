from host import Host
from nat_gateway import NATGateway
from network import Network
from server import InternetServer
from packet import Packet

import time


# ==================================================
# NAT GATEWAY SIMULATOR
# ==================================================

print("\n")
print("====================================================")
print("             NAT GATEWAY SIMULATOR")
print("====================================================")


# ==================================================
# CREATE PRIVATE HOSTS
# ==================================================

pc_a = Host(
    name="PC-A",
    ip="10.0.0.10"
)

pc_b = Host(
    name="PC-B",
    ip="10.0.0.11"
)

pc_c = Host(
    name="PC-C",
    ip="10.0.0.12"
)


# ==================================================
# CREATE NAT GATEWAY
# ==================================================

nat = NATGateway(
    private_ip="10.0.0.1",
    public_ip="203.0.113.10"
)


# ==================================================
# CREATE INTERNET SERVER
# ==================================================

server = InternetServer(
    name="Web Server",
    ip="198.51.100.20"
)


# ==================================================
# CREATE NETWORK
# ==================================================

network = Network()

network.add_device(pc_a)
network.add_device(pc_b)
network.add_device(pc_c)
network.add_device(nat)
network.add_device(server)


# ==================================================
# SHOW NETWORK
# ==================================================

network.show_devices()


# ==================================================
# PC-A CONNECTION
# ==================================================

print("\n\n====================================================")
print("                 PC-A CONNECTION")
print("====================================================")

packet_a = pc_a.create_packet(
    destination_ip=server.ip,
    destination_port=80,
    source_port=5000
)

print("\n[PC-A] Sending:")
print(packet_a)

translated_a = nat.translate_outbound(packet_a)

print("\n[NAT] Forwarding to Internet:")
print(translated_a)

response_a = server.receive_packet(translated_a)

private_response_a = nat.translate_inbound(response_a)

if private_response_a:

    print("\n[PC-A] Received:")
    print(private_response_a)


# ==================================================
# PC-B CONNECTION
# ==================================================

print("\n\n====================================================")
print("                 PC-B CONNECTION")
print("====================================================")

packet_b = pc_b.create_packet(
    destination_ip=server.ip,
    destination_port=80,
    source_port=5000
)

print("\n[PC-B] Sending:")
print(packet_b)

translated_b = nat.translate_outbound(packet_b)

print("\n[NAT] Forwarding to Internet:")
print(translated_b)

response_b = server.receive_packet(translated_b)

private_response_b = nat.translate_inbound(response_b)

if private_response_b:

    print("\n[PC-B] Received:")
    print(private_response_b)


# ==================================================
# PC-C CONNECTION
# ==================================================

print("\n\n====================================================")
print("                 PC-C CONNECTION")
print("====================================================")

packet_c = pc_c.create_packet(
    destination_ip=server.ip,
    destination_port=80,
    source_port=5000
)

print("\n[PC-C] Sending:")
print(packet_c)

translated_c = nat.translate_outbound(packet_c)

print("\n[NAT] Forwarding to Internet:")
print(translated_c)

response_c = server.receive_packet(translated_c)

private_response_c = nat.translate_inbound(response_c)

if private_response_c:

    print("\n[PC-C] Received:")
    print(private_response_c)


# ==================================================
# DISPLAY NAT TABLE
# ==================================================

print("\n\n====================================================")
print("              CURRENT NAT TABLE")
print("====================================================")

nat.show_translation_table()


# ==================================================
# UNSOLICITED INBOUND TRAFFIC TEST
# ==================================================

print("\n\n====================================================")
print("          UNSOLICITED INBOUND TRAFFIC TEST")
print("====================================================")

attacker_packet = Packet(
    source_ip="203.0.113.50",
    source_port=9999,

    destination_ip="203.0.113.10",
    destination_port=45000,

    protocol="TCP",

    data="Unauthorized connection attempt"
)

print("\n[ATTACKER] Sending:")
print(attacker_packet)

result = nat.translate_inbound(attacker_packet)

if result is None:

    print("\n[SECURITY] Unauthorized packet blocked successfully.")


# ==================================================
# NAT TIMEOUT TEST
# ==================================================

print("\n\n====================================================")
print("                 NAT TIMEOUT TEST")
print("====================================================")

print("\n[NAT] Active connections before timeout:")

nat.show_translation_table()

print("\n[TEST] Waiting 11 seconds...")
print("[TEST] NAT timeout configured for 10 seconds.")

time.sleep(11)

nat.show_expired_check()


# ==================================================
# NAT TABLE AFTER TIMEOUT
# ==================================================

print("\n[NAT] Connections after timeout:")

nat.show_translation_table()


# ==================================================
# FINAL STATISTICS
# ==================================================

print("\n\n====================================================")
print("                FINAL STATISTICS")
print("====================================================")

nat.show_statistics()


# ==================================================
# SIMULATION COMPLETE
# ==================================================

print("\n")
print("====================================================")
print("             SIMULATION COMPLETE")
print("====================================================")