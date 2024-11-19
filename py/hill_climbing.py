def objective_function(x):
    return -(x**2) + 4*x  # Example objective function (maximize)

def hill_climbing(starting_point):
    current_point = starting_point
    while True:
        # Explore neighbors
        neighbor_up = current_point + 0.1
        neighbor_down = current_point - 0.1
        
        # Choose the best neighbor
        if objective_function(neighbor_up) > objective_function(current_point):
            current_point = neighbor_up
        elif objective_function(neighbor_down) > objective_function(current_point):
            current_point = neighbor_down
        else:
            break  # No improvement, stop

    return current_point, objective_function(current_point)

# Corrected part
if __name__ == "__main__":
    starting_point = 0  # Starting at x = 0
    best_point, best_value = hill_climbing(starting_point)
    print(f"Best point: {best_point}, Best value: {best_value}")
