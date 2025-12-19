# -*- coding: utf-8 -*-

label location_home_main:
    scene expression Solid("#1d1f2f")
    $ actions = []
    $ travels = [
        {"title": "Город", "key": "city"},
        {"title": "Институт", "key": "campus"},
        {"title": "Кафе", "key": "cafe"},
        {"title": "Магазин", "key": "store"},
        {"title": "Парк", "key": "park"},
    ]
    $ actions.append({"title": "Отдохнуть", "label": "action_home_rest", "tooltip": "-1 время, +20 энергия, +5 настроение"})
    $ actions.append({"title": "Душ", "label": "action_home_shower", "tooltip": "-1 время, -5 энергия, +25 чистота"})
    $ cost_snack = 20
    $ actions.append({"title": "Перекус (20₽)", "label": "action_home_snack", "available": money >= cost_snack, "reason": "Нужно 20₽", "tooltip": "-1 время, -20₽, +20 сытость"})
    $ actions.append({"title": "Поговорить с Катей", "label": "action_home_chat", "available": known_people.get("katya", False), "reason": "Нужно познакомиться", "tooltip": "-1 время, +10 настроение, +5 отношения"})
    call screen sandbox_ui(actions=actions, travels=travels)
    return

label action_home_rest:
    if not spend_period(1):
        jump location_home_main
    $ change_stat("energy", 20)
    $ change_stat("mood", 5)
    n "Немного отдыха на диване восстанавливает силы."
    $ process_events("home", "home_rest")
    jump location_home_main

label action_home_shower:
    if not spend_period(1):
        jump location_home_main
    $ change_stat("energy", -5)
    $ change_stat("hygiene", 25)
    n "Горячий душ помогает собраться."
    $ process_events("home", "home_shower")
    jump location_home_main

label action_home_snack:
    if not money >= 20:
        $ notify("Нужно 20₽")
        jump location_home_main
    if not spend_period(1):
        jump location_home_main
    $ try_spend(20)
    $ change_stat("satiety", 20)
    $ change_stat("energy", 5)
    n "Быстрый перекус прогоняет голод."
    $ process_events("home", "home_snack")
    jump location_home_main

label action_home_chat:
    if not spend_period(1):
        jump location_home_main
    $ change_stat("mood", 10)
    $ relationships["katya"] = relationships.get("katya", 0) + 5
    katya "Не забывай отдыхать, Настя."
    n "Катя улыбается и делится историями о соседях."
    $ process_events("home", "home_chat")
    jump location_home_main
