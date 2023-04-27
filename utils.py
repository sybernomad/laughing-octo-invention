import os
import socket


def verify_file_in_directory(filename, directory):
    """
    Verifies that a file with the given filename is located in the
    specified directory.

    :param filename: The name of the file to search for.
    :type filename: str
    :param directory: The directory in which to search for the file.
    :type directory: str

    :return: True if the file exists in the directory, False otherwise.
    :rtype: bool
    """
    # construct the full path to the file
    filepath = os.path.join(directory, filename)

    # check if the file exists
    if not os.path.exists(filepath):
        return False

    return True


def verify_host_ip(expected_ip):
    """
    Verifies whether the host machine is configured with the specified IP
    address.

    :param expected_ip: The IP address to check for.
    :type expected_ip: str

    :return: True if the host machine is configured with the specified IP
             address, False otherwise.
    :rtype: bool
    """
    # get the hostname
    hostname = socket.gethostname()
    # get a list of IP addresses for the hostname
    ip_list = socket.getaddrinfo(hostname, None, socket.AF_INET)
    # loop through the list of IP addresses
    for item in ip_list:
        # get the IP address as a string
        ip_address = item[4][0]
        # compare the IP address to the expected IP address
        if ip_address == expected_ip:
            return True
    # if no matching IP address was found, return False
    return False


def is_valid_ip_address(ip_address):
    """
    Verifies whether the specified string is a valid IP address.

    :param ip_address: The string to check for validity as an IP address.
    :type ip_address: str

    :return: True if the string is a valid IP address, False otherwise.
    :rtype: bool
    """
    try:
        # Try to convert the input string to an IP address
        socket.inet_aton(ip_address)
        return True
    except socket.error:
        return False


def is_valid_port(port_number):
    """
    Verifies whether the specified integer is a valid TCP/UDP port number.

    :param port_number: The integer to check for validity as a TCP/UDP port
                        number.
    :type port_number: int

    :return: True if the integer is a valid TCP/UDP port number, False
             otherwise.
    :rtype: bool
    """
    if port_number < 0 or port_number > 65535:
        return False
    else:
        return True
