#!/usr/bin/env python

# File: nordPing.py
# Author: Luis Moraguez
# Date: 2022-12-21
# Description: This script will ping the NordVPN servers and return the fastest three
# Usage: python nordPing.py -c <ping_count> -n <top_n> -C <country_code> -L <lower_range> -U <upper_range> -p <processes> --version

from collections import defaultdict
from multiprocessing import Pool
from multiprocessing.managers import BaseManager, DictProxy
import argparse
import os
import sys

# Create a multiprocessing default dictionary
class MyManager(BaseManager):
    pass

MyManager.register('defaultdict', defaultdict, DictProxy)

# Function to ping the servers
def ping(ping_count, country_code, i, results):
    if ping_count == 1:
        # Ping the server
        ping = os.popen('ping -c ' + str(ping_count) + ' ' + country_code + str(i) + '.nordvpn.com 2> /dev/null').read()
        # Get the time
        time = ping.split('time=')[1].split(' ')[0].strip() #print(country_code + str(i) + '.nordvpn.com: ' + time)
        # Store only successful pings
        results[country_code + str(i) + '.nordvpn.com'] = time
    elif ping_count > 1:
        # Ping the server
        ping = os.popen('ping -c ' + str(ping_count) + ' ' + country_code + str(i) + '.nordvpn.com 2> /dev/null').read()
        # Get the times
        times = ping.split('time=')[1:]
        # Get the average time
        time = 0
        for t in times:
            time += float(t.split(' ')[0].strip())
        time /= ping_count
        # Store only successful pings
        results[country_code + str(i) + '.nordvpn.com'] = str(round(time, 1))
    else:
        print('Invalid ping count')
        sys.exit(1)

# Driver code
if __name__ == '__main__':
    # Get the arguments
    parser = argparse.ArgumentParser(prog = 'python nordPing.py', description = 'This script will ping the NordVPN servers and return the ones with the fastest response times')
    parser.add_argument('-c', '--ping_count', type=int, default=1, help='Number of pings to send to each server (Default: 1)')
    parser.add_argument('-n', '--top_n', type=int, default=3, help='Number of fastest responses to return (Default: 3)')
    parser.add_argument('-C', '--country_code', type=str, default='us', help='Country code for the servers to ping (Default: us)')
    parser.add_argument('-L', '--lower_range', type=int, default=5500, help='Lower range of the servers to ping (Default: 5500)')
    parser.add_argument('-U', '--upper_range', type=int, default=5502, help='Upper range of the servers to ping (Default: 5502)')
    parser.add_argument('-p', '--processes', type=int, default=5, help='Number of processes to use (Default: 5)')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = parser.parse_args()

    # Create a pool of processes and the shared dictionary for the results
    pool = Pool(processes=args.processes)
    mgr = MyManager()
    mgr.start()
    results = mgr.defaultdict()

    # Ping the servers
    for i in range(args.lower_range, args.upper_range + 1):
        pool.apply_async(ping, (args.ping_count, args.country_code, i, results))

    # Close the pool and wait for the processes to finish
    pool.close()
    pool.join()

    # Sort the results
    sorted_results = sorted(results.items(), key=lambda x: float(x[1]))

    # Print the argument values
    print('\nSettings:\n-------------------------------')
    print('Ping count:\t\t' + str(args.ping_count))
    print('Country code:\t\t' + args.country_code)
    print('Lower range:\t\t' + str(args.lower_range))
    print('Upper range:\t\t' + str(args.upper_range))
    print('Parallel Processes:\t' + str(args.processes) + '\n')

    # Check if there are enough servers to return the top_n
    if len(sorted_results) < args.top_n:
        args.top_n = len(sorted_results)

    # Print the fastest top_n servers
    if args.top_n > 0:
        print('The ' + str(args.top_n) + ' fastest responses are:\n-------------------------------')
        for i in range(args.top_n):
            print(' - ' + sorted_results[i][0] + ': ' + sorted_results[i][1] + ' ms')
        print('')
    else:
        print('\nNo servers in the range responded to the ping\n')