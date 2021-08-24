# tshark2pandas
tshark2pandas

This (soon to be) small library, allows pandas to directly ingest JSON from tshark (skipping the more typical pyshark intermediate step).

pyshark has a lot of features and is useful for relatively small numbers of packets. But for analyzing attributes of a large number of packets,
a framework like pandas is a better fit. However tshark and pandas don't quite meet in the middle - tshark2pandas does the inconvenient
and messy intermediate work of translating tshark's Elasticsearch export format, into JSON that pandas can easily import.


```
>>> import pandas as pd
>>> import tshark2pandas
>>> df = tshark2pandas.tshark2pandas('/home/josh/tmp/x.cap')
>>> df['frame_frame_len'].quantile(0.75)
1392.0
>>> df['frame_frame_len'].mean()
863.077
```

```
$ /usr/bin/time -v ./tshark2pandas.py ~/tmp/test.cap
        frame_frame_encap_type                 frame_frame_time  frame_frame_offset_shift  frame_frame_time_epoch  frame_frame_time_delta  frame_frame_time_delta_displayed  frame_frame_time_relative  frame_frame_number  ...       ip_ip_src                      ip_ip_addr  ip_ip_src_host                      ip_ip_host        ip_ip_dst   ip_ip_dst_host filtered  eth_eth_padding
0                            1 2021-07-28 00:43:41.264531+00:00                         0            1.627433e+09                0.000000                          0.000000                   0.000000                   1  ...   142.250.71.78    [142.250.71.78, 192.168.2.2]   142.250.71.78    [142.250.71.78, 192.168.2.2]      192.168.2.2      192.168.2.2     data              NaN
1                            1 2021-07-28 00:43:41.291350+00:00                         0            1.627433e+09                0.026819                          0.026819                   0.026819                   2  ...   142.250.71.78    [142.250.71.78, 192.168.2.2]   142.250.71.78    [142.250.71.78, 192.168.2.2]      192.168.2.2      192.168.2.2     data              NaN
2                            1 2021-07-28 00:43:41.492988+00:00                         0            1.627433e+09                0.201638                          0.201638                   0.228457                   3  ...     192.168.2.2    [192.168.2.2, 142.250.71.78]     192.168.2.2    [192.168.2.2, 142.250.71.78]    142.250.71.78    142.250.71.78     data              NaN
3                            1 2021-07-28 00:43:41.571585+00:00                         0            1.627433e+09                0.078597                          0.078597                   0.307054                   4  ...   142.250.71.78    [142.250.71.78, 192.168.2.2]   142.250.71.78    [142.250.71.78, 192.168.2.2]      192.168.2.2      192.168.2.2     data              NaN
4                            1 2021-07-28 00:43:41.794021+00:00                         0            1.627433e+09                0.222436                          0.222436                   0.529490                   5  ...     192.168.2.2   [192.168.2.2, 142.250.66.202]     192.168.2.2   [192.168.2.2, 142.250.66.202]   142.250.66.202   142.250.66.202     data              NaN
...                        ...                              ...                       ...                     ...                     ...                               ...                        ...                 ...  ...             ...                             ...             ...                             ...              ...              ...      ...              ...
299538                       1 2021-07-28 00:44:40.155184+00:00                         0            1.627433e+09                0.016521                          0.016521                  58.890653              299539  ...     192.168.2.2   [192.168.2.2, 142.250.66.202]     192.168.2.2   [192.168.2.2, 142.250.66.202]   142.250.66.202   142.250.66.202     data              NaN
299539                       1 2021-07-28 00:44:40.212098+00:00                         0            1.627433e+09                0.056914                          0.056914                  58.947567              299540  ...   142.250.71.78    [142.250.71.78, 192.168.2.2]   142.250.71.78    [142.250.71.78, 192.168.2.2]      192.168.2.2      192.168.2.2     data              NaN
299540                       1 2021-07-28 00:44:40.213003+00:00                         0            1.627433e+09                0.000905                          0.000905                  58.948472              299541  ...  142.250.66.202   [142.250.66.202, 192.168.2.2]  142.250.66.202   [142.250.66.202, 192.168.2.2]      192.168.2.2      192.168.2.2     data              NaN
299541                       1 2021-07-28 00:44:40.218458+00:00                         0            1.627433e+09                0.005455                          0.005455                  58.953927              299542  ...     192.168.2.2  [192.168.2.2, 172.217.194.189]     192.168.2.2  [192.168.2.2, 172.217.194.189]  172.217.194.189  172.217.194.189     data              NaN
299542                       1 2021-07-28 00:44:40.246191+00:00                         0            1.627433e+09                0.027733                          0.027733                  58.981660              299543  ...  142.250.66.202   [142.250.66.202, 192.168.2.2]  142.250.66.202   [142.250.66.202, 192.168.2.2]      192.168.2.2      192.168.2.2     data              NaN

[299543 rows x 56 columns]
frame_frame_encap_type                            int64
frame_frame_time                    datetime64[ns, UTC]
frame_frame_offset_shift                          int64
frame_frame_time_epoch                          float64
frame_frame_time_delta                          float64
frame_frame_time_delta_displayed                float64
frame_frame_time_relative                       float64
frame_frame_number                                int64
frame_frame_len                                   int64
frame_frame_cap_len                               int64
frame_frame_marked                                 bool
frame_frame_ignored                                bool
frame_frame_protocols                            object
eth_eth_dst                                      object
eth_eth_dst_resolved                             object
eth_eth_dst_oui                                   int64
eth_eth_dst_oui_resolved                         object
eth_eth_addr                                     object
eth_eth_addr_resolved                            object
eth_eth_addr_oui                                  int64
eth_eth_addr_oui_resolved                        object
eth_eth_dst_lg                                     bool
eth_eth_lg                                         bool
eth_eth_dst_ig                                     bool
eth_eth_ig                                         bool
eth_eth_src                                      object
eth_eth_src_resolved                             object
eth_eth_src_oui                                   int64
eth_eth_src_oui_resolved                         object
eth_eth_src_lg                                     bool
eth_eth_src_ig                                     bool
eth_eth_type                                     object
ip_ip_version                                   float64
ip_ip_hdr_len                                   float64
ip_ip_dsfield                                    object
ip_ip_dsfield_dscp                              float64
ip_ip_dsfield_ecn                               float64
ip_ip_len                                       float64
ip_ip_id                                         object
ip_ip_flags                                      object
ip_ip_flags_rb                                  float64
ip_ip_flags_df                                  float64
ip_ip_flags_mf                                  float64
ip_ip_frag_offset                               float64
ip_ip_ttl                                       float64
ip_ip_proto                                     float64
ip_ip_checksum                                   object
ip_ip_checksum_status                           float64
ip_ip_src                                        object
ip_ip_addr                                       object
ip_ip_src_host                                   object
ip_ip_host                                       object
ip_ip_dst                                        object
ip_ip_dst_host                                   object
filtered                                         object
eth_eth_padding                                  object
        Command being timed: "./tshark2pandas.py /home/josh/tmp/test.cap"
        User time (seconds): 70.21
        System time (seconds): 5.57
        Percent of CPU this job got: 121%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 1:02.61
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 4834440
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 2368829
        Voluntary context switches: 430644
        Involuntary context switches: 1706
        Swaps: 0
        File system inputs: 0
        File system outputs: 0
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
```
