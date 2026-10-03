import numpy as np
import pandas as pd


def unique_values(card):
    unique = []

    for lol in card:
        for uj in lol:
            if type(uj) == int:
                continue
            unique.append(uj)

    unique = list(sorted((set(unique))))

    return unique

def table(card):

    df2 = pd.DataFrame({
    "node": unique_values(card),
    "shortest_distance": np.inf,
    "previous_node": "nichts"
    })

    return df2


    
def dijkstra(nodes, start, end):

    if start == end:
        return print("BRO DIGGAH HÖR MAL AUF MIT DIESEM FAXXEN UND TUE WAS GESCHEITES REIN!!!! :(")

    

    unvisited = unique_values(nodes)
    visited = []

    visited_table = pd.DataFrame()
    unvisited_table = table(nodes)
    unvisited_table.loc[unvisited_table["node"] == start, "shortest_distance"] = 0
    current_node = start

    if not (unvisited_table["node"] == start).any():
        return print(f"Diesen Node '{start}' gibt es nicht")

    if not (unvisited_table["node"] == end).any():
            return print(f"Diesen Node '{end}' gibt es nicht")

    while unvisited:
        for row in nodes:
            if current_node == row[0] and row[1] in unvisited:
                if unvisited_table.loc[unvisited_table["node"] == row[1], "shortest_distance"].iloc[0] > (row[2]+unvisited_table.loc[unvisited_table["node"] == current_node, "shortest_distance"].iloc[0]):
                    unvisited_table.loc[unvisited_table["node"] == row[1], "shortest_distance"] = (row[2]+unvisited_table.loc[unvisited_table["node"] == row[0], "shortest_distance"].iloc[0])
                    unvisited_table.loc[unvisited_table["node"] == row[1], "previous_node"] = current_node

        idx = unvisited_table[unvisited_table["node"] == current_node].index
        visited_table = pd.concat([visited_table, unvisited_table.loc[idx]])

        visited.append(current_node)
        unvisited.remove(current_node)

        unvisited_table.drop(idx, inplace=True)

        if unvisited_table.empty:
            break

        current_node = unvisited_table.loc[unvisited_table["shortest_distance"].idxmin(), "node"]



    #RÜCKKUPPLUNG
    distance_result = [end]
    previous = visited_table.loc[visited_table["node"] == end, "previous_node"].iloc[0]

    end_row = visited_table.loc[visited_table["node"] == end]
    if end_row.empty or end_row["shortest_distance"].iloc[0] == np.inf:
        print(f"Kein Weg von {start} nach {end} vorhanden.")

        return visited_table, [], np.inf

    while True:   
        if previous == start:
            distance_result.append(start)
            break 

        distance_result.append(previous)
        previous = visited_table.loc[visited_table["node"] == previous, "previous_node"].iloc[0]
       
    preis = visited_table.loc[visited_table['node'] == end, "shortest_distance"].iloc[0]
    print(visited_table)
    print(f"BESTE VORHANDENE STRECKE UND SEIN PREIS ({preis}) :   {distance_result[::-1]}")

    return visited_table, distance_result, preis
    
    
dijkstra(nodes=input, start="AR", end="CV")
