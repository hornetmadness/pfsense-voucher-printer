import config
import logging
import argparse
import sys
import csv
from db import Vouchers, connect_db
from sqlalchemy.orm import sessionmaker

db=connect_db() #establish connection
Session = sessionmaker(bind=db)
session = Session()

def importCSV(file, time):
  bulkInsert=[]
  keep={}
  csv.register_dialect('myDialect',
    skipinitialspace=True
  )

  with open(file) as csvfile:
    reader = csv.reader(csvfile, dialect="myDialect")
    for row in reader:
      if row[0].startswith("#"):
        continue

      keep['vid'] = row[0].lstrip(' ')
      keep['time'] = time
      bulkInsert.append(Vouchers(**keep))
  
  if bool(bulkInsert):
    session.bulk_save_objects(bulkInsert)
    session.commit()




if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--debug", help="enable debug output", action="store_true")
  parser.add_argument("--file", help="Provide the path to the CSV", type=str)
  parser.add_argument("--minutes", help="How many minutes are assigned to this roll", type=int)
  args, unknown_args = parser.parse_known_args()    
  
  logging_level = logging.INFO
  
  if args.debug:
    config.debug = True
    config.db_debug = True
    logging_level = logging.DEBUG
    logging.getLogger()
  logging.basicConfig(format='%(asctime)s %(message)s', level=logging_level)
  logging.info("args: {}".format(args))

  if not args.file or not args.minutes:
    logging.error("Both --minutes and --file are requred input for importing")
    sys.exit(1)
  
  importCSV(args.file, args.minutes)