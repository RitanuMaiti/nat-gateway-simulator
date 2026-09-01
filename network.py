class Network:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def show_devices(self):
        print("\n========== NETWORK ==========")

        for device in self.devices:
            print(device)

        print("=============================")