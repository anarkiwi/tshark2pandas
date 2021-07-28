# tshark2pandas
tshark2pandas

This (soon to be) small library, allows pandas to directly ingest JSON from tshark (skipping the more typical pyshark intermediate step).

```
$ ./tshark2pandas.py ~/tmp/x.cap
     frame_frame_encap_type  ... tls_tls_handshake_extensions_psk_binders
0                         1  ...                                      NaN
1                         1  ...                                      NaN
2                         1  ...                                      NaN
3                         1  ...                                      NaN
4                         1  ...                                      NaN
..                      ...  ...                                      ...
995                       1  ...                                      NaN
996                       1  ...                                      NaN
997                       1  ...                                      NaN
998                       1  ...                                      NaN
999                       1  ...                                      NaN

[1000 rows x 224 columns]
frame_frame_encap_type                                                           int64
frame_frame_time                                                   datetime64[ns, UTC]
frame_frame_offset_shift                                                         int64
frame_frame_time_epoch                                                         float64
frame_frame_time_delta                                                         float64
frame_frame_time_delta_displayed                                               float64
frame_frame_time_relative                                                      float64
frame_frame_number                                                               int64
frame_frame_len                                                                  int64
frame_frame_cap_len                                                              int64
frame_frame_marked                                                                bool
frame_frame_ignored                                                               bool
frame_frame_protocols                                                           object
eth_eth_dst                                                                     object
eth_eth_dst_resolved                                                            object
eth_eth_dst_oui                                                                  int64
eth_eth_dst_oui_resolved                                                        object
eth_eth_addr                                                                    object
eth_eth_addr_resolved                                                           object
eth_eth_addr_oui                                                                 int64
eth_eth_addr_oui_resolved                                                       object
eth_eth_dst_lg                                                                    bool
eth_eth_lg                                                                        bool
eth_eth_dst_ig                                                                    bool
eth_eth_ig                                                                        bool
eth_eth_src                                                                     object
eth_eth_src_resolved                                                            object
eth_eth_src_oui                                                                  int64
eth_eth_src_oui_resolved                                                        object
eth_eth_src_lg                                                                    bool
eth_eth_src_ig                                                                    bool
eth_eth_type                                                                    object
ip_ip_version                                                                    int64
ip_ip_hdr_len                                                                    int64
ip_ip_dsfield                                                                   object
ip_ip_dsfield_dscp                                                               int64
ip_ip_dsfield_ecn                                                                int64
ip_ip_len                                                                        int64
ip_ip_id                                                                        object
ip_ip_flags                                                                     object
ip_ip_flags_rb                                                                    bool
ip_ip_flags_df                                                                    bool
ip_ip_flags_mf                                                                    bool
ip_ip_frag_offset                                                                int64
ip_ip_ttl                                                                        int64
ip_ip_proto                                                                      int64
ip_ip_checksum                                                                  object
ip_ip_checksum_status                                                            int64
ip_ip_src                                                                       object
ip_ip_addr                                                                      object
ip_ip_src_host                                                                  object
ip_ip_host                                                                      object
ip_ip_dst                                                                       object
ip_ip_dst_host                                                                  object
udp_udp_srcport                                                                float64
udp_udp_dstport                                                                float64
udp_udp_port                                                                    object
udp_udp_length                                                                 float64
udp_udp_checksum                                                                object
udp_udp_checksum_status                                                        float64
udp_udp_stream                                                                 float64
text                                                                            object
udp_udp_time_relative                                                          float64
udp_udp_time_delta                                                             float64
data_data_data                                                                  object
data_data_len                                                                  float64
tcp_tcp_srcport                                                                float64
tcp_tcp_dstport                                                                float64
tcp_tcp_port                                                                    object
tcp_tcp_stream                                                                 float64
tcp_tcp_len                                                                    float64
tcp_tcp_seq                                                                    float64
tcp_tcp_seq_raw                                                                float64
tcp_tcp_nxtseq                                                                 float64
tcp_tcp_ack                                                                    float64
tcp_tcp_ack_raw                                                                float64
tcp_tcp_hdr_len                                                                float64
tcp_tcp_flags                                                                   object
tcp_tcp_flags_res                                                              float64
tcp_tcp_flags_ns                                                               float64
tcp_tcp_flags_cwr                                                              float64
tcp_tcp_flags_ecn                                                              float64
tcp_tcp_flags_urg                                                              float64
tcp_tcp_flags_ack                                                              float64
tcp_tcp_flags_push                                                             float64
tcp_tcp_flags_reset                                                            float64
tcp_tcp_flags_syn                                                              float64
tcp_tcp_flags_fin                                                              float64
tcp_tcp_flags_str                                                               object
tcp_tcp_window_size_value                                                      float64
tcp_tcp_window_size                                                            float64
tcp_tcp_window_size_scalefactor                                                float64
tcp_tcp_checksum                                                                object
_ws_expert                                                                      object
tcp_tcp_checksum_status                                                        float64
tcp_tcp_checksum_calculated                                                     object
tcp_tcp_urgent_pointer                                                         float64
tcp_tcp_options                                                                 object
tcp_options_nop                                                                 object
tcp_tcp_option_kind                                                            float64
tcp_options_timestamp                                                           object
tcp_tcp_option_len                                                             float64
tcp_tcp_options_timestamp_tsval                                                float64
tcp_tcp_options_timestamp_tsecr                                                float64
tcp_tcp_time_relative                                                          float64
tcp_tcp_time_delta                                                             float64
tcp_tcp_analysis                                                               float64
tcp_tcp_analysis_flags                                                         float64
tcp_options_mss                                                                 object
tcp_tcp_options_mss_val                                                        float64
tcp_options_sack_perm                                                           object
tcp_options_wscale                                                              object
tcp_tcp_options_wscale_shift                                                   float64
tcp_tcp_options_wscale_multiplier                                              float64
eth_eth_padding                                                                 object
tcp_tcp_analysis_acks_frame                                                    float64
tcp_tcp_analysis_ack_rtt                                                       float64
tcp_tcp_analysis_initial_rtt                                                   float64
tcp_tcp_analysis_bytes_in_flight                                               float64
tcp_tcp_analysis_push_bytes_sent                                               float64
tcp_tcp_payload                                                                 object
tls_tls_record                                                                  object
tls_tls_record_content_type                                                     object
tls_tls_record_version                                                          object
tls_tls_record_length                                                           object
tls_tls_handshake                                                              float64
tls_tls_handshake_type                                                         float64
tls_tls_handshake_length                                                       float64
tls_tls_handshake_version                                                       object
tls_tls_handshake_random                                                        object
tls_tls_handshake_random_time                                      datetime64[ns, UTC]
tls_tls_handshake_random_bytes                                                  object
tls_tls_handshake_session_id_length                                            float64
tls_tls_handshake_session_id                                                    object
tls_tls_handshake_cipher_suites_length                                         float64
tls_tls_handshake_ciphersuites                                                 float64
tls_tls_handshake_ciphersuite                                                   object
tls_tls_handshake_comp_methods_length                                          float64
tls_tls_handshake_comp_methods                                                 float64
tls_tls_handshake_comp_method                                                  float64
tls_tls_handshake_extensions_length                                            float64
tls_tls_handshake_extension_type                                                object
tls_tls_handshake_extension_len                                                 object
tls_tls_handshake_extension_data                                                object
tls_tls_handshake_extensions_server_name_list_len                              float64
tls_tls_handshake_extensions_server_name_type                                  float64
tls_tls_handshake_extensions_server_name_len                                   float64
tls_tls_handshake_extensions_server_name                                        object
tls_tls_handshake_extensions_reneg_info_len                                    float64
tls_tls_handshake_extensions_supported_groups_length                           float64
tls_tls_handshake_extensions_supported_groups                                  float64
tls_tls_handshake_extensions_supported_group                                    object
tls_tls_handshake_extensions_ec_point_formats_length                           float64
tls_tls_handshake_extensions_ec_point_formats                                  float64
tls_tls_handshake_extensions_ec_point_format                                   float64
tls_tls_handshake_extensions_alpn_len                                          float64
tls_tls_handshake_extensions_alpn_list                                         float64
tls_tls_handshake_extensions_alpn_str_len                                       object
tls_tls_handshake_extensions_alpn_str                                           object
tls_tls_handshake_extensions_status_request_type                               float64
tls_tls_handshake_extensions_status_request_responder_ids_len                  float64
tls_tls_handshake_extensions_status_request_exts_len                           float64
tls_tls_handshake_sig_hash_alg_len                                             float64
tls_tls_handshake_sig_hash_algs                                                float64
tls_tls_handshake_sig_hash_alg                                                  object
tls_tls_handshake_sig_hash_hash                                                 object
tls_tls_handshake_sig_hash_sig                                                  object
tls_tls_handshake_extensions_key_share_client_length                           float64
tls_tls_handshake_extensions_key_share_group                                    object
tls_tls_handshake_extensions_key_share_key_exchange_length                      object
tls_tls_handshake_extensions_key_share_key_exchange                             object
tls_tls_extension_psk_ke_modes_length                                          float64
tls_tls_extension_psk_ke_mode                                                  float64
tls_tls_handshake_extensions_supported_versions_len                            float64
tls_tls_handshake_extensions_supported_version                                  object
tls_tls_compress_certificate_algorithms_length                                 float64
tls_tls_compress_certificate_algorithm                                         float64
tls_tls_handshake_extensions_padding_data                                       object
tcp_tcp_segment_data                                                            object
tls_tls_change_cipher_spec                                                     float64
tls_tls_record_opaque_type                                                     float64
tls_tls_app_data                                                                object
dns_dns_id                                                                      object
dns_dns_flags                                                                   object
dns_dns_flags_response                                                         float64
dns_dns_flags_opcode                                                           float64
dns_dns_flags_truncated                                                        float64
dns_dns_flags_recdesired                                                       float64
dns_dns_flags_z                                                                float64
dns_dns_flags_checkdisable                                                     float64
dns_dns_count_queries                                                          float64
dns_dns_count_answers                                                          float64
dns_dns_count_auth_rr                                                          float64
dns_dns_count_add_rr                                                           float64
dns_dns_qry_name                                                                object
dns_dns_qry_name_len                                                           float64
dns_dns_count_labels                                                           float64
dns_dns_qry_type                                                               float64
dns_dns_qry_class                                                               object
dns_dns_resp_name                                                               object
dns_dns_resp_type                                                               object
dns_dns_rr_udp_payload_size                                                    float64
dns_dns_resp_ext_rcode                                                          object
dns_dns_resp_edns0_version                                                     float64
dns_dns_resp_z                                                                  object
dns_dns_resp_z_do                                                              float64
dns_dns_resp_z_reserved                                                         object
dns_dns_resp_len                                                                object
dns_dns_flags_authoritative                                                    float64
dns_dns_flags_recavail                                                         float64
dns_dns_flags_authenticated                                                    float64
dns_dns_flags_rcode                                                            float64
dns_dns_resp_class                                                              object
dns_dns_resp_ttl                                                                object
dns_dns_a                                                                       object
dns_dns_response_to                                                            float64
dns_dns_time                                                            datetime64[ns]
dns_dns_cname                                                                   object
tls_tls_handshake_extensions_psk_identities_length                             float64
tls_tls_handshake_extensions_psk_identity_identity_length                      float64
tls_tls_handshake_extensions_psk_identity_identity                              object
tls_tls_handshake_extensions_psk_identity_obfuscated_ticket_age                float64
tls_tls_handshake_extensions_psk_binders_len                                   float64
tls_tls_handshake_extensions_psk_binders                                       float64

```

