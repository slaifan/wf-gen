import csv
from re import T
from struct import pack
from typing import Type
from scapy.all import *
import ipaddress

def process_pcap(file_name):
    print('Opening {}...'.format(file_name))

    raw_packets = rdpcap(file_name)
    fst_pkt = raw_packets[0]
    packets = [(i, (pkt.time - fst_pkt.time), len(pkt), convert_src(pkt)) for i, pkt in enumerate(raw_packets) if convert_src(pkt) != 2 and len(pkt) > 100]
    # for i, t, l, dst in packets[:20]:
    #     print(f'packet {i}, time: {t}, length: {l}, to: {dst}')
    return packets

def group_packets(packets):
    prev_time = 0
    times = []
    for i, t, l, dst in packets:
        if dst == 2:
            continue
        times.append((i , t - prev_time))
        prev_time = t
    breakpoints = sorted(times, key=lambda item: item[1], reverse=True)
    
    fst_pkts = sorted([i for i, t in breakpoints if t > 10])
    fst_pkts = [packets[0][0]] + fst_pkts + [packets[-1][0]]
    print(fst_pkts)

    groups = []
    for i in range(len(fst_pkts[:-1])):
        indices = [idx for idx, _, _, _ in packets]
        start_idx = indices.index(fst_pkts[i])
        end_idx = indices.index(fst_pkts[i + 1])
        groups.append(packets[start_idx: end_idx])

    print(len(groups))
    for group in groups:
        print(len(group))
    return groups


def convert_src(pkt):
    try:
        if pkt.dst == '172.16.236.1':
           return 0
        elif pkt.dst == '172.16.236.44':
           return 1
        return 2
    except:
        return 2

def write_session_stats(filename, session):
    with open(filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        total_size = sum([l for i, t, l, dst in session])
        num_packets = len(session)

        num_out_packets = len([l for i, t, l, dst in session if dst == 0])
        ratio_out = num_out_packets / num_packets

        num_in_packets = len([l for i, t, l, dst in session if dst == 1])
        ratio_in = num_in_packets / num_packets

        avg_packet_size = total_size / num_packets

        out = [total_size, num_packets, num_out_packets, num_in_packets, ratio_out, ratio_in, avg_packet_size]
        writer.writerow(out)

for filename in os.listdir('./data'):
    if 'eve' in filename:
        packets = process_pcap(f'./data/{filename}')
        sessions = group_packets(packets)
        for session in sessions:
            write_session_stats(f'./stats/{filename}.csv', session)