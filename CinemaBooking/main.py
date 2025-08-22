from _system import CinemaSystem

system = CinemaSystem()
# Test case 1
show_id = system.registerShow(
    "Grand Cinema", "Avengers", "02/05/2025 10:00 AM", 15.0, 100
)
system.order_ticket("Avengers", "02/05/2025 10:00 AM", 60)
system.start_show(show_id)
system.end_show(show_id)
system.print_system_stats()
print("\n")


system = CinemaSystem()
# Test case 2
show_id_1 = system.registerShow(
    "Grand Cinema", "Avengers", "02/05/2025 10:00 AM", 15.0, 100
)
show_id_2 = system.registerShow("PVR", "X-Men", "02/05/2025 11:00 AM", 15.0, 100)
system.order_ticket("Avengers", "02/05/2025 10:00 AM", 60)
try:
    system.end_show(show_id_1)
except Exception as e:
    print("Error:", e)
system.start_show(show_id_1)
print(" \n")


system = CinemaSystem()
# Test case 3
show_id_1 = system.registerShow(
    "Grand Cinema", "Avengers", "02/05/2025 10:00 AM", 15.0, 100
)
show_id_2 = system.registerShow("PVR", "Avengers", "02/05/2025 10:00 AM", 10.0, 100)
system.order_ticket("Avengers", "02/05/2025 10:00 AM", 60)
system.start_show(show_id_1)
system.end_show(show_id_1)
system.start_show(show_id_2)
system.end_show(show_id_2)
system.print_system_stats()
print(" \n")


system = CinemaSystem()
# Test case 4
show_id_1 = system.registerShow(
    "Grand Cinema", "Avengers", "02/05/2025 10:00 AM", 15.0, 100
)
show_id_2 = system.registerShow("PVR", "Avengers", "02/05/2025 10:00 AM", 10.0, 100)
system.order_ticket("Avengers", "02/05/2025 10:00 AM", 60)
system.order_ticket("Avengers", "02/05/2025 10:00 AM", 100)
print(system.order_ticket("Avengers", "02/05/2025 10:00 AM", 50))
system.start_show(show_id_2)
print(system.order_ticket("Avengers", "02/05/2025 10:00 AM", 10))
system.end_show(show_id_2)
print(" \n")



# Test case 5
system = CinemaSystem()
show_id_1 = system.registerShow(
    "Grand Cinema", "Avengers", "02/05/2025 10:00 AM", 15.0, 100
)
show_id_2 = system.registerShow("PVR", "Avengers", "02/05/2025 10:00 AM", 10.0, 100)
booking_id_1, _ = system.order_ticket("Avengers", "02/05/2025 10:00 AM", 60)
booking_id_2, _ = system.order_ticket("Avengers", "02/05/2025 10:00 AM", 100) 

print(system.cancel_booking(booking_id_1))  # Refund 50% of 600 = 300
system.start_show(show_id_1)
print(system.cancel_booking(booking_id_2))  # Refund 0 (show already started)
system.end_show(show_id_1)
system.start_show(show_id_2)
system.end_show(show_id_2)
system.print_system_stats()
print(" \n")
