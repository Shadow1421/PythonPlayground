def create_ip_address(address_string):
    if len(address_string) < 4 or len(address_string) > 12:
        return "Invalid input - 1"

    ip_address = []
    for i in range(3, 0, -1):
        ip_part = address_string[-i:]
        if int(ip_part) > 255:
            return "Invalid input - 2"
        ip_address.append(ip_part)
        address_string = address_string[:-i]
    
    ip_address.append(address_string)
    ip_address.reverse()
    formatted_ip = ".".join(ip_address)

    return "IP Address = " + formatted_ip

# Test with sample inputs
addressString1 = "19216801"
print(create_ip_address(addressString1))

addressString2 = "190145"
print(create_ip_address(addressString2))
