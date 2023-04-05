#!/bin/python3
# brute force TLDs for a domain of choice
import asyncio
import itertools
import string
import sys



length = sys.argv[1]
keyword = sys.argv[2]
port = sys.argv[3]

combos = itertools.product(string.ascii_lowercase, repeat=length)
urls = [f"{keyword}.{''.join(tld)}" for tld in combos]


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
    if len(sys.argv) != 4:
        print("""
            Please provide TLD's length, keyword, and port as arguments.
            
            Example usage: python3 bruTLD.py 3 google 443
        """)
        sys.exit()
    tasks = [check_tld(url, port) for url in urls]
    asyncio.run(main(tasks=tasks))
