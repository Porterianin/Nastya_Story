# -*- coding: utf-8 -*-

init python:
    unlock_rules = {
        "cafe": lambda: known_people.get("kristina", False),
        "cafe_shift": lambda: unlocked_actions.get("cafe_shift", False),
        "party": lambda: flags.get("party_invite", False),
    }

    def is_unlocked(key):
        rule = unlock_rules.get(key)
        if not rule:
            return True
        return rule()

    def unlock_location(key):
        unlocked_locations[key] = True

    def unlock_action(key):
        unlocked_actions[key] = True
