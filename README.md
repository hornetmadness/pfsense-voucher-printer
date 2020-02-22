# Pfsence Voucher Printer

(https://syslinux.info)

This is some simple python scripts and Flask interface to importing and printing vouchers generated from pfsense

This was built to print vouchers on a thermal printer like [this one](https://www.amazon.com/gp/product/B07R39G4WZ/) and 
specificly to make use of [this app](https://play.google.com/store/apps/details?id=mate.bluetoothprint) for the printing.

Rolls from pfSense are store in a sqlite3 database. Since this uses [SQLAlchemy](https://www.sqlalchemy.org/) most any databases should work since I dont use dialects.

You should secure this by running it behind a real webserver like nginx or apache which provides the means for security.

FYI, if you try to run this in a desktop web browser, it might seem like its not working. Thats because the output generated after clicking the button 
is meant to only be supported by Android [bluetoohprint app](https://play.google.com/store/apps/details?id=mate.bluetoothprint).

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
[This image](https://hub.docker.com/r/hornetmadness/pfsense-voucher-printer) is provided


License
----
MIT

