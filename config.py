import os

bind = os.environ.get("BIND","127.0.0.1:5000") #gunicorn
db_string = os.environ.get("DB_FILE","sqlite:///database/vouchers.sqlite3")
db_debug=os.environ.get("DB_DEBUG",False)
debug=os.environ.get("DEBUG",False)
force_ssl = os.environ.get("FORCE_SSL",True)
