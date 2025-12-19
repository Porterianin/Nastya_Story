# -*- coding: utf-8 -*-

init python:
    def periods_left():
        return max(0, periods_per_day - current_period)

    def spend_period(cost=1):
        global current_period
        if current_period + cost > periods_per_day:
            notify("Недостаточно времени на сегодня")
            return False
        current_period += cost
        if current_period >= periods_per_day:
            notify("День завершён. Отдохни дома, чтобы сбросить усталость.")
        return True

    def reset_day():
        global current_period
        current_period = 0

label end_of_day:
    $ reset_day()
    return
