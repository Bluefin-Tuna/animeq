from typing import List
from collections import defaultdict
import re

def process_name(name: str) -> str:
    return str(name)

def process_summary(sum: str) -> str:
    return str(sum)

def process_information(info: List[tuple]) -> dict:
    return info

def process_statistics(stat: List[tuple]):
    
    if(re.search(r"[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+", stat[0][1]) is not None ):
        sc = re.findall(r"[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+", stat[0][1])
        sc = [n.replace(",", "") for n in sc]
        sc[0] = float(sc[0])
        sc[1] = int(sc[1])

    else:
        sc = [None, None]
    
    return stat

def process_reviews(tag: List[str], pop: List[str]):
    return tag, pop

def process_relations(rels = List[tuple]):
    return rels