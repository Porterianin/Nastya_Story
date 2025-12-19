# -*- coding: utf-8 -*-

init python:
    STAT_LIMITS = {
        "energy": (0, 100),
        "hygiene": (0, 100),
        "satiety": (0, 100),
        "mood": (0, 100),
        "arousal": (0, 100),
    }

    def clamp_stat(name, value):
        low, high = STAT_LIMITS.get(name, (0, 100))
        return max(low, min(high, value))

    def change_stat(name, delta):
        if name not in player_stats:
            return
        new_val = clamp_stat(name, player_stats[name] + delta)
        player_stats[name] = new_val
        notify(f"{name}: {delta:+}")

    def require_stats(requirements):
        for key, minimum in requirements.items():
            if player_stats.get(key, 0) < minimum:
                return False
        return True

    def apply_costs(costs):
        for key, delta in costs.items():
            change_stat(key, delta)

    def fatigue(delta= -10):
        change_stat("energy", delta)

