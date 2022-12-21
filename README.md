# nordPing
A utility that pings a range of nordVPN servers and return the servers with the fastest response


## Help Output:
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

## Example Use:
### Input
```
python nordPing.py -c 3 -n 5 -C us -L 9372 -U 9390 -p 8
```

### Output
```

Settings:
-------------------------------
Ping count:             3
Country code:           us
Lower range:            9372
Upper range:            9390
Parallel Processes:     8

The 5 fastest responses are:
-------------------------------
 - us9373.nordvpn.com: 17.9 ms
 - us9382.nordvpn.com: 18.0 ms
 - us9378.nordvpn.com: 18.3 ms
 - us9385.nordvpn.com: 19.3 ms
 - us9379.nordvpn.com: 19.5 ms

```

## Contributions:
Contributions are welcome. Fork the repo, make your changes, create a diff file, and email the diff file to luis@moraguez.com

## Donations:
If this utility helped you with a project you're working on and you wish to make a donation, you can do so by clicking the donate button that follows. Thank you for your generosity and support!
<noscript><a href="https://liberapay.com/z3d6380/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a></noscript>
