#!/usr/bin/python3

import sys
from tshark2pandas import tshark2pandas


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
