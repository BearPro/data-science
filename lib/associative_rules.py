def _all_items(dataset):
    items = set()
    for tx in dataset:
        for item in tx:
            items.add(item)
    return items

def _significance(support, a_hits, b_hits):
    return support - a_hits / b_hits

def _increment(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

def compute(dataset):
    tx_total = 0
    items = _all_items(dataset)
    rule_hits = {}
    rule_miss = {}
    item_hits = {}
    for tx in dataset:
        tx_total += 1
        for itemA in items:
            if itemA in tx:
                _increment(item_hits, itemA)
            for itemB in items:
                if itemA in tx and itemB in tx:
                    _increment(rule_hits, (itemA, itemB))
                elif itemA in tx:
                    _increment(rule_miss, (itemA, itemB))
                else:
                    if (itemA, itemB) not in rule_hits:
                        rule_miss[(itemA, itemB)] = 0
                    if (itemA, itemB) not in rule_miss:
                        rule_miss[(itemA, itemB)] = 0

    result = { (a, b): { "support": rule_hits[(a, b)]/tx_total, 
                         "confidence": rule_hits[(a, b)]/rule_miss[(a, b)] if rule_miss[(a, b)] != 0 else "INF" } 
        for (a, b) in rule_hits }
    return result