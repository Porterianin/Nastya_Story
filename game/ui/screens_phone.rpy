# -*- coding: utf-8 -*-

screen screen_phone():
    tag menu
    modal True
    frame:
        background Solid(UI_COLORS["panel"])
        xalign 0.5
        yalign 0.5
        padding 20
        vbox:
            text "Телефон" style "hud_label"
            text "Последние уведомления" style "hud_label"
            viewport:
                ymaximum 300
                vbox:
                    for note in notifications[-10:]:
                        text note
            textbutton "Закрыть" action Hide("screen_phone")
