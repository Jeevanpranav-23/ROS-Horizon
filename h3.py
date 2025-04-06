import numpy as np
from scipy.spatial.transform import Rotation

def euler_to_quaternion(roll, pitch, yaw):
    """
    Converts Euler angles (roll, pitch, yaw) to Martian quaternion format (w, x, y, z).
    
    Args:
        roll (float): Rotation around x-axis in radians
        pitch (float): Rotation around y-axis in radians
        yaw (float): Rotation around z-axis in radians
        
    Returns:
        tuple: (w, x, y, z) quaternion components
    """

    rotation = Rotation.from_euler('xyz', [roll, pitch, yaw], degrees=False)
    quat = rotation.as_quat()  # Returns (x, y, z, w)
    
    # Reorder to (w, x, y, z) which is more common
    return (quat[3], quat[0], quat[1], quat[2])

if __name__ == "__main__":

    roll = np.pi/4   # 45 degrees
    pitch = np.pi/6  # 30 degrees
    yaw = np.pi/3    # 60 degrees
    
    quaternion = euler_to_quaternion(roll, pitch, yaw)
    print("Martian quaternion (w, x, y, z):")
    print(f"{quaternion[0]:.4f}, {quaternion[1]:.4f}, {quaternion[2]:.4f}, {quaternion[3]:.4f}")
