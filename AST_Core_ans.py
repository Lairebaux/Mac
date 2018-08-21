from random import choice
from random import randint


class Domain:
    all_domains_macs = {}

    def __init__(self, id=None, name=None):
        self.id = id
        self.Name = str(name)
        self.mac_addresses = []


    def _add_domain_id(self, mac_adr):
        """add mac address to dict"""
        self.all_domains_macs[self.id] = mac_adr[:5]


    def _check_duplicates(self, mac_adr):
        """verify mac addresses do not have different keys"""
        if mac_adr[:5] in self.all_domains_macs.values():
            raise ValueError("Mac batch already registered")


    def generate_random_macs(self, mac_adr=None, amount=10):
        """generate 10 mac addresses"""
        if not mac_adr:
            mac_adr = self._random_macs()
        self._check_duplicates(mac_adr)
        for _ in range(amount):
            x = mac_adr.split(":", maxsplit=2)
            a, b, *c = x
            mac = [
                int(a, 16),
                int(b, 16),
                randint(0x0, 0xff),
                randint(0x0, 0xff),
                randint(0x0, 0xff),
                randint(0x0, 0xff),
            ]
            mac_formatted = ":".join("{:02X}".format(n) for n in mac)
            self.mac_addresses.append(mac_formatted)
        self._add_domain_id(mac_formatted[:5])


    def _random_macs(self):
        """random generator helper"""
        letters = ["A", "B", "C", "D", "E", "F"]
        numbers = [i for i in range(9)]
        x = ""
        for _ in range(6):
            if randint(0, 1) == 0:
                x += "{}{}:".format(choice(letters), choice(numbers))
            else:
                x += "{}{}:".format(choice(numbers), choice(numbers))
        return x[:-1]


def mac_format(mac_address):
    """strip colon from mac address"""
    mac = mac_address.split(":")
    colon_stripped = "".join(mac)
    return colon_stripped


def hex_to_decimal(mac_address):
    """convert hexadecimal to decimal"""
    mac_hex = mac_format(mac_address)
    dec = int(str(mac_hex), 16)
    return dec


def lookup_mac_address_domain(mac):
    """lookup domain name in dict"""
    d = Domain().all_domains_macs
    for key, value in d.items():
        if d[key] == mac[:5]:
            return "Mac address in Domain: {}.".format(key)
    return "Mac address not registered."


