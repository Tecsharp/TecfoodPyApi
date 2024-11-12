import logging
import os

import requests
import json


class LokiHandler(logging.Handler):
    def __init__(self, url, job):
        super().__init__()
        self.url = url
        self.job = job

    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s - %(message)s'
    )

    def emit(self, record):
        log_entry = self.format(record)
        headers = {'Content-Type': 'application/json'}
        payload = {
            "streams": [
                {
                    "stream": {"job": self.job},
                    "values": [
                        [str(int(record.created * 1e9)), log_entry]
                    ]
                }
            ]
        }
        try:
            requests.post(self.url, data=json.dumps(payload), headers=headers)
        except Exception as e:
            print(f"Error enviando log a Loki: {e}")


loki_handler = LokiHandler(os.getenv('LOKI_HOST'), "tecfoodpy-api")
loki_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
loki_handler.setFormatter(formatter)
