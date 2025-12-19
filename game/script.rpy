# -*- coding: utf-8 -*-

label start:
    scene expression Solid("#1b1b2b")
    $ notify("Настя возвращается в реальность города.")
    jump location_home_main

label sandbox_loop:
    call screen sandbox_ui
    return

python early:
    def travel_to(location_key):
        if not unlocked_locations.get(location_key, False):
            notify("Локация недоступна")
            return
        store.current_location = location_key
        reduce_cooldowns()
        renpy.jump(f"location_{location_key}_main")
