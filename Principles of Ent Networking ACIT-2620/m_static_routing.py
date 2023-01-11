#! /usr/bin/env python3

from collections import namedtuple
from pprint import pprint
import argparse
import hashlib
import os
import subprocess
import sys
import textwrap
import uuid

op = namedtuple('operation', ['desc', 'cmds'])

vbox_command = "vboxmanage" 
web_ip = "10.0.100.1"
ws1_ip = "10.0.100.2"
ws2_ip = "10.0.200.1"

def process_args(arguments=sys.argv[1:]) -> str:
    """Parses command line arguments into studentID

    Returns:
        studentID
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=("Verifies project IPv4 address assignment and routing"),
        epilog=textwrap.dedent('''\
            Examples:
                m_static_routing.py A012367
            '''))
    parser.add_argument('studentID',
                        help="your student number")

    args = parser.parse_args(arguments)

    return args.studentID

def append_digest(report_path): 
    """Appends a 10 bit hex blake2 file hash to file name

    Args:
        report_path (os.path): file name to append blake2 hash to
    """
    with open(report_path) as report_file:
        buffer = report_file.read()
        digest = hashlib.blake2b(digest_size=5)
        digest.update(buffer.encode())

    new_path = report_path[0:-4] + '_' + digest.hexdigest() + report_path[-4:]
    os.rename(report_path, new_path)

def main() -> None:

    studentID = process_args()

    # Use a file path relative to the executing file so that we always know
    # where the output is going
    script_dir = os.path.dirname(__file__)
    outputfile_name =  'static_routing_report_' + studentID + '.txt'
    output_path = os.path.join(script_dir, outputfile_name)

    operations = [
        op('Traceroute web -> ws2', [vbox_command,'guestcontrol', 'web','run','--exe', '/usr/bin/traceroute','--username', 'root','--password','P@ssw0rd', '--','traceroute', '-I', '-n', '-q', '1', ws2_ip]),
        op('Traceroute ws1 -> ws2', [vbox_command,'guestcontrol', 'ws1','run','--exe', '/usr/bin/traceroute','--username', 'root','--password','P@ssw0rd', '--','traceroute', '-I', '-n', '-q', '1', ws2_ip]),
        op('r1 IPv4 Addresses', [vbox_command,'guestcontrol', 'r1','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'address', 'show']),
        op('r1 Bridge Info', [ vbox_command,'guestcontrol', 'r1','run','--exe', '/usr/sbin/bridge','--username', 'root','--password','P@ssw0rd', '--','bridge/arg0', 'link', 'show']),
        op('r1 IPv4 Routes', [vbox_command,'guestcontrol', 'r1','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'route', 'show']),
        op('r2 IPv4 Addresses', [vbox_command,'guestcontrol', 'r2','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'address', 'show']),
        op('r2 IPv4 Routes', [vbox_command,'guestcontrol', 'r2','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'route', 'show']),
        op('web IPv4 Addresses', [vbox_command,'guestcontrol', 'web','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'address', 'show']),
        op('web IPv4 Routes', [vbox_command,'guestcontrol', 'web','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'route', 'show']),
        op('ws1 IPv4 Addresses', [vbox_command,'guestcontrol', 'ws1','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'address', 'show']),
        op('ws1 IPv4 Routes', [vbox_command,'guestcontrol', 'ws1','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'route', 'show']),
        op('ws2 IPv4 Addresses', [vbox_command,'guestcontrol', 'ws2','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'address', 'show']),
        op('ws2 IPv4 Routes', [vbox_command,'guestcontrol', 'ws2','run','--exe', '/usr/sbin/ip','--username', 'root','--password','P@ssw0rd', '--','ip', '-4', 'route', 'show']),
    ]

    with open(output_path, 'w') as output_file:

        output_file.write("IPv4 Static Routing Report " + studentID + '\n') 

        for operation in operations:
            output_file.write('\n\n' + operation.desc + '\n\n')
            command = subprocess.run(operation.cmds, text=True, stdout=subprocess.PIPE)
            output_file.write(command.stdout)

        output_file.write('\nUID:' + hex(uuid.getnode()))

    append_digest(output_path)

if __name__ =="__main__":
    main()