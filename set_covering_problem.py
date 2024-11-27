# 1. Pick the station that covers the most states that haven’t been covered
# yet. It’s OK if the station covers some states that have been covered
# already.
# 2. Repeat until all the states are covered

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

# You need to go
# through every station and pick the one that covers the most
# uncovered states. I’ll call this best_station:

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
        
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)