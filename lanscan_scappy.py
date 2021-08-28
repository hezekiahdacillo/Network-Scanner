from datetime import datetime
import scapy.all as scapy
import re


def print_logo():
    """
    Prints my logo.
    """
    print(r'''
     _   _  ____       ____ _   __ _       _       ____              _  _  _
    | | | |/ ___|____ / ___| | / /(_)     | |     |  _ \            (_)| || |
    | |_| | |_  |__  | |_  | |/ /  _  ____| |___  | | | | ____  ___  _ | || | ___
    |  _  |  _|   / /|  _| |   <  | |/ _  `  _  \ | | | |/ _  `/ __)| || || |/ _ \
    | | | | |__  / /_| |__ | |\ \ | | (_) | | | | | |_| | (_) | |__ | || || | (_) |
    |_| |_|\____|____|\____|_| \_\|_|\__,_|_| |_| |____/ \__,_|\___)|_||_||_|\___/
    ''')
    print()
    print('   ' + '*' * 80)
    print('   *' + (' ' * 78) + '*')
    print('   *' + (' ' * 21) + f'Copyright of Hezekiah Dacillo, {datetime.today().year}' + (' ' * 22) + '*')
    print('   *' + (' ' * 78) + '*')
    print('   ' + '*' * 80)
    print()
    print()


def error(message):
    """
    Prints the error message and exits the program.
    :param message: error message
    """
    print(message)


def get_add_range():
    """
    Gets the range of the IP addresses.
    """
    ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

    # Get the address range to ARP
    while True:
        range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
        if ip_pattern.search(range_entered):
            error(f'{range_entered} is a valid ip address range')
            break
    return range_entered


def send_arp_msg(range_entered):
    """
    Sends ARP messages to the IP address range supplied by the user.
    """
    arp_result = scapy.arping(range_entered)

if __name__ == '__main__':
    print_logo()
    range_entered = get_add_range()
    send_arp_msg(range_entered)
