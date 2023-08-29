from Model import control_commands

initial_position = (0, 0, 0)
initial_direction = "N"
# commands = ["f", "r", "u","b","l"]
print("Enter Commands")
commands=input()


final_position, final_direction = control_commands(initial_position, initial_direction, commands)

print("Final Position:", final_position)
print("Final Direction:", final_direction)