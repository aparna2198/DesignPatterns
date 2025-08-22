from abc import ABC, abstractmethod

class RentingAlgo(ABC):
    @abstractmethod
    def best_vehicle_branch(self):
        pass

class PricingAlgo(RentingAlgo):
    def best_vehicle_branch(self, branches, vehicle_type:str):
        available_vehicles_vehicle_type = []
        for branch_name, vehicles in branches.items():
            vehicles_vehicle_type = vehicles.get(vehicle_type)
            if vehicles_vehicle_type and vehicles_vehicle_type['available']:
                vehicles_vehicle_type["branch_name"] = branch_name
                available_vehicles_vehicle_type.append(vehicles_vehicle_type)
        available_vehicles_vehicle_type.sort(key = lambda x:int(x['price']))
        return available_vehicles_vehicle_type[0] if available_vehicles_vehicle_type else None




