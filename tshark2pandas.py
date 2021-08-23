#!/usr/bin/python3

import os
import subprocess
import sys
import pandas as pd


def tshark2pandas(pcap_filename, layers=None):
    if not layers:
       layers = ['eth', 'ip', 'frame']
    layer_args = ['-J', ' '.join(layers)]
    tshark_proc = subprocess.Popen(['tshark', '-r', pcap_filename, '-Tek', '-n'] + layer_args, stdout=subprocess.PIPE)
    filter_proc = subprocess.Popen([os.path.join('.', 'tshark2pandas_jsonfilter')], stdin=tshark_proc.stdout, stdout=subprocess.PIPE)
    return pd.read_json(filter_proc.stdout, lines=True)


def main():
    if len(sys.argv) == 1:
        print('need cap')
        sys.exit(0)

    for pcap_filename in sys.argv[1:]:
        df = tshark2pandas(pcap_filename)
        print(df)
        print(df.dtypes.to_string())


if __name__ == '__main__':
    main()
