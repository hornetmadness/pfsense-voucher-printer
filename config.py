import os

db_string = "sqlite:///database/vouchers.sqlite3"
db_debug=False
debug=False

tcpPort = os.environ.get("TCPPORT", "5000")
ifaceAddress = os.environ.get("IFADDR", "127.0.0.1")

print_url = "print"

force_ssl = True