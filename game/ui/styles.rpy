# -*- coding: utf-8 -*-

init python:
    UI_COLORS = {
        "bg": "#0f111a",
        "panel": "#161a2d",
        "accent": "#8ad0ff",
        "text": "#f0f0f0",
        "disabled": "#555a70",
    }

init -1 style default:
    font "DejaVuSans.ttf"
    color UI_COLORS["text"]

style action_button is default:
    background Solid(UI_COLORS["panel"])
    hover_background Solid(UI_COLORS["accent"])
    foreground None
    padding (8, 8)
    xalign 0.0

style action_button_text is default:
    color UI_COLORS["text"]

style disabled_button is action_button:
    background Solid(UI_COLORS["disabled"])

style hud_label is default:
    color UI_COLORS["accent"]
    size 18

style hud_value is default:
    color UI_COLORS["text"]
    size 16
