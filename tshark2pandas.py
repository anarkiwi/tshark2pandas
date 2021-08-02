#!/usr/bin/python3

import pandas as pd
import subprocess
import sys

def tshark2pandas(pcap_filename, layers=None, snaplen=256):
    if layers is None:
       layers = ['eth', 'ip', 'frame']
    layer_args = []
    if layers:
        layer_args = ['-J', ' '.join(layers)]
    if not snaplen:
        tshark_proc = subprocess.Popen(['tshark', '-r', pcap_filename, '-Tek', '-n'] + layer_args, stdout=subprocess.PIPE)
    else:
        editcap_proc = subprocess.Popen(['editcap', '-s', str(snaplen), '-F', 'pcap', pcap_filename, '-'], stdout=subprocess.PIPE)
        tshark_proc = subprocess.Popen(['tshark', '-r', '-', '-Tek', '-n'] + layer_args, stdin=editcap_proc.stdout, stdout=subprocess.PIPE)
    grep_proc = subprocess.Popen(['grep', '-v', '_index'], stdin=tshark_proc.stdout, stdout=subprocess.PIPE)
    # jq_proc = subprocess.Popen(['jq', '-nc', '--stream', 'fromstream(1|truncate_stream(inputs))|flatten|add'], stdin=grep_proc.stdout, stdout=subprocess.PIPE)
    jq_proc = subprocess.Popen(['jq', '-c', '-s', 'def map_values(f): with_entries(.value = (.value|f)); .[].layers|flatten|add|del(.filtered)|map_values(tonumber? // .)'], stdin=grep_proc.stdout, stdout=subprocess.PIPE)
    return pd.read_json(jq_proc.stdout, lines=True)


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
