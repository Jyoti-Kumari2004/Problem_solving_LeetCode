class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        buses.sort()
        passengers.sort()
        
        i = 0 
        m = len(passengers)
        
        last_bus = buses[-1]
        people_on_last_bus = []
        
        for bus in buses:
            cnt = 0
            while i < m and passengers[i] <= bus and cnt < capacity:
                last_person = passengers[i]
                i += 1
                cnt += 1
                if bus == last_bus:
                    people_on_last_bus.append(last_person)
        
        taken = set(passengers)
        
        if len(people_on_last_bus) < capacity:
            t = last_bus
            while t in taken:
                t -= 1
            return t
        
        last_boarded = people_on_last_bus[-1]
        t = last_boarded - 1
        while t in taken:
            t -= 1
        return t
