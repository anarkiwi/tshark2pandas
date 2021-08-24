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

    def _proc_stdin():
        stdin = None
        if procs:
            stdin = stdin=procs[-1].stdout
        return stdin

    def _add_proc(proc_args, stdout=subprocess.PIPE):
        procs.append(subprocess.Popen(proc_args, stdin=_proc_stdin(), stdout=stdout))

    if snaplen:
        _add_proc(['editcap', '-s', str(snaplen), '-F', 'pcap', pcap_filename, '-'])
        _add_proc(['tshark', '-r', '-'] + TSHARK_ARGS + layer_args)
    else:
        _add_proc(['tshark', '-r', pcap_filename] + TSHARK_ARGS + layer_args)
    _add_proc([os.path.join(os.path.dirname(__file__), 'tshark2pandas_jsonfilter')])
    df = pd.read_json(_proc_stdin(), lines=True)
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
