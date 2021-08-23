#!/usr/bin/python3

import os
import subprocess
import sys
import pandas as pd

TSHARK_ARGS = ['-Tek', '-n']


def tshark2pandas(pcap_filename, layers=None, snaplen=256):
    if layers is None:
       layers = ['eth', 'ip', 'frame']
    layer_args = []
    if layers:
        layer_args = ['-J', ' '.join(layers)]
    procs = []
    if snaplen:
        procs.append(subprocess.Popen(['editcap', '-s', str(snaplen), '-F', 'pcap', pcap_filename, '-'], stdout=subprocess.PIPE))
        procs.append(subprocess.Popen(['tshark', '-r', '-'] + TSHARK_ARGS + layer_args, stdin=procs[-1].stdout, stdout=subprocess.PIPE))
    else:
        procs.append(subprocess.Popen(['tshark', '-r', pcap_filename] + TSHARK_ARGS + layer_args, stdout=subprocess.PIPE))
    procs.append(subprocess.Popen([os.path.join('.', 'tshark2pandas_jsonfilter')], stdin=procs[-1].stdout, stdout=subprocess.PIPE))
    df = pd.read_json(procs[-1].stdout, lines=True)
    for proc in procs:
        proc.wait()
    return df


def main():
    if len(sys.argv) == 1:
        print('need cap')
        sys.exit(0)

    for pcap_filename in sys.argv[1:]:
        df = tshark2pandas(pcap_filename)
        print(df)
        print(df.dtypes.to_string())
        for r in df.itertuples():
            print(r)
            break


if __name__ == '__main__':
    main()
