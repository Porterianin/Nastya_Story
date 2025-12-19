# -*- coding: utf-8 -*-

# Здесь можно размещать общие функции для действий.
init python:
    def action_effects(costs=None, rewards=None, skills=None):
        costs = costs or {}
        rewards = rewards or {}
        skills = skills or {}
        for stat, delta in costs.items():
            change_stat(stat, delta)
        for skill, xp in skills.items():
            gain_xp(skill, xp)
        if "money" in rewards:
            add_money(rewards["money"])
