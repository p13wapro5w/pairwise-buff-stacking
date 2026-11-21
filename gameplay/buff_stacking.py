import math


def stack_value(base, bonus, stacks, mode):
    """叠层数值。

    乘区与加区分离：
    - "mul"：每层在当前值上相乘，base * (1 + bonus) ** stacks；
      修复把乘区当加区（五层 1.1 被算成 1.5）的问题。
    - "add"：每层只贡献一次固定加成，base * (1 + bonus * stacks)。
    """
    if mode == "mul":
        return base * (1.0 + bonus) ** stacks
    if mode == "add":
        return base * (1.0 + bonus * stacks)
    raise ValueError(f"unknown stack mode: {mode!r}")


def refresh_remaining(remaining, duration):
    """刷新保留。

    刷新持续时间时保留尚未用完的剩余时间，取剩余时间与新持续时间的较大值，
    而不是把剩余时间清零，避免高层 buff 每次刷新都亏掉剩余的半秒。
    """
    return max(remaining, duration)


def dynamic_attr(base, bonus):
    """动态属性。

    属性在每次求值时实时计算（base + bonus），不在施加 buff 时固化快照，
    之后换装、增减加成都会立即反映到 buff 效果上。
    """
    return base + bonus


def cap_stacks(stacks, cap):
    """层数上限（服务器权威截断）。

    层数上限由服务器裁决：超过 cap 一律截断到 cap，
    客户端显示多少层都以服务器截断后的层数为准。
    """
    return min(stacks, cap)


def dispel_source(entries, source):
    """按来源驱散。

    只移除来自指定 source 的 buff 实例，保留其他来源的同名 buff。
    入参可以是来源标识列表，也可以是带 "source" 键的 buff 实例字典列表。
    """
    result = []
    for entry in entries:
        if isinstance(entry, dict):
            if entry.get("source") != source:
                result.append(entry)
        elif entry != source:
            result.append(entry)
    return result


def death_clear(buffs):
    """死亡清理。

    角色死亡时清空全部 buff（正面与负面一起清），
    避免复活后中毒等负面层数残留。
    """
    return []


def tick_damage(stacks, interval):
    """tick 伤害（按时间驱动）。

    伤害跳数由真实时间决定：单位时间内的 tick 数为 1 / interval，
    总伤害 = stacks / interval，与帧率、帧累加无关。
    """
    if interval <= 0:
        raise ValueError("interval must be positive")
    return stacks / interval


def immune_before(immune, stacks):
    """免疫优先。

    免疫判定先于叠层：目标免疫时直接返回 0 层，buff 根本不会被施加，
    自然不会在施加当帧触发一次伤害；不免疫时层数才正常生效。
    """
    return 0 if immune else stacks


def sync_remaining(remaining, latency):
    """同步剩余时间。

    网络同步同时携带剩余时间，客户端按延迟扣除已流逝的时间，
    并在 0 处截断，保证客户端倒计时与服务器一致而不是固定差两秒。
    """
    return max(0, remaining - latency)


def instance_id(source, index):
    """实例 id。

    每个来源的每次施加都生成独立实例 id（source:index），
    多个来源的同名 buff 不再共用 id，驱散时不会连带清掉别人的 buff。
    """
    return f"{source}:{index}"


def at_cap(stacks, cap):
    """到达上限。"""
    return stacks >= cap


def add_stack(stacks, count):
    """加层。"""
    return stacks + count


def remove_stack(stacks, count):
    """减层（不会减成负数）。"""
    return max(0, stacks - count)


def buff_duration(stacks, per_stack):
    """总持续时间。"""
    return stacks * per_stack


def buff_id(seed, index):
    """buff id。"""
    return f"{seed}:{index}"
