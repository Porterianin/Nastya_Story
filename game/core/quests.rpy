# -*- coding: utf-8 -*-

init python:
    class QuestStage(object):
        def __init__(self, description, complete_conditions=None, rewards=None):
            self.description = description
            self.complete_conditions = complete_conditions or []
            self.rewards = rewards or []

    class Quest(object):
        def __init__(self, qid, title, description, requirements=None, stages=None):
            self.id = qid
            self.title = title
            self.description = description
            self.requirements = requirements or []
            self.stages = stages or []

    quests_registry = {
        "cafe_intro": Quest(
            "cafe_intro", "Знакомство с Кристиной", "Устроиться на смены в кафе.",
            requirements=[{"location": "cafe"}],
            stages=[
                QuestStage("Поговорить с Кристиной", complete_conditions=["met_kristina"]),
                QuestStage("Пройти стажировку", complete_conditions=["cafe_training_done"], rewards=[{"unlock_action": "cafe_shift"}]),
            ],
        ),
        "cafe_party": Quest(
            "cafe_party", "Закрытая вечеринка", "Доказать готовность и попасть на частное обслуживание.",
            requirements=[{"quest": "cafe_intro", "stage": 1, "skill": ("social", 2)}],
            stages=[
                QuestStage("Достигнуть доверия Кристины", complete_conditions=["kristina_trust"], rewards=[{"flag": "party_invite"}]),
                QuestStage("Отработать вечеринку", complete_conditions=["party_served"], rewards=[{"money": 200}, {"relationship": ("leon", 10)}]),
            ],
        ),
        "campus_project": Quest(
            "campus_project", "Учебный проект", "Помочь Маше с презентацией.",
            requirements=[{"location": "campus"}],
            stages=[
                QuestStage("Обсудить проект с Машей", complete_conditions=["project_offer"], rewards=[{"skill_xp": ("discipline", 15)}]),
                QuestStage("Подготовить черновик", complete_conditions=["project_draft"], rewards=[{"skill_xp": ("intellect", 20)}]),
                QuestStage("Выступить", complete_conditions=["project_presented"], rewards=[{"relationship": ("masha", 10)}]),
            ],
        ),
        "tutoring": Quest(
            "tutoring", "Репетиторство", "Заработать на знаниях.",
            requirements=[{"quest": "campus_project", "stage": 2}],
            stages=[
                QuestStage("Найти первых учеников", complete_conditions=["tutor_first"], rewards=[{"money": 80}]),
                QuestStage("Закрепиться", complete_conditions=["tutor_repeat"], rewards=[{"skill_xp": ("social", 10)}, {"money": 120}]),
            ],
        ),
        "park_leon": Quest(
            "park_leon", "Контакты Леона", "Завести знакомство с организатором вечеринок.",
            requirements=[{"location": "park"}],
            stages=[
                QuestStage("Встретить Леона", complete_conditions=["met_leon"], rewards=[{"relationship": ("leon", 10)}]),
                QuestStage("Получить приглашение", complete_conditions=["leon_invite"], rewards=[{"flag": "party_invite"}]),
            ],
        ),
    }

    def quest_available(qid):
        quest = quests_registry.get(qid)
        if not quest:
            return False
        for req in quest.requirements:
            if "location" in req and not unlocked_locations.get(req["location"], False):
                return False
            if "quest" in req:
                state = quest_states.get(req["quest"], 0)
                if state < req.get("stage", 0):
                    return False
            if "skill" in req:
                name, level_needed = req["skill"]
                if get_skill_level(name) < level_needed:
                    return False
        return True

    def quest_stage(qid):
        return quest_states.get(qid, 0)

    def complete_condition(condition):
        return condition in flags and flags[condition] or condition in completed_events

    def advance_quest(qid, condition):
        quest = quests_registry.get(qid)
        if not quest:
            return
        idx = quest_states.get(qid, 0)
        if idx >= len(quest.stages):
            return
        stage = quest.stages[idx]
        if condition in stage.complete_conditions:
            quest_states[qid] = idx + 1
            apply_rewards(stage.rewards)
            notify(f"Квест {quest.title}: этап завершён")

    def apply_rewards(rewards):
        for reward in rewards:
            if "money" in reward:
                add_money(reward["money"])
            if "skill_xp" in reward:
                name, xp = reward["skill_xp"]
                gain_xp(name, xp)
            if "relationship" in reward:
                name, delta = reward["relationship"]
                relationships[name] = relationships.get(name, 0) + delta
                notify(f"Отношения {name}: {delta:+}")
            if "unlock_action" in reward:
                unlocked_actions[reward["unlock_action"]] = True
            if "flag" in reward:
                flags[reward["flag"]] = True

