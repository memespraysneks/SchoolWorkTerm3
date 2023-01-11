#! /usr/bin/env python3

from collections import namedtuple
from pprint import pprint
import abc
import argparse
import hashlib
import os
import re
import shlex
import subprocess
import sys
import textwrap
import uuid

vboxmanage = "vboxmanage"

vm_credentials = {    
    'r3': { 'login' : 'root', 'password' : 'P@ssw0rd' },    
    "pc1": { 'login' : 'root', 'password' : 'P@ssw0rd' },
    "pc2": { 'login' : 'root', 'password' : 'P@ssw0rd' }
}

def process_args(arguments=sys.argv[1:]) -> str:
    """Parses command line arguments into studentID

    Returns:
        studentID
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=("Verifies project DHCP and Dynamic Routing"),
        epilog=textwrap.dedent('''\
            Examples:
                m_dynamic_routing.py A012367
            '''))
    parser.add_argument('studentID',
                        help="your student number")

    args = parser.parse_args(arguments)

    return args.studentID


class Operation(metaclass=abc.ABCMeta):
    def __init__(self, desc, vm, cmd):
        self.desc = desc
        self.vm = vm
        self.cmd = cmd

    @abc.abstractmethod
    def execute(self):
        pass

class Run(Operation):
    def execute(self):
        guest_cmd_split = shlex.split(self.cmd)
        command = subprocess.run(
            [
                vboxmanage,
                'guestcontrol',
                self.vm,
                'run',
                '--username',
                vm_credentials[self.vm]['login'],
                '--password',
                vm_credentials[self.vm]['password'],
                '--',
                *guest_cmd_split
            ],
            text=True,
            stdout=subprocess.PIPE
        )

        return command.stdout

class Copy_from(Operation):
    def execute(self):
        guest_cmd_split = self.cmd.split()
        command = subprocess.run(
            [
                vboxmanage,
                'guestcontrol',
                self.vm,
                'copyfrom',
                '--username',
                vm_credentials[self.vm]['login'],
                '--password',
                vm_credentials[self.vm]['password'],
                 '-R',
                '--target-directory',
                *guest_cmd_split
            ],
            text=True,
            stdout=subprocess.PIPE
        )

        return command.stdout

def perform(operations, out_file):
    for operation in operations:
        out_file.write('\n\n' + operation.vm + " " + operation.desc + '\n')
        out_file.write(operation.execute())

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
    outputfile_name =  'final_network_configuration_' + studentID + '.txt'
    output_path = os.path.join(script_dir, outputfile_name)
    vm_info_regex= re.compile(r'(?:NIC \d:\s+.+)')

    operations = [
        Run('IPv4 Address', 'r3', '/usr/sbin/ip -4 address show'),
        Run('IPv4 Routes', 'r3', '/usr/sbin/ip -4 route show'),
        Run('r3 DHCP configuration', 'r3', '/usr/bin/cat /etc/dhcp/dhcpd.conf'),
        Run('r3 BIRD configuration', 'r3', '/usr/bin/cat /etc/bird.conf'),
        Run('IPv4 Address', 'pc1', '/usr/sbin/ip -4 address show'),
        Run('IPv4 Routes', 'pc1', '/usr/sbin/ip -4 route show'), 
        Run('IPv4 Address', 'pc2', '/usr/sbin/ip -4 address show'),
        Run('IPv4 Routes', 'pc2', '/usr/sbin/ip -4 route show'),               
        Run('Traceroute to web', 'pc1', '/usr/bin/traceroute -In 10.0.100.1'),
        Run('Traceroute to ws1', 'pc2', '/usr/bin/traceroute -In 10.0.100.2'),        
        Run('dhcpd log', 'r3', '/usr/bin/journalctl -u dhcpd --no-pager'),
    ]

    with open(output_path, 'w', errors='ignore') as output_file:

        output_file.write("Final Network Configuration " + studentID + '\n') 

        for vm in ["r3", "pc1", "pc2"]:
            print(f'Retrieving {vm} Network Info')
            output_file.write(f'\n\n{vm} Info\n' )
            cmd = subprocess.run([vboxmanage, 'showvminfo', vm], text=True, stdout=subprocess.PIPE)
            output_file.write('\n\n'.join(vm_info_regex.findall(cmd.stdout)).replace(',','\n'))

        perform(operations, output_file)
        output_file.write('\nUID:' + hex(uuid.getnode()))

    append_digest(output_path)

if __name__ =="__main__":
    main()