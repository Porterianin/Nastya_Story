# -*- coding: utf-8 -*-

screen hud():
    frame style "default" background Solid(UI_COLORS["panel"]):
        xfill True
        ysize 70
        hbox:
            spacing 20
            text "Время: [current_period]/[periods_per_day]" style "hud_label"
            text "Деньги: [money]" style "hud_label"
            text "Энергия: [player_stats['energy']]" style "hud_value"
            text "Настроение: [player_stats['mood']]" style "hud_value"
            text "Сытость: [player_stats['satiety']]" style "hud_value"
            textbutton "Персонаж" action Show("screen_character")
            textbutton "Телефон" action Show("screen_phone")
            textbutton "Инвентарь" action NullAction()
