# -*- coding: utf-8 -*-

init python:
    events_registry = [
        {"id": "met_kristina", "label": "event_met_kristina", "trigger": {"location": "cafe", "action": "cafe_meet"}, "once": True},
        {"id": "cafe_training", "label": "event_cafe_training", "trigger": {"location": "cafe", "action": "cafe_train"}, "once": True},
        {"id": "cafe_shift_tip", "label": "event_cafe_tip", "trigger": {"location": "cafe", "action": "cafe_shift", "skill": ("social", 2)}, "cooldown": 2},
        {"id": "cafe_party_invite", "label": "event_cafe_party", "trigger": {"location": "cafe", "action": "cafe_shift", "flags": ["party_invite"]}, "once": True},
        {"id": "campus_project_offer", "label": "event_project_offer", "trigger": {"location": "campus", "action": "campus_study", "skill": ("intellect", 2)}, "once": True},
        {"id": "project_draft", "label": "event_project_draft", "trigger": {"location": "campus", "action": "campus_project"}},
        {"id": "project_presentation", "label": "event_project_present", "trigger": {"location": "campus", "action": "campus_project", "flags": ["project_draft"]}, "once": True},
        {"id": "meet_leon", "label": "event_meet_leon", "trigger": {"location": "park", "action": "park_social", "skill": ("social", 1)}, "once": True},
        {"id": "leon_invite", "label": "event_leon_invite", "trigger": {"location": "park", "action": "park_social", "flags": ["party_invite"]}, "once": True},
        {"id": "tutor_offer", "label": "event_tutor_offer", "trigger": {"location": "campus", "action": "campus_consult", "skill": ("discipline", 2)}, "once": True},
    ]

    def reduce_cooldowns():
        for key in list(cooldowns.keys()):
            cooldowns[key] = max(0, cooldowns[key] - 1)

    def event_matches(event, location=None, action=None):
        trigger = event.get("trigger", {})
        if location and trigger.get("location") and trigger.get("location") != location:
            return False
        if action and trigger.get("action") and trigger.get("action") != action:
            return False
        skill_req = trigger.get("skill")
        if skill_req:
            name, lvl = skill_req
            if get_skill_level(name) < lvl:
                return False
        flags_req = trigger.get("flags", [])
        for f in flags_req:
            if not flags.get(f, False):
                return False
        return True

    def available_events(location=None, action=None):
        result = []
        for ev in events_registry:
            if ev["id"] in completed_events:
                continue
            if event_matches(ev, location, action):
                cooldown = cooldowns.get(ev["id"], 0)
                if cooldown == 0:
                    result.append(ev)
        return result

    def trigger_event(event_id):
        ev = next((e for e in events_registry if e["id"] == event_id), None)
        if not ev:
            return False
        if ev.get("once") and event_id in completed_events:
            return False
        cooldown = ev.get("cooldown", 0)
        if cooldown:
            cooldowns[event_id] = cooldown
        renpy.call(ev["label"])
        completed_events.add(event_id)
        return True

init python:
    def process_events(location=None, action=None):
        for ev in available_events(location, action):
            trigger_event(ev["id"])
