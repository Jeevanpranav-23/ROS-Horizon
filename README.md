# ROS-Horizon
# 🚀 MaRS Rover Task #1
## Learning Experience

Through this challenge, I explored:
- Core Linux terminal commands and scripting
- Basic automation with Bash
- 3D spatial transformations and frame references
- Signal noise reduction using custom filters
- Real-world navigation and obstacle avoidance
- Image processing with OpenCV


This task gave me insight into how multi-disciplinary robotics systems operate — from communication to localization and control.

---

##  Tasks Overview & Approach

###  Light Dose

**Ubuntu Terminal Commands**  
A Bash script (`light_dose.sh`) executes commands for directory management, text processing, and system monitoring.

**Bash Script: rover_system_check.sh**  
Performs:
- Random battery level simulation
- Ping test to check connectivity
- Logs system readiness

---

###  Medium Dose

#### 1. **Red Circle Marker Correction**
- Adjusts rover's position using new frame of reference.
- Corrected for offset due to camera placement at (x, y, -60).

#### 2. **Morse Code Decoder**
- Converts Morse code signals to English text.
- Handles spacing and unknown symbols.

#### 3. **Encoded Message Reversal**
- Deciphers encoded messages using shift pattern.

#### 4. **Sensor Noise Filtering**
- Implements `Muchiko`, `Sanchiko`, and hybrid filters.
- Plots and compares results to find the most stable value.

#### 5. **3D Rotation System Conversion**
- Converts Euler angles to quaternion format (4D Martian system).
- Avoids gimbal lock.

---

###  Hard Dose

#### 1. **Obstacle Avoidance and Path Planning**
- Reads obstacles from `arena.txt`.
- Builds `n x n` grid map.
- Uses BFS/A* to find shortest path from (0, 0) to (10, 10).
- Bonus: visual path and step-by-step route included.

#### 2. **Arrow Distance Detection**
- Uses pinhole camera formula:
Distance = (Real Width × Focal Length) / Perceived Width

## Challenges Faced
Honestly, this task pushed me in all the right ways. Here’s what gave me a tough time:

Filtering sensor data wasn’t just plug-and-play. I had to build my own filters (Muchiko, Sanchiko, and a hybrid one), and getting them to smooth the data without killing the actual signal was all about trial, error, and patience.

Euler to quaternion conversion was a math rabbit hole. I avoided using any libraries, so I had to dig deep into the formulas and make sure I wasn’t hitting issues like gimbal lock.

Path planning with BFS and A* took time to get right. Reading from the file, building the grid, finding neighbors — it sounds simple until you start hitting dead ends in your logic.

Decoding Morse and encrypted messages was fun, but catching edge cases (like weird spacing or unknown characters) meant a lot of test cases and tweaking.
##How I Approached It:
I didn’t try to solve everything at once. Here's how I broke it down:

Start small, test often — I always began with the core idea (like basic filtering or pathfinding) and got that working first before adding fancy stuff.

Visuals helped a ton — plotting graphs for the filters or mapping the path step-by-step made bugs easier to spot.

Keep it modular — I wrote each part like its own little program so I could debug it easily and reuse pieces when needed.

Google + Docs = Lifesavers — I constantly checked formulas for quaternions, OpenCV docs, and even Git tutorials when I got stuck.

Refactor, refine, repeat — Once things worked, I always came back to clean the code or make the output more readable or efficient.



- [GeeksforGeeks: Linux Commands & Bash Scripting](https://www.geeksforgeeks.org)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Pinhole Camera Model - LearnOpenCV](https://learnopencv.com)
- [Quaternion Basics - 3D Rotations](https://eater.net/quaternions)
- [Behavior Trees Overview](https://www.behaviortree.dev/)
- [Git & GitHub Crash Course](https://www.codedex.io/git-github)
- I used Ai tools to do my work easier (chatGpt,deepseek,copilot)


#what is good at working these things means :
Clear Sectioning: The Light/Medium/Hard dose structure makes it super digestible.

Technical Depth: You’ve demonstrated a solid grasp on both hardware-interfacing (sensors, camera) and software (Bash, Python, OpenCV).

Realistic Simulation: The rover system check and obstacle avoidance feel like real-world Mars rover tasks.

Useful References: Crediting resources shows solid research backing.

#About maze rover competition: the experience which i had is good than i thought how the software built the real time running rover and navigation and all so good and the commands idk what to write in the ubantu so the team members helped what to do thankyou for giving this oppourtunity to me i am very thankfull to all the MaRS Rover team members 


----
#The file h1.py is - Rover Navigation Adjusment(medium dose ) 
#The file h2.py is - Message Decoder (medium dose )
#The file h3.py is - 3D Rotation Conversion(medium dose )
#The file h4.py is -Rover path planning (hard dose)
#The file H myscript.sh is - Bash script 1-10 problems (light dose) 
