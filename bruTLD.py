#!/bin/python3
# brute force TLDs for a domain of choice
import asyncio
import itertools
import string
import sys



length = 2
domain = sys.argv[1]
port = sys.argv[2]

combos = itertools.product(string.ascii_lowercase, repeat=length)
urls = [f"{domain}.{''.join(tld)}" for tld in combos]


async def check_tld(url, port):
    try:
        sock = await asyncio.open_connection(url, port)
        ip = sock[1].get_extra_info('peername')[0]
        print(f"| {url} | {ip} |")
    except OSError:
        pass


async def main(tasks):
    for task in asyncio.as_completed(tasks):
        await task


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide a domain and port as an argument.")
        sys.exit()
    tasks = [check_tld(url, port) for url in urls]
    asyncio.run(main(tasks=tasks))
