# -*- coding: utf-8 -*-

label location_cafe_main:
    scene expression Solid("#2a2030")
    $ actions = []
    $ travels = [
        {"title": "Дом", "key": "home"},
        {"title": "Город", "key": "city"},
        {"title": "Институт", "key": "campus"},
        {"title": "Магазин", "key": "store"},
        {"title": "Парк", "key": "park"},
    ]
    $ actions.append({"title": "Познакомиться с Кристиной", "label": "action_cafe_meet", "available": not known_people.get('kristina', False), "reason": "Уже знакомы", "tooltip": "-1 время, открывает работу"})
    $ actions.append({"title": "Стажировка", "label": "action_cafe_train", "available": known_people.get('kristina', False), "reason": "Нужно познакомиться", "tooltip": "-1 время, -15 энергия, +8 work XP"})
    $ shift_unlocked = unlocked_actions.get("cafe_shift", False)
    $ actions.append({"title": "Смена официанткой", "label": "action_cafe_shift", "available": shift_unlocked and player_stats['energy'] >= 20 and player_stats['hygiene'] >= 40, "reason": "Нужно стажировка и ≥20 энергии, ≥40 чистоты", "tooltip": "-1 время, -20 энергия, +10 social XP, +80-120₽"})
    call screen sandbox_ui(actions=actions, travels=travels)
    return

label action_cafe_meet:
    if known_people.get("kristina", False):
        jump location_cafe_main
    if not spend_period(1):
        jump location_cafe_main
    kristina "Ты Настя? Я Кристина, менеджер. Покажи, что умеешь работать."
    $ known_people["kristina"] = True
    $ unlock_location("cafe")
    $ advance_quest("cafe_intro", "met_kristina")
    $ process_events("cafe", "cafe_meet")
    jump location_cafe_main

label action_cafe_train:
    if not known_people.get("kristina", False):
        $ notify("Сначала познакомься с менеджером")
        jump location_cafe_main
    if not spend_period(1):
        jump location_cafe_main
    $ change_stat("energy", -15)
    $ gain_xp("work", 8)
    kristina "Запомни: улыбка и скорость — наши друзья."
    $ unlocked_actions["cafe_shift"] = True
    $ flags["cafe_training_done"] = True
    $ advance_quest("cafe_intro", "cafe_training_done")
    $ process_events("cafe", "cafe_train")
    jump location_cafe_main

label action_cafe_shift:
    if player_stats["energy"] < 20 or player_stats["hygiene"] < 40:
        $ notify("Подготовься: энергия ≥20 и чистота ≥40")
        jump location_cafe_main
    if not spend_period(1):
        jump location_cafe_main
    $ change_stat("energy", -20)
    $ change_stat("mood", -5)
    $ base_tip = 80
    $ performance = check_skill("social", difficulty=2, modifiers=[player_stats['mood']//30])
    if performance == "critical":
        $ reward = base_tip + 50
        $ relationships["kristina"] += 5
    elif performance == "success":
        $ reward = base_tip + 20
        $ relationships["kristina"] += 2
    else:
        $ reward = base_tip - 30
        $ relationships["kristina"] -= 2
    $ add_money(reward)
    $ gain_xp("social", 10)
    $ gain_xp("work", 5)
    kristina "Смена завершена. Посмотрим на отзывы." 
    $ flags["kristina_trust"] = relationships["kristina"] >= 15
    if flags["kristina_trust"]:
        $ advance_quest("cafe_party", "kristina_trust")
    $ process_events("cafe", "cafe_shift")
    jump location_cafe_main
