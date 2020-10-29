'''
Validate if a string is a valid IP address.
'''

def ValidateIPAddress(ipadd):
    lst = [ip for ip in ipadd.split('.')]
    if len(lst) != 4:
        return False

    for key in lst:
        try:
            if int(key) >= 0 and int(key) <= 255:
                continue
            else:
                return False
        except:
            return False
    return True

def main():

    ip = '69.89.18.226'
    print(ValidateIPAddress(ip))

    ip='69.89.345.226'
    print(ValidateIPAddress(ip))

    ip = '69.89.345'
    print(ValidateIPAddress(ip))

    ip = '69.89.345.aa'
    print(ValidateIPAddress(ip))

if __name__=='__main__':
    main()