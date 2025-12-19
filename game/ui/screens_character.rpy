# -*- coding: utf-8 -*-

screen screen_character():
    tag menu
    modal True
    frame:
        style "default"
        background Solid(UI_COLORS["panel"])
        xalign 0.5
        yalign 0.5
        padding 20
        vbox:
            text "Настя" style "hud_label"
            hbox:
                vbox:
                    text "Статы" style "hud_label"
                    for k, v in player_stats.items():
                        text f"{k}: {v}" style "hud_value"
                vbox:
                    text "Навыки" style "hud_label"
                    for k, data in player_skills.items():
                        $ lvl = get_skill_level(k)
                        text f"{k}: ур. {lvl} (xp {data['xp']})" style "hud_value"
                vbox:
                    text "Отношения" style "hud_label"
                    for k, rel in relationships.items():
                        text f"{k}: {rel}" style "hud_value"
            textbutton "Закрыть" action Hide("screen_character")
