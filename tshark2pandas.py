#!/usr/bin/python3

import pandas as pd
import subprocess
import sys


def tshark2pandas(pcap_filename):
    tshark_proc = subprocess.Popen(['tshark', '-r', pcap_filename, '-Tek', '-n'], stdout=subprocess.PIPE)
    grep_proc = subprocess.Popen(['grep', '-v', '_index'], stdin=tshark_proc.stdout, stdout=subprocess.PIPE)
    jq_proc = subprocess.Popen(['jq', '-sc', '.[].layers|flatten|add'], stdin=grep_proc.stdout, stdout=subprocess.PIPE)
    return pd.read_json(jq_proc.stdout, lines=True)


if len(sys.argv) == 1:
    print('need cap')
    sys.exit(0)

for pcap_filename in sys.argv[1:]:
    df = tshark2pandas(pcap_filename)
    print(df)
    print(df.dtypes.to_string())
