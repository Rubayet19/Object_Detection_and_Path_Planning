# Object Detection and Path Planning

## Introduction
This project aims to develop an autonomous delivery robot capable of navigating through environments with dynamic obstacles. It leverages SSD MobileNet V3 for object detection and implements advanced path planning algorithms. This work is part of my thesis project, focusing on enhancing the efficiency and safety of autonomous robotic deliveries.

## Technologies
- **Object Detection:** SSD MobileNet V3
- **Programming Language:** Python
- **Libraries:** TensorFlow, OpenCV
- **Path Planning:** Custom Algorithm Implementation using GraphHopper API

## Project Structure
- `main.py` - The entry point of the application, integrating object detection and path planning.
- `Path_Planning.py` - Contains the path planning algorithm used by the robot to navigate.
- `threshold.py` - Helper script for setting detection thresholds.
- `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` - Configuration file for SSD MobileNet V3.
- `coco.names` - Contains the names of objects that can be detected by the model.

## Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/Rubayet19/Object_Detection_and_Path_Planning.git
   cd Object_Detection_and_Path_Planning
2. Set up a Python virtual environment (optional but recommended)
3. python -m venv venv
4. source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install dependencies
pip install -r requirements.txt

## Usage
To run the project, execute the main.py script:
python main.py

Adjust the parameters within the script as needed to fit the specific requirements of your environment or robot.

## Contributing
Contributions to the project are welcome! Here's how you can contribute:

Fork the repository.
Create a new branch for your feature (git checkout -b feature/AmazingFeature).
Commit your changes (git commit -m 'Add some AmazingFeature').
Push to the branch (git push origin feature/AmazingFeature).
Open a pull request.
