import os

db_string = "sqlite:///database/vouchers.sqlite3"
db_debug=False
debug=False

tcpPort = os.environ.get("TCPPORT", "4040")
ifaceAddress = os.environ.get("IFADDR", "127.0.0.1")

force_ssl = True