from collections import defaultdict
from _rentingalgo import PricingAlgo
from loguru import logger
class Branch:

    def __init__(self):
        self.branches = defaultdict(dict)
        self.algo = PricingAlgo()

    def add_branch(self, branch_name: str, vehicle_details: list):
        for vehicle_detail in vehicle_details:
            vehicle_detail = vehicle_detail.split(" ")
            price = vehicle_detail[3].split('.')[1]
            self.branches[branch_name][vehicle_detail[1]] = {
                    "quantity": int(vehicle_detail[0]),
                    "price": price,
                    "booked":0,
                    "available":int(vehicle_detail[0])
            }

    def add_vehicle(self, branch_name: str, vehicle_detail: list):
        vehicle_detail = vehicle_detail.split(" ")
        self.branches[branch_name][vehicle_detail[1]][
                    "quantity"
                ] += int(vehicle_detail[0])

    def rent_vehicle(self, vehicle_type, start, end):
        best_vehicle = self.algo.best_vehicle_branch(self.branches.copy(), vehicle_type)
        if best_vehicle:
            self.branches[best_vehicle['branch_name']][vehicle_type]['booked']+=1
            self.branches[best_vehicle['branch_name']][vehicle_type]['available']-=1
            logger.success(f"vehicle booked from {best_vehicle['branch_name']} branch")
        else:
            logger.error("no vehicle available")


    def print_system_view_for_time_slot(self, start_time, end_time):
        for branch_name, vehicles in self.branches.items():
            print(f"***{branch_name}***")
            for vehicle_type, metadata in vehicles.items():
                if not metadata['available']:
                    print(f"All {vehicle_type} are booked.")
                else:
                    print(f"{vehicle_type} is available for Rs{metadata['price']}")


# ‘Koramangala’: 
# 		All “suv” are booked.
# 		“sedan” is available for Rs.10
# 		“bike” is available for Rs.20



branch = Branch()
branch.add_branch("koramangala", ["1 suv for Rs.12 per hour", "3 sedan for Rs.10 per hour", "3 bikes for Rs.20 per hour"])
branch.add_branch("jayanagar", ["3 sedan for Rs.11 per hour", "3 bikes for Rs.30 per hour", "4 hatchback for Rs.8 per hour"])
branch.add_branch("malleshwaram", ["1 suv for Rs.11 per hour", "10 bikes for Rs.3 per hour", "3 sedan for Rs.10 per hour"])
branch.add_vehicle("koramangala",  "1 sedan")
branch.rent_vehicle("suv", "20th Feb 10:00 PM", "20th Feb 12:00 PM")
branch.rent_vehicle("suv", "20th Feb 10:00 PM", "20th Feb 12:00 PM")
branch.rent_vehicle("suv", "20th Feb 10:00 PM", "20th Feb 12:00 PM")
branch.print_system_view_for_time_slot("20th Feb 11:00 PM", "20th Feb 12:00 PM")
