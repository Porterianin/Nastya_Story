# -*- coding: utf-8 -*-

screen main_menu():
    tag menu
    add Solid(UI_COLORS["bg"])
    frame:
        xalign 0.5
        yalign 0.5
        background Solid(UI_COLORS["panel"])
        padding 40
        vbox:
            spacing 15
            text "Nastya Story" style "hud_label"
            text "Маленькая сандбокс-история" style "hud_value"
            textbutton _("Начать") action Start()
            textbutton _("Загрузить") action ShowMenu("load")
            textbutton _("Настройки") action ShowMenu("preferences")
            textbutton _("Выход") action Quit(confirm=True)
