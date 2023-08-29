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

        elif command == "l":
            if direction == "N":
                direction = "W"
            elif direction == "S":
                direction = "E"
            elif direction == "E":
                direction = "N"
            elif direction == "W":
                direction = "S"
                
            # check the previous direction for up and down
            elif direction == "Up":
                if previous_direction == "N":
                    direction = "W"
                elif previous_direction == "S":
                    direction = "E"
                elif previous_direction == "E":
                    direction = "N"
                elif previous_direction == "W":
                    direction = "S"
            elif direction == "Down":
                if previous_direction == "N":
                    direction = "E"
                elif previous_direction == "S":
                    direction = "W"
                elif previous_direction == "E":
                    direction = "S"
                elif previous_direction == "W":
                    direction = "N"
                
        elif command == "r":
            if direction == "N":
                direction = "E"
            elif direction == "S":
                direction = "W"
            elif direction == "E":
                direction = "S"
            elif direction == "W":
                direction = "N"

            # check the previous direction for up and down
            elif direction == "Up":
                if previous_direction == "N":
                    direction = "E"
                elif previous_direction == "S":
                    direction = "W"
                elif previous_direction == "E":
                    direction = "S"
                elif previous_direction == "W":
                    direction = "N"
                elif previous_direction == "Up":
                    pass
                elif previous_direction == "Down":
                    pass
            elif direction == "Down":
                if previous_direction == "N":
                    direction = "W"
                elif previous_direction == "S":
                    direction = "E"
                elif previous_direction == "E":
                    direction = "N"
                elif previous_direction == "W":
                    direction = "S"
                elif previous_direction == "Up":
                    pass
                elif previous_direction == "Down":
                    pass
        
                
       
        # Check if the Chandrayaan is within the galactic boundaries

        if position[0] < -100 or position[0] > 100 or position[1] < -100 or position[1] > 100 or position[2] < -100 or position[2] > 100:
            raise ValueError("Chandrayaan is out of boundries")
        
        # if the direction is up or down prevent the previous added direction
        if direction != "Up" and direction != "Down":
            previous_direction = direction
            
    return position, direction