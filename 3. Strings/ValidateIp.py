def validateIp(ip):
    groups = ip.split('.')

    if (len(groups) != 4):
        return 0
    
    for group in groups:
        if not group.isdigit() or int(group) > 255:
            return 0

    return 1

print(validateIp('123.123.123.255'))