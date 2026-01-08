# -*- coding: utf-8 -*-

init python:
    def add_money(amount):
        global money
        money += amount
        notify(f"Деньги: {amount:+} (итого {money})")

    def try_spend(amount):
        global money
        if money < amount:
            notify("Недостаточно денег")
            return False
        money -= amount
        notify(f"Потрачено {amount}, осталось {money}")
        return True
