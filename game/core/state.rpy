# -*- coding: utf-8 -*-

# Базовые default переменные для состояния игрока и мира.
default current_location = "home"
default current_period = 0
# 4 периода в день как ресурс.
default periods_per_day = 4

default player_stats = {
    "energy": 70,
    "hygiene": 70,
    "satiety": 70,
    "mood": 60,
    "arousal": 10,
}

default player_skills = {
    "social": {"xp": 0},
    "intellect": {"xp": 0},
    "discipline": {"xp": 0},
    "charm": {"xp": 0},
    "work": {"xp": 0},
    "corruption": {"xp": 0},
}

default money = 200

default relationships = {
    "katya": 10,
    "igor": 0,
    "masha": 5,
    "kristina": -5,
    "leon": -10,
}

default known_people = {
    "katya": True,
    "igor": True,
    "masha": True,
    "kristina": False,
    "leon": False,
}

default flags = {
    "party_invite": False,
    "project_offer": False,
    "cafe_training_done": False,
    "project_draft": False,
    "project_presented": False,
    "kristina_trust": False,
    "party_served": False,
    "tutor_first": False,
    "tutor_repeat": False,
}

default unlocked_locations = {
    "home": True,
    "city": True,
    "campus": True,
    "cafe": False,
    "store": True,
    "park": True,
}

default unlocked_actions = {}

default cooldowns = {}

default completed_events = set()

default quest_states = {}

default notifications = []

python early:
    import math
    import renpy.store as store

    def notify(message):
        renpy.notify(message)
        store.notifications.append(message)

