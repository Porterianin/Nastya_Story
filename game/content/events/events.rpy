# -*- coding: utf-8 -*-

label event_met_kristina:
    kristina "Начнём с простого. Покажи пунктуальность, и я дам тебе шанс."
    $ advance_quest("cafe_intro", "met_kristina")
    return

label event_cafe_training:
    kristina "Отработка движений — залог успеха."
    $ flags["cafe_training_done"] = True
    $ advance_quest("cafe_intro", "cafe_training_done")
    return

label event_cafe_tip:
    n "Гости щедро оставляют чаевые за улыбку и расторопность."
    $ add_money(30)
    return

label event_cafe_party:
    kristina "Есть закрытая вечеринка. Думаю, ты справишься."
    $ flags["party_invite"] = True
    $ advance_quest("cafe_party", "kristina_trust")
    return

label event_project_offer:
    masha "Настя, помоги с проектом? Тебе зачтётся."
    $ flags["project_offer"] = True
    $ advance_quest("campus_project", "project_offer")
    return

label event_project_draft:
    igor "Я посмотрю черновик, ок?"
    $ flags["project_draft"] = True
    $ advance_quest("campus_project", "project_draft")
    return

label event_project_present:
    n "Выступление проходит гладко, аудитория заинтересована."
    $ flags["project_presented"] = True
    $ advance_quest("campus_project", "project_presented")
    return

label event_meet_leon:
    leon "Слышал, ты работаешь быстро. Нужны люди на частные мероприятия."
    $ known_people["leon"] = True
    $ advance_quest("park_leon", "met_leon")
    return

label event_leon_invite:
    leon "Есть закрытая вечеринка на выходных. Вписываешься?"
    $ flags["party_invite"] = True
    $ advance_quest("park_leon", "leon_invite")
    return

label event_tutor_offer:
    masha "У тебя хорошо получается объяснять. Попробуешь репетиторство?"
    $ flags["tutor_first"] = True
    $ advance_quest("tutoring", "tutor_first")
    return
