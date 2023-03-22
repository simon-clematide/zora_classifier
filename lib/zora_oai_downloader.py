#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

"""



__appname__ = "[application name here]"
__author__  = "AA"
__version__ = "0.0pre0"
__license__ = "GNU GPL 3.0 or later"
import time
import logging
log = logging.getLogger(__name__)
import sys
from sickle import Sickle
from lxml import etree
import json
from smart_open import open

# Initialise the Sickle client with the base URL of the OAI-PMH server
sickle = Sickle('https://www.zora.uzh.ch/cgi/oai2')



class MainApplication(object):

    def __init__(self, args):
        self.args = args

    def run(self):
        log.info(self.args)
        self.download(self.args.outfile)

    def download(self,filename, limit=999999999):
        # Set metadata prefix and other parameters for the OAI-PMH request
        metadata_prefix = 'oai_dc'
        params = {'metadataPrefix': metadata_prefix,'ignore_deleted':True}
        count = 0
        ignored = 0
        log.info(f"Fetching records...")
        # when looping over the records, sickle automatically loads further pages as long as a resumption token is thereedit
        records = sickle.ListRecords(**params)
        resumption_token = records.resumption_token
        log.info(f"fetched  records")
        with open(filename, "w", encoding="utf-8") as outfile:



            for i,record in enumerate(records):
                if count > limit:
                    break
                log.info(f"WOrking on record {i}")
                try:
                    d_record = dict(record)
                    count += 1
                    print(json.dumps(d_record,ensure_ascii=False), file=outfile)
                except AttributeError:
                    ignored += 1

            log.info(f"# records: {count}")
            log.info(f"# IGNORED records: {ignored}")



if __name__ == '__main__':
    import argparse
    description = ""
    epilog = ""
    parser = argparse.ArgumentParser(description=description, epilog=epilog)
    parser.add_argument('-l', '--logfile', dest='logfile',
                      help='write log to FILE', metavar='FILE')
    parser.add_argument('-v', '--verbose', dest='verbose',default=3,type=int, metavar="LEVEL",
                      help='set verbosity level: 0=CRITICAL, 1=ERROR, 2=WARNING, 3=INFO 4=DEBUG (default %(default)s)')
    parser.add_argument(
        "--outfile",
        metavar="OUTPUT",
        default="zora_oai_output.jsonl.bz2",
        help="Input file (default: STDIN)",
    )

    arguments = parser.parse_args()

    log_levels = [logging.CRITICAL, logging.ERROR, logging.WARNING,
                  logging.INFO, logging.DEBUG]
    logging.basicConfig(level=log_levels[arguments.verbose],
                        format='%(asctime)-15s %(levelname)s: %(message)s')

    # launching application ...
    MainApplication(arguments).run()

