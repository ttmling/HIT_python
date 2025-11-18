#===Câu 1
def create_event(name, day, time):
    data = {}
    data["name"] = name
    data["day"] = day
    data["time"] = time
    return data

event = create_event("Math", "Mon", "07:00")
print("Câu 1", event)


#===Câu 2
def add_event(schedule, event):
    kq = schedule.copy()
    kq.append(event)
    return kq

schedule = []
schedule = add_event(schedule, event)
print("Câu 2", schedule)


#===Câu 3
def find_by_day(schedule, day):
    for event in schedule:
        if event["day"] == day:
            return event
    return None

print("Câu 3", find_by_day(schedule, "Fri"))


#===Câu 4
def remove_event(schedule, name):
    return [event for event in schedule if event["name"] != name]

print("Câu 4", remove_event(schedule, "Math"))


#==Câu 5
def export_schedule(schedule):
    for event in schedule:
        print(f"{event["day"]} {event["time"]} - {event["name"]}")

export_schedule(schedule)