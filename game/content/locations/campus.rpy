# -*- coding: utf-8 -*-

label location_campus_main:
    scene expression Solid("#1a2636")
    $ actions = []
    $ travels = [
        {"title": "Дом", "key": "home"},
        {"title": "Город", "key": "city"},
        {"title": "Кафе", "key": "cafe"},
        {"title": "Магазин", "key": "store"},
        {"title": "Парк", "key": "park"},
    ]
    $ actions.append({"title": "Посетить пары", "label": "action_campus_study", "tooltip": "-1 время, -15 энергия, -10 сытость, +12 intellect XP"})
    $ actions.append({"title": "Консультация с Игорем", "label": "action_campus_consult", "available": player_stats['energy'] >= 20, "reason": "Нужно ≥20 энергии", "tooltip": "-1 время, -15 энергия, +10 intellect XP, +5 отношения"})
    $ actions.append({"title": "Обсудить проект с Машей", "label": "action_campus_project", "available": player_stats['energy'] >= 10, "reason": "Нужно ≥10 энергии", "tooltip": "-1 время, -10 энергия, +8 discipline XP"})
    call screen sandbox_ui(actions=actions, travels=travels)
    return

label action_campus_study:
    if not spend_period(1):
        jump location_campus_main
    $ change_stat("energy", -15)
    $ change_stat("satiety", -10)
    $ gain_xp("intellect", 12)
    n "Лекции затягиваются, но знания закрепляются."
    $ process_events("campus", "campus_study")
    jump location_campus_main

label action_campus_consult:
    if player_stats["energy"] < 20:
        $ notify("Недостаточно энергии")
        jump location_campus_main
    if not spend_period(1):
        jump location_campus_main
    $ change_stat("energy", -15)
    $ gain_xp("intellect", 10)
    $ relationships["igor"] += 5
    igor "Вот здесь можно упростить расчёты."
    n "Советы Игоря делают материал понятнее."
    $ process_events("campus", "campus_consult")
    jump location_campus_main

label action_campus_project:
    if player_stats["energy"] < 10:
        $ notify("Недостаточно энергии")
        jump location_campus_main
    if not spend_period(1):
        jump location_campus_main
    $ change_stat("energy", -10)
    $ gain_xp("discipline", 8)
    masha "Нужна помощь с презентацией, успеем?"
    n "Маша доверяет Насте важные слайды."
    $ flags["project_draft"] = True
    $ process_events("campus", "campus_project")
    jump location_campus_main
