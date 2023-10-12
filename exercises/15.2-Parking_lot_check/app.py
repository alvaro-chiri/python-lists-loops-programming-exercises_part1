parking_state = [
  [1, 1, 1],
  [0, 0, 0],
  [1, 1, 2]
]

# Your code go here:


def get_parking_lot(lot):
    state = {"total_slots": 0, "available_slots": 0, "occupied_slots": 0}
    for i in range(len(lot)):
            for x in range(len(lot[i])):
                if lot[i][x] == 1:
                    state["occupied_slots"] += 1
                    state["total_slots"] += 1
                elif lot[i][x] == 2:
                    state["available_slots"] += 1
                    state["total_slots"] += 1
    return state


print(get_parking_lot(parking_state))
