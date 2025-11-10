class NetworkDevice:
    def __init__(self, name, ip_address, mac_address):
        self.name = name
        self.ip_address = ip_address
        self.mac_address = mac_address


class DesktopPC(NetworkDevice):
    def __init__(self, name, ip_address, mac_address, os):
        super().__init__(name, ip_address, mac_address)
        self.os = os


class Printer(NetworkDevice):
    def __init__(self, name, ip_address, mac_address, color_type):
        super().__init__(name, ip_address, mac_address)
        self.color_type = color_type

    def print(self):
        print("Printer is printing...")
