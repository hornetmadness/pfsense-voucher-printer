import config
from flask import Flask, request, Response, make_response
from db import Vouchers, connect_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, asc
import json
from htmlmaker import render

app = Flask(__name__)

db=connect_db() #establish connection
Session = sessionmaker(bind=db)
session = Session()

@app.route("/", methods=["GET"])
def index():
  av = session.query(
    Vouchers.time, 
    func.count(Vouchers.time)).filter(
      Vouchers.disabled == 0
  ).group_by(Vouchers.time)

  url = request.url
  if bool(config.force_ssl):
    url = url.replace("http:", "https:",1)
    url = f"{url}print"
  else:
    url = f"{url}print"
  return render(url, av)


@app.route("/print", methods=["GET"])
def printer():
  time = int(request.args.get('time'))

  if not time:
    return """<h2>Invalid Input</h3>"""

  #Grab the token FIFO style
  tix = session.query(Vouchers).filter(
    Vouchers.time == time,
    Vouchers.disabled == 0
  ).order_by(
    asc(Vouchers.date_added)
  ).first()

  if not bool(tix):
    return "<h3>No active vouchers found in the database</h3>"
  
  #This is the json required my the android app
  voucher = {
    "0": {
      "type": "0",
      "content": " <br />",
      "bold": "0",
      "align": "0"
    },
    "1": {
      "type": "0",
      "content": f"{tix.time} minutes",
      "bold": "1",
      "align": "1",
      "format": "2",
    },
    "2": {
      "type": "0",
      "content": "-------------------------<br />",
      "bold": "0",
      "align": "1"
    },
    "3": {
      "type": "0",
      "content": f"Code:",
      "bold": "1",
      "align": "1",
      "format": "3",
    },
    "4": {
      "type": "0",
      "content": f"{tix.vid}",
      "bold": "1",
      "align": "1",
      "format": "3",
    },
    "5": {
      "type": "0",
      "content": "-------------------------<br />",
      "bold": "0",
      "align": "1"
    },
    "6": {
      "type": "0",
      "content": " <br />",
      "bold": "0",
      "align": "0"
    },
    "7": {
      "type": "0",
      "content": " <br />",
      "bold": "0",
      "align": "0"
    }
  }
  tix.disabled = 1
  tix.date_disabled = func.now()
  session.commit()

  resp = Response( json.dumps(voucher) )
  resp.headers["Content-Type"]="application/json"
  return resp
