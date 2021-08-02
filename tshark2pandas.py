#!/usr/bin/python3

import pandas as pd
import subprocess
import sys

TSHARK_ARGS = ['-Tek', '-n']
#JQ_REMAP_SCRIPT = r'def map_values(f): with_entries(.value = (.value|f)); .[].layers|flatten|add|del(.filtered)|map_values(tonumber? // .)'
#JQ_STREAM_REMAP_SCRIPT = r'fromstream(1|truncate_stream(inputs))|flatten|add'
JQ_REMAP_SCRIPT = r'.[].layers|flatten|add|del(.filtered)'


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
    procs.append(subprocess.Popen(['grep', '-v', '_index'], stdin=procs[-1].stdout, stdout=subprocess.PIPE))
    procs.append(subprocess.Popen(['jq', '-c', '-s', JQ_REMAP_SCRIPT], stdin=procs[-1].stdout, stdout=subprocess.PIPE))
    df = pd.read_json(procs[-1].stdout, lines=True)
    # TODO: ideally, detect and convert hex ints before pandas.
    object_cols = {col for col, col_dtype in df.dtypes.iteritems() if col_dtype == object}
    for col in object_cols:
        # hex strings
        prefixes = df[col].str[:2]
        if prefixes[0] == '0x':
            if prefixes.nunique() == 1:
                df[col] = df[col].fillna('0x0').map(lambda x: int(x, 16)).astype(pd.Int64Dtype())
                continue
        # int strings
        if df[col][(df[col].notna()) & (df[col].str.isdecimal())].size == df[col].size:
            df[col] = df[col].fillna('0').map(int).astype(pd.Int64Dtype())
            continue
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
