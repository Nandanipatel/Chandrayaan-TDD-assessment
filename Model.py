def control_commands(initial_position, initial_direction, commands):
    position = initial_position
    direction = initial_direction

    previous_direction = None
    
    for command in commands:
        if command == "f":
            if direction == "N":
                position = (position[0], position[1]+1, position[2])
            elif direction == "S":
                position = (position[0], position[1]-1, position[2])
            elif direction == "E":
                position = (position[0]+1, position[1], position[2])
            elif direction == "W":
                position = (position[0]-1, position[1], position[2])
            elif direction == "Up":
                position = (position[0], position[1], position[2]+1)
            elif direction == "Down":
                position = (position[0], position[1], position[2]-1)
                
        elif command == "b":
            if direction == "N":
                position = (position[0], position[1]-1, position[2])
            elif direction == "S":
                position = (position[0], position[1]+1, position[2])
            elif direction == "E":
                position = (position[0]-1, position[1], position[2])
            elif direction == "W":
                position = (position[0]+1, position[1], position[2])
            elif direction == "Up":
                position = (position[0], position[1], position[2]-1)
            elif direction == "Down":
                position = (position[0], position[1], position[2]+1)
                
       
        # Check if the Chandrayaan is within the galactic boundaries

        if position[0] < -100 or position[0] > 100 or position[1] < -100 or position[1] > 100 or position[2] < -100 or position[2] > 100:
            raise ValueError("Chandrayaan is out of boundries")
        
        # if the direction is up or down prevent the previous added direction
        if direction != "Up" and direction != "Down":
            previous_direction = direction
            
    return position, direction