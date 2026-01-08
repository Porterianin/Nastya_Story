# -*- coding: utf-8 -*-

label location_store_main:
    scene expression Solid("#2d2a1f")
    $ actions = []
    $ travels = [
        {"title": "Дом", "key": "home"},
        {"title": "Город", "key": "city"},
        {"title": "Институт", "key": "campus"},
        {"title": "Кафе", "key": "cafe"},
        {"title": "Парк", "key": "park"},
    ]
    $ actions.append({"title": "Купить еду (40₽)", "label": "action_store_food", "available": money >= 40, "reason": "Нужно 40₽", "tooltip": "-1 время, -40₽, +30 сытость"})
    $ actions.append({"title": "Купить косметику (60₽)", "label": "action_store_cosmetics", "available": money >= 60, "reason": "Нужно 60₽", "tooltip": "-1 время, -60₽, +10 charm XP, +10 настроение"})
    $ actions.append({"title": "Примерить одежду (50₽)", "label": "action_store_clothes", "available": money >= 50, "reason": "Нужно 50₽", "tooltip": "-1 время, -50₽, +8 mood, +8 charm XP"})
    call screen sandbox_ui(actions=actions, travels=travels)
    return

label action_store_food:
    if not money >= 40:
        $ notify("Нужно 40₽")
        jump location_store_main
    if not spend_period(1):
        jump location_store_main
    $ try_spend(40)
    $ change_stat("satiety", 30)
    n "Пакеты с едой наполняют холодильник."
    $ process_events("store", "store_food")
    jump location_store_main

label action_store_cosmetics:
    if not money >= 60:
        $ notify("Нужно 60₽")
        jump location_store_main
    if not spend_period(1):
        jump location_store_main
    $ try_spend(60)
    $ change_stat("mood", 10)
    $ gain_xp("charm", 10)
    n "Новая косметика поднимает настроение."
    $ process_events("store", "store_cosmetics")
    jump location_store_main

label action_store_clothes:
    if not money >= 50:
        $ notify("Нужно 50₽")
        jump location_store_main
    if not spend_period(1):
        jump location_store_main
    $ try_spend(50)
    $ change_stat("mood", 8)
    $ gain_xp("charm", 8)
    n "Обновка подчёркивает стиль Насти."
    $ process_events("store", "store_clothes")
    jump location_store_main
