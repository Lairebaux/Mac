import pytest
from random import seed
from .AST_Core_ans import Domain
from .AST_Core_ans import mac_format
from .AST_Core_ans import hex_to_decimal
from .AST_Core_ans import lookup_mac_address_domain


@pytest.fixture(scope="module")
def d1():
    """Domain 1 instance"""
    return Domain(43960, "Domain 1")


@pytest.fixture(scope="module")
def d2():
    """Domain 2 instance"""
    return Domain(48059, "Domain 2")

@pytest.fixture(scope="module")
def d3():
    """Domain 3 instance"""
    return Domain(52428, "Domain 3")


@pytest.fixture(scope="module")
def mac_1():
    """mac address 1"""
    return "F4:AD:1D:0C:EC:27"


@pytest.fixture(scope="module")
def mac_2():
    """mac address 2"""
    return "13:45:FB:A1:2C:0D"


@pytest.fixture(scope="module")
def mac_3():
    """mac address 3"""
    return


@pytest.mark.parametrize("mac_adr, expected",[
    (mac_1(), "F4AD1D0CEC27"),
    (mac_2(), "1345FBA12C0D")
])
def test_mac_format(mac_adr, expected):
    """remove colons in mac addresses"""
    assert mac_format(mac_adr) == expected


@pytest.mark.parametrize("mac_adr, expected",[
    (mac_1(), 269024353905703),
    (mac_2(), 21191295314957)
])
def test_hex_to_decimal(mac_adr, expected):
    """hexadecimal to decimal conversion"""
    assert hex_to_decimal(mac_adr) == expected


@pytest.mark.parametrize("names, expected",[
    (d1().Name, "Domain 1"),
    (d2().Name, "Domain 2"),
    (d3().Name, "Domain 3"),
])
def test_Domain_names(names, expected):
    """verify domain Name"""
    assert names == expected


def test_wrong_domain_name(d1):
    """raises exception for wrong Domain name"""
    with pytest.raises(AssertionError):
        assert d1.Name == "jon"


@pytest.mark.parametrize("ids, expected",[
    (d1().id, 43960),
    (d2().id, 48059),
    (d3().id, 52428),
])
def test_Domain_ids(ids, expected):
    """verify domain Name"""
    assert ids == expected


@pytest.mark.parametrize("mac_adr, expected",[
    (mac_1(), ['F4:AD:44:20:82:3C', 'F4:AD:FD:E6:F1:C2',
               'F4:AD:6B:30:F9:0E', 'F4:AD:C7:DD:01:E4',
               'F4:AD:88:75:34:A2', 'F4:AD:0F:0B:0D:04',
               'F4:AD:C3:6E:D8:0E', 'F4:AD:71:E0:FD:77',
               'F4:AD:B0:76:70:EB', 'F4:AD:94:0B:D5:33']),
])
def test_Domain_1_mac_addresses(d1, mac_adr, expected):
    """populate Domain 1 given mac address 1"""
    seed(1)
    d1.generate_random_macs(mac_adr)
    assert d1.mac_addresses == expected


@pytest.mark.parametrize("mac_adr, expected",[
    (mac_2(), ['13:45:44:20:82:3C', '13:45:FD:E6:F1:C2',
               '13:45:6B:30:F9:0E', '13:45:C7:DD:01:E4',
               '13:45:88:75:34:A2', '13:45:0F:0B:0D:04',
               '13:45:C3:6E:D8:0E', '13:45:71:E0:FD:77',
               '13:45:B0:76:70:EB', '13:45:94:0B:D5:33']),
])
def test_Domain_2_mac_addresses(d2, mac_adr, expected):
    """populate Domain 2 given mac address 2"""
    seed(1)
    d2.generate_random_macs(mac_adr)
    assert d2.mac_addresses == expected


@pytest.mark.parametrize("mac_adr, expected",[
    (None, ['E1:17:88:75:34:A2','E1:17:0F:0B:0D:04',
            'E1:17:C3:6E:D8:0E','E1:17:71:E0:FD:77',
            'E1:17:B0:76:70:EB','E1:17:94:0B:D5:33',
            'E1:17:5F:97:3D:AA','E1:17:D8:61:9B:91',
            'E1:17:FF:C9:11:F5','E1:17:7C:CE:D4:58']),
])
def test_Domain_3_mac_addresses(d3, mac_adr, expected):
    """populate Domain 3 by generating random mac address"""
    seed(1)
    d3.generate_random_macs(mac_adr)
    assert d3.mac_addresses == expected


def test_duplicate_mac_addresses(d1):
    """generating different mac addresses for a Domain should raise exception"""
    with pytest.raises(ValueError):
        seed(1)
        d1.generate_random_macs(mac_2())
        

@pytest.mark.parametrize("mac_adr, expected",[
    (mac_1(), "Mac address in Domain: 43960."),
    (mac_2(), "Mac address in Domain: 48059."),
    ("E1:17:C3:6E:D8:0E", "Mac address in Domain: 52428."),
    ("B5:D3:C9:41:14:75", "Mac address not registered."),
])
def test_lookup_mac_address(mac_adr, expected):
    """lookup mac address by first 4 characters"""
    assert lookup_mac_address_domain(mac_adr) == expected


def test_domain_sizes(d1, d2, d3):
    """total mac addresses equals 30"""
    l = [len(d1.mac_addresses), len(d2.mac_addresses), len(d3.mac_addresses)]
    assert sum(l) == 30


def test_view_domain_mac_keys():
    """all Domains and mac keys"""
    assert Domain().all_domains_macs == \
           {43960: "F4:AD", 48059: "13:45", 52428: "E1:17"}



