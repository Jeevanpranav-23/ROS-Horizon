#!/bin/bash

# 1) Create new directory called rover_mission and navigate into it
mkdir -p rover_mission
cd rover_mission

# 2) Create three empty files named log1.txt, log2.txt, and log3.txt
touch log1.txt log2.txt log3.txt

# 3) Rename log1.txt to mission_log.txt
mv log1.txt mission_log.txt

# Add some sample content to mission_log.txt for testing
echo "This is a sample log entry" >> mission_log.txt
echo "ERROR: Battery low" >> mission_log.txt
echo "System check complete" >> mission_log.txt
echo "ERROR: Sensor malfunction" >> mission_log.txt
echo "All systems nominal" >> mission_log.txt

# 4) Find all files in the current directory that have a .log extension
# (Creating a sample .log file first)
touch sample.log
find . -name "*.log"

# 5) Display the contents of mission_log.txt without opening it in an editor
cat mission_log.txt

# 6) Find and display all lines containing the word "ERROR" in mission_log.txt
grep "ERROR" mission_log.txt

# 7) Count the number of lines in mission_log.txt
wc -l mission_log.txt

# 8) Show the system's current date and time
date

# 9) Display the CPU usage of your system in real time
# Using top in batch mode for a single snapshot
top -bn1 | grep "Cpu(s)"

# 10) Schedule a command to shut down the system in 10 minutes
echo "System will shut down in 10 minutes"
shutdown -h +10

# Rover system check function
rover_system_check() {
    # Generate random battery percentage (0-100)
    battery=$(( RANDOM % 101 ))
    echo "Battery level: $battery%"
    
    # Check battery level
    if [ $battery -lt 20 ]; then
        echo "Battery low! Return to base!" >> mission_log.txt
        echo "Battery low! Return to base!"
        exit 1
    fi
    
    # Check network connectivity by pinging google.com
    if ping -c 1 google.com &> /dev/null; then
        echo "All systems operational!" >> mission_log.txt
        echo "All systems operational!"
    else
        echo "Communication failure!" >> mission_log.txt
        echo "Communication failure!"
        exit 1
    fi
}

# Call the rover system check function
rover_system_check
