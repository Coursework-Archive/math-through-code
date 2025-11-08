from .items import Item

def gen_powerset(items, constraint, get_val, get_weight):
    """Yield all subsets with total weight <= constraint (early pruning)."""
    n = len(items)

    def backtrack(idx, cur_subset, cur_wt):
        if cur_wt > constraint:
            return
        if idx == n:
            yield list(cur_subset)
            return
        # skip
        for s in backtrack(idx + 1, cur_subset, cur_wt):
            yield s
        # take
        it = items[idx]
        cur_subset.append(it)
        for s in backtrack(idx + 1, cur_subset, cur_wt + get_weight(it)):
            yield s
        cur_subset.pop()

    for s in backtrack(0, [], 0.0):
        yield s


def choose_best(pset, max_weight, get_val, get_weight):
    best_val = 0.0
    best_set = []
    for items in pset:
        total_value = 0.0
        total_weight = 0.0
        valid = True
        for it in items:
            total_weight += get_weight(it)
            if total_weight > max_weight:
                valid = False
                break
            total_value += get_val(it)
        if valid and total_value > best_val:
            best_val, best_set = total_value, items
    return best_set, best_val


def test_best(max_weight=20):
    its = build_items()  # noqa: F821 if imported before items
    feasible = list(gen_powerset(its, max_weight, Item.get_value, Item.get_weight))
    best_set = max(feasible, key=lambda S: sum(Item.get_value(x) for x in S))
    best_val = sum(Item.get_value(x) for x in best_set)
    return best_set, best_val

