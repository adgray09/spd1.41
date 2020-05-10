# def tracking(my_tuple):
#     answer = []
#     iteration = 0
#     temp_tuple = my_tuple[iteration]
#     for i in my_tuple:
#         if my_tuple[i][0] == temp_tuple:
#             answer.append(temp_tuple)
#         else:
#             iteration += 1
#             temp_tuple = temp_tuple[iteration]
            
# whole_tuple = [(Noodle, Jungalow), (Korok, Bunpun), (Bunpun, Noodle), (Jungalow, Astra Nova)]

            
# print(tracking(whole_tuple))

def tracking_places(tickets):
    from_to_dictionary = {}
    
    for ticket in tickets:
        from_island = ticket[0]
        to_island = ticket[1]
        from_to_dictionary[from_island] = to_island
    print(from_to_dictionary)
    
    # figuring out where to start
    start = ""
    for from_island in from_to_dictionary.keys():
        if from_island not in from_to_dictionary.values():
            start = from_island
            break
        
    # reconstructing the order
    result = []
    current = start
    for i in range(len(tickets)):
        result.append(current)
        next = from_to_dictionary[current]
        current = next
    result.append(current)
    return result
        
    
print(tracking_places([('Noodle', 'Jungalow'), ('Korok', 'Bunpun'), ('Bunpun', 'Noodle'), ('Jungalow', 'Astra Nova')]))
    
    
    
