# -*- coding: utf-8 -*-

label location_park_main:
    scene expression Solid("#1c2f26")
    $ actions = []
    $ travels = [
        {"title": "Дом", "key": "home"},
        {"title": "Город", "key": "city"},
        {"title": "Институт", "key": "campus"},
        {"title": "Кафе", "key": "cafe"},
        {"title": "Магазин", "key": "store"},
    ]
    $ actions.append({"title": "Прогулка в парке", "label": "action_park_walk", "tooltip": "-1 время, -5 энергия, +8 настроение"})
    $ actions.append({"title": "Пообщаться", "label": "action_park_social", "available": player_stats['energy'] >= 10, "reason": "Нужно ≥10 энергии", "tooltip": "-1 время, -10 энергия, +8 social XP"})
    $ actions.append({"title": "Помочь Маше с проектом", "label": "action_park_help", "available": flags.get('project_draft', False), "reason": "Нужно начать проект", "tooltip": "-1 время, -10 энергия, +10 discipline XP"})
    call screen sandbox_ui(actions=actions, travels=travels)
    return

label action_park_walk:
    if not spend_period(1):
        jump location_park_main
    $ change_stat("energy", -5)
    $ change_stat("mood", 8)
    n "Парк наполняет тишина и запах хвои."
    $ process_events("park", "park_walk")
    jump location_park_main

label action_park_social:
    if player_stats["energy"] < 10:
        $ notify("Недостаточно энергии")
        jump location_park_main
    if not spend_period(1):
        jump location_park_main
    $ change_stat("energy", -10)
    $ gain_xp("social", 8)
    n "Завязался разговор с незнакомцами."
    $ process_events("park", "park_social")
    jump location_park_main

label action_park_help:
    if not flags.get("project_draft", False):
        $ notify("Сначала начни проект с Машей")
        jump location_park_main
    if not spend_period(1):
        jump location_park_main
    $ change_stat("energy", -10)
    $ gain_xp("discipline", 10)
    masha "Свежий воздух помогает думать."
    $ process_events("park", "park_help")
    jump location_park_main
