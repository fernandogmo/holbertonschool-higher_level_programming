#!/usr/bin/python3
def best_score(d):
    return max(d, key=d.get) if d else None
