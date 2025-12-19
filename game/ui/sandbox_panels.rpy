# -*- coding: utf-8 -*-

screen sandbox_ui(actions=[], travels=[]):
    tag menu
    use hud
    frame background Solid(UI_COLORS["bg"]):
        xfill True
        yfill True
        hbox:
            spacing 20
            frame:
                style "default"
                background Solid(UI_COLORS["panel"])
                xsize 400
                vbox:
                    label "Действия" style "hud_label"
                    for action in actions:
                        $ can_do = action.get("available", True)
                        $ reason = action.get("reason", "")
                        $ tooltip = action.get("tooltip", "")
                        $ target_label = action.get("label")

                        if can_do and target_label:
                            textbutton action.get("title"):
                                action Jump(target_label)
                                tooltip tooltip
                                style "action_button"
                        elif can_do:
                            textbutton action.get("title"):
                                action NullAction()
                                tooltip "Требуется настроить метку действия"
                                style "disabled_button"
                        else:
                            textbutton action.get("title"):
                                action NullAction()
                                tooltip reason
                                style "disabled_button"
            frame:
                background Solid(UI_COLORS["panel"])
                xsize 250
                vbox:
                    label "Перемещения" style "hud_label"
                    for move in travels:
                        $ can_move = unlocked_locations.get(move["key"], False)
                        $ move_tooltip = move.get("tooltip", "")
                        if can_move:
                            textbutton move["title"]:
                                action Function(travel_to, move["key"])
                                tooltip move_tooltip
                                style "action_button"
                        else:
                            textbutton move["title"]:
                                action NullAction()
                                tooltip move_tooltip if move_tooltip else "Локация пока недоступна"
                                style "disabled_button"
            frame:
                background Solid(UI_COLORS["panel"])
                xfill True
                vbox:
                    text "Локация: [move_label(current_location)]" style "hud_label"
                    text "Уведомления" style "hud_label"
                    viewport:
                        draggable True
                        mousewheel True
                        vbox:
                            for note in notifications[-10:]:
                                text note

init python:
    def move_label(key):
        labels = {
            "home": "Дом",
            "city": "Город",
            "campus": "Институт",
            "cafe": "Кафе",
            "store": "Магазин",
            "park": "Парк",
        }
        return labels.get(key, key)
