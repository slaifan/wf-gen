
from collections import defaultdict
import csv
import random
from socket import socket
from time import sleep

import aiohttp
import asyncio

top_level_domains = ['gov', 'com', 'org', 'edu', 'net']
input_file = 'top-1m.csv'
output_file = 'quic-enabled'
batch_size = 250
domains = []
h3_enabled_domains = set()
start_batch = 517

async def fetch(session, url):
    rand = random.random()
    sleep(rand / 10)
    try: 
        async with session.get(url) as response:
            try:
                if response.status > 299:
                    return (f'status:{response.status} , {url}', 3)
                if 'Alt-Svc' not in response.headers:
                    return (url, 2)
                for protocol in response.headers['Alt-Svc'].split():
                    if 'h3' in protocol or 'quic' in protocol:
                        return (url,1)
                    else:
                        return (url, 2)
                return (url, 9)
            except Exception as e:
                formatted_err = repr(e)
                return (f'{url} {formatted_err}', 4)
    except Exception as e:
        formatted_err = repr(e)
        return (f'{url} {formatted_err}', 5)

async def fetch_all(urls, loop):
    sem = asyncio.Semaphore(batch_size)
    async with sem:
        async with aiohttp.ClientSession(loop=loop) as session:
            results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=False)
            return results



with open('country_codes.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        top_level_domains.append(row[1])

def group_top_level(domains):
    res = defaultdict(list)
    out = []
    for domain in domains:
        dom_parts = domain.split('.')
        res[dom_parts[0]] += dom_parts[1:]
    for dom, ext in res.items():
        for top_lvl in top_level_domains:
            if top_lvl in ext:
                out.append(f'https://www.{dom}.{top_lvl}')
                break
    return out


with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        domains.append(row[1])

final_urls = group_top_level(domains)
print(f'after filtering, we have a total of {len(final_urls)} urls')

for batch_id in range(start_batch, len(domains) // batch_size):
    batch_first = batch_id * batch_size
    batch_urls = final_urls[batch_first: batch_first + batch_size]

    print(f'batch {batch_id} begins')
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()

    output = loop.run_until_complete(fetch_all(batch_urls, loop))
    out_dict = defaultdict(list)
    for url, status in output:
        out_dict[status].append(url)

    for i, urls in out_dict.items():
        print(i, len(urls))
        with open(f'output/status-{i}-{output_file}.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for i, url in enumerate(urls):
                writer.writerow([(batch_size * batch_id) + i, f'{url}'])




