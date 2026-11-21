import pytest
import math
from gameplay import buff_stacking as mod

CASES = [
    ("mul", "m.stack_value(100, 0.1, 2, 'mul') == approx(121.0)"),
    ("refresh", 'm.refresh_remaining(1, 5) == 5'),
    ("attr", 'm.dynamic_attr(10, 2) == 12'),
    ("cap", 'm.cap_stacks(6, 5) == 5'),
    ("dispel", "m.dispel_source(['a', 'b'], 'a') == ['b']"),
    ("death", "m.death_clear(['x']) == []"),
    ("tick", 'm.tick_damage(3, 0.5) == approx(6.0)'),
    ("immune", 'm.immune_before(True, 3) == 0'),
    ("sync", 'm.sync_remaining(5, 2) == 3'),
    ("inst", "m.instance_id('src', 2) == 'src:2'"),
    ("atcap", 'm.at_cap(5, 5) is True'),
    ("add", 'm.add_stack(1, 1) == 2'),
    ("remove", 'm.remove_stack(3, 1) == 2'),
    ("dur", 'm.buff_duration(3, 2) == 6'),
    ("id", 'm.buff_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
