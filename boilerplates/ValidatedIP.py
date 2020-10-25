"""
Given an IP address as input, write a Python program to check whether the given IP Address is Valid or not.
"""

def validateIP(strIP):
    lst = strIP.split('.')
    if len(lst) != 4:
        return False
    else:
        for ip in lst:
            try:
                if int(ip) >=0 and int(ip) <= 255:
                    continue
                else:
                    return False
            except:
                return False
    return True

if __name__ == "__main__":
    assert (validateIP('192.168.0.1')) == True
    assert (validateIP('666.1.2.2')) == False
    assert (validateIP('ABC.1.2.2')) == False