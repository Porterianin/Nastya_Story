# -*- coding: utf-8 -*-

label location_city_main:
    scene expression Solid("#1f2438")
    $ actions = []
    $ travels = [
        {"title": "Дом", "key": "home"},
        {"title": "Институт", "key": "campus"},
        {"title": "Кафе", "key": "cafe"},
        {"title": "Магазин", "key": "store"},
        {"title": "Парк", "key": "park"},
    ]
    $ actions.append({"title": "Прогуляться", "label": "action_city_walk", "tooltip": "-1 время, -5 энергия, +5 настроение"})
    $ actions.append({"title": "Мелкие поручения", "label": "action_city_errands", "available": player_stats['energy'] >= 20, "reason": "Нужно ≥20 энергии", "tooltip": "-1 время, -15 энергия, +40₽"})
    $ actions.append({"title": "Поиск встреч", "label": "action_city_meet", "tooltip": "-1 время, шанс события"})
    $ actions.append({"title": "Репетиторство", "label": "action_city_tutor", "available": flags.get('tutor_first', False) and player_stats['energy'] >= 15, "reason": "Нужно предложение и ≥15 энергии", "tooltip": "-1 время, -15 энергия, +80₽, +10 social XP"})
    $ actions.append({"title": "Закрытая вечеринка", "label": "action_city_party", "available": flags.get('party_invite', False) and player_stats['energy'] >= 25, "reason": "Нужно приглашение и ≥25 энергии", "tooltip": "-1 время, -25 энергия, проверка social/work"})
    call screen sandbox_ui(actions=actions, travels=travels)
    return

label action_city_walk:
    if not spend_period(1):
        jump location_city_main
    $ change_stat("energy", -5)
    $ change_stat("mood", 5)
    n "Прогулка по району помогает проветрить голову."
    $ process_events("city", "city_walk")
    jump location_city_main

label action_city_errands:
    if player_stats["energy"] < 20:
        $ notify("Недостаточно энергии")
        jump location_city_main
    if not spend_period(1):
        jump location_city_main
    $ change_stat("energy", -15)
    $ add_money(40)
    n "Несколько поручений приносят немного наличных."
    $ process_events("city", "city_errands")
    jump location_city_main

label action_city_meet:
    if not spend_period(1):
        jump location_city_main
    $ change_stat("mood", 3)
    n "Настя осматривается в людном месте." 
    $ process_events("city", "city_meet")
    jump location_city_main

label action_city_tutor:
    if not flags.get("tutor_first", False):
        $ notify("Нужно договориться о репетиторстве")
        jump location_city_main
    if player_stats["energy"] < 15:
        $ notify("Недостаточно энергии")
        jump location_city_main
    if not spend_period(1):
        jump location_city_main
    $ change_stat("energy", -15)
    $ add_money(80)
    $ gain_xp("social", 10)
    $ flags["tutor_repeat"] = True
    $ advance_quest("tutoring", "tutor_repeat")
    n "Ученики довольны объяснениями Насти."
    $ process_events("city", "city_tutor")
    jump location_city_main

label action_city_party:
    if not flags.get("party_invite", False):
        $ notify("Нужно приглашение")
        jump location_city_main
    if player_stats["energy"] < 25:
        $ notify("Нужно больше энергии")
        jump location_city_main
    if not spend_period(1):
        jump location_city_main
    $ change_stat("energy", -25)
    $ change_stat("hygiene", -10)
    $ performance = check_skill("social", difficulty=3, modifiers=[get_skill_level("work")])
    if performance == "critical":
        $ add_money(200)
        $ relationships["leon"] += 10
        $ gain_xp("corruption", 8)
        n "Вечеринка проходит на ура, Леон доволен сервисом."
    elif performance == "success":
        $ add_money(140)
        $ relationships["leon"] += 5
        $ gain_xp("corruption", 4)
        n "Настя справляется с задачами и привлекает внимание гостей."
    else:
        $ add_money(60)
        $ relationships["leon"] -= 5
        n "Сложно угодить взыскательной публике."
    $ flags["party_served"] = True
    $ advance_quest("cafe_party", "party_served")
    $ process_events("city", "city_party")
    jump location_city_main
