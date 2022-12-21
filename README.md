# nordPing
A utility that pings a range of nordVPN servers and return the servers with the fastest response

```
python nordPing.py [-h] [-c PING_COUNT] [-n TOP_N] [-C COUNTRY_CODE] [-L LOWER_RANGE] [-U UPPER_RANGE] [-p PROCESSES] [--version]

This script will ping the NordVPN servers and return the ones with the fastest response times

optional arguments:
  -h, --help            show this help message and exit
  -c PING_COUNT, --ping_count PING_COUNT
                        Number of pings to send to each server (Default: 1)
  -n TOP_N, --top_n TOP_N
                        Number of fastest responses to return (Default: 3)
  -C COUNTRY_CODE, --country_code COUNTRY_CODE
                        Country code for the servers to ping (Default: us)
  -L LOWER_RANGE, --lower_range LOWER_RANGE
                        Lower range of the servers to ping (Default: 5500)
  -U UPPER_RANGE, --upper_range UPPER_RANGE
                        Upper range of the servers to ping (Default: 5502)
  -p PROCESSES, --processes PROCESSES
                        Number of processes to use (Default: 5)
  --version             show program's version number and exit
```
