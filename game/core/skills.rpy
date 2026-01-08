# -*- coding: utf-8 -*-

init python:
    def xp_to_level(xp):
        return math.floor(0.1 * math.sqrt(xp))

    def get_skill_level(name):
        data = player_skills.get(name, {"xp": 0})
        return xp_to_level(data.get("xp", 0))

    def gain_xp(name, base_xp):
        data = player_skills.get(name)
        if data is None:
            return
        level = get_skill_level(name)
        modifier = 1 / (1 + level * 0.25)
        gained = int(base_xp * modifier)
        data["xp"] += max(1, gained)
        notify(f"{name} XP: +{max(1, gained)}")

    def check_skill(name, difficulty=1, modifiers=None):
        mods = modifiers or []
        level = get_skill_level(name)
        score = level + sum(mods)
        if score >= difficulty + 2:
            return "critical"
        elif score >= difficulty:
            return "success"
        else:
            return "fail"
