---
id: loc_apartment_5_hallway
entity_type: location
status: approved_partial
parent: loc_apartment_5
connections:
  - loc_entrance_1_floor_3
  - loc_apartment_5_room
  - loc_apartment_5_kitchen
  - loc_apartment_5_bathroom
  - loc_playground
  - hc_residential_district
objects:
  - obj_apartment_5_hallway_mirror
---

# Квартира №5 — прихожая

Связывает комнату, кухню, ванную/туалет и выход из квартиры.

## Действия
На первом этапе предусмотрено взаимодействие с зеркалом: посмотреться в зеркало.

## Выход из квартиры
При выборе выхода игроку предлагаются три маршрута:

1. **В подъезд — 3 этаж** → `loc_entrance_1_floor_3`.
2. **На детскую площадку** → `loc_playground`.
3. **В спальный район** → основной экран `hc_residential_district`.

Это быстрые навигационные переходы. Они не отменяют подробную структуру дома, а позволяют не прокликивать её при рутинном перемещении.

## Визуальный паспорт
Не утверждён.
