# Pfsence Voucher Printer

(https://syslinux.info)

This is a simple python and Flask interface to importing and printing vouchers generated from pfsence

This was built to print vouchers on a thermal printer like [this one](https://www.amazon.com/gp/product/B07R39G4WZ/) and specificly to make use of [this app](https://play.google.com/store/apps/details?id=mate.bluetoothprint) for the printing

### Installation

Requires [Python](https://www.python.org/) v3+ to run.

```sh
$ git clone https://github.com/hornetmadness/pfsence-voucher-printer.git
$ cd pfsence-voucher-printer
```

#### Install the dependencies
```sh
$ pip install -r requriements.txt
```
#### Import the CSV Rolls
```sh
$ python import.py --file /tmp/roll1 --minutes 60
```
#### Start the server
```sh
$ ./start.sh
```

### Docker
[This image](https://hub.docker.com/repository/docker/hornetmadness/pfsence-voucher-printe) is provided


License
----
MIT

