def _all_items(dataset):
    items = set()
    for tx in dataset:
        for item in tx:
            items.add(item)
    return items

def _increment(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

def compute(dataset):
    tx_total = 0
    items = _all_items(dataset)
    rule_hits = {}
    item_hits = {}
    for tx in dataset:
        tx_total += 1
        for itemA in items:
            if itemA in tx:
                _increment(item_hits, itemA)
            for itemB in items:
                if itemA != itemB and itemA in tx and itemB in tx:
                    _increment(rule_hits, (itemA, itemB))

    result = { (a, b): { "support":      rule_hits[(a, b)] / tx_total, 
                         "confidence":   rule_hits[(a, b)] / item_hits[a],
                         "significance": rule_hits[(a, b)] - (item_hits[a] / tx_total) * (item_hits[b] / tx_total)} 
        for (a, b) in rule_hits }
    return result