import math

def stack_value(base, bonus, stacks, mode):
    """叠层数值。"""
    raise NotImplementedError("TODO: stack_value")

def refresh_remaining(remaining, duration):
    """刷新保留。"""
    raise NotImplementedError("TODO: refresh_remaining")

def dynamic_attr(base, bonus):
    """动态属性。"""
    raise NotImplementedError("TODO: dynamic_attr")

def cap_stacks(stacks, cap):
    """层数上限。"""
    raise NotImplementedError("TODO: cap_stacks")

def dispel_source(entries, source):
    """按来源驱散。"""
    raise NotImplementedError("TODO: dispel_source")

def death_clear(buffs):
    """死亡清理。"""
    raise NotImplementedError("TODO: death_clear")

def tick_damage(stacks, interval):
    """tick 伤害。"""
    raise NotImplementedError("TODO: tick_damage")

def immune_before(immune, stacks):
    """免疫优先。"""
    raise NotImplementedError("TODO: immune_before")

def sync_remaining(remaining, latency):
    """同步剩余时间。"""
    raise NotImplementedError("TODO: sync_remaining")

def instance_id(source, index):
    """实例 id。"""
    raise NotImplementedError("TODO: instance_id")

def at_cap(stacks, cap):
    """到达上限。"""
    raise NotImplementedError("TODO: at_cap")

def add_stack(stacks, count):
    """加层。"""
    raise NotImplementedError("TODO: add_stack")

def remove_stack(stacks, count):
    """减层。"""
    raise NotImplementedError("TODO: remove_stack")

def buff_duration(stacks, per_stack):
    """总持续时间。"""
    raise NotImplementedError("TODO: buff_duration")

def buff_id(seed, index):
    """buff id。"""
    raise NotImplementedError("TODO: buff_id")
