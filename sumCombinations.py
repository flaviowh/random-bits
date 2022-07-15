from itertools import combinations

def closest_sum(nums, target, tolerance=10, rate=0.01, accept_larger=True, accept_smaller=True):

    def itersum(nums, tg):
        res = []
        for idx in range(0, len(nums)+1):
            for subset in combinations(nums, idx):
                if sum(subset) == tg:
                    res.append(subset)
        return res

    spot_on = itersum(nums, target)
    if spot_on:
        return {target: spot_on}
    
    space = round((tolerance / rate ))

    if accept_smaller:
        new_tg = target
        for _ in range(space):
            new_tg -= rate
            new_tg = round(new_tg, 2)
            seq = itersum(nums, new_tg)
            if seq:
                return {new_tg: seq}
    if accept_larger:        
        new_tg = target
        for _ in range(space):
            new_tg += rate
            new_tg = round(new_tg, 2)
            seq = itersum(nums, new_tg)
            if seq:
                return {new_tg: seq}    

    return False