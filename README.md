# Mac

Question 1:
Your are given the following class:

class Domain:
	id = None
	Name = None
	mac_addresses = None

Define a valid __init__ method so that when a Domain object is instantiated, an id is assigned to Domain.id, a string to the Domain.name and an empty list is assigned is Domain.mac_addresses

Question 2:
You have 3 domains that are currently unpopulated, and a new task requires you to generate 10 unique MAC addresses for each domain, where each MAC address contains 12 hexadecimal characters that are colon-separated every 2 characters.

Ie: Valid MAC addresses include, but are not limited to:
-	F4:AD:1D:0C:EC:27
-	13:45:FB:A1:2C:0D

Using the code from question 1, you instantiate 3 domains with the following ids:
-	D1.id = 43690
-	D2.id = 48059
-	D3.id = 52428

Populate each domain such that the first 4 characters of a domain’s MAC address can allow us to identify which domain it belongs to, and such that each domain has 10 unique MAC addresses 
