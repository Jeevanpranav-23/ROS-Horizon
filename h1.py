def adjust_rover_position(x, y):
    """
    Adjusts the rover's navigation system to account for the 55cm offset.
    
    The camera is mounted at the front and top of the rover. When it detects
    the marker at (x, y, -60), the actual marker position needs to be adjusted
    by 55cm in the forward direction (z-axis in camera coordinates).
    
    Args:
        x (float): x-coordinate of marker in camera frame
        y (float): y-coordinate of marker in camera frame
        
    Returns:
        tuple: (x_final, y_final, z_final) adjusted coordinates
    """
    # The camera sees the marker at (x, y, -60) but the rover stops 55cm short
    # We need to add 55cm to the z-coordinate (forward direction)
    z_adjusted = -60 + 55  # -60cm + 55cm = -5cm
    
    return (x, y, z_adjusted)

def calculate_distance_before_after(x, y):
    """
    Calculates distance between marker and camera before and after adjustment.
    
    Args:
        x (float): x-coordinate
        y (float): y-coordinate
        
    Returns:
        tuple: (distance_before, distance_after)
    """

    distance_before = (x**2 + y**2 + (-60)**2)**0.5
    
    x_final, y_final, z_final = adjust_rover_position(x, y)
    distance_after = (x_final**2 + y_final**2 + z_final**2)**0.5
    
    return (distance_before, distance_after)


if __name__ == "__main__":
    x, y = 40, 80 
    adjusted_pos = adjust_rover_position(x, y)
    print(f"Adjusted position: {adjusted_pos}")
    
    dist_before, dist_after = calculate_distance_before_after(x, y)
    print(f"Distance before adjustment: {dist_before:.2f} cm")
    print(f"Distance after adjustment: {dist_after:.2f} cm")
