# Football Analysis Deep Learning Project

![Sample Output](/output_videos/output_sample_screenshot.png)

This project is a deep learning-powered football analysis tool that processes match footage to extract and visualize various metrics like player positions, speeds, distances covered, team possession, and camera movements. The output is an annotated video providing comprehensive insights into the game.

## Features

- **Object Tracking**: Detects and tracks players and the ball using YOLOv5-based object detection.
- **Camera Movement Estimation**: Analyzes camera movements to adjust player and ball positions for accurate tracking.
- **Team Assignment**: Automatically assigns players to teams based on jersey colors.
- **Ball Possession Analysis**: Identifies which player or team has possession of the ball.
- **Speed and Distance Estimation**: Calculates players' speeds and distances covered during the game.
- **Perspective Transformation**: Applies view transformation for a bird's-eye view of the field.
- **Annotated Video Output**: Generates an output video with real-time annotations of players, ball, speed, distance, and team possession.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- OpenCV
- NumPy
- PyTorch
- Additional dependencies listed in `requirements.txt`

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/aum2606/football-analysis.git
    cd football-analysis
    ```
2. Install dependencies:
    ```
    bash
    pip install -r requirements.txt
    ```
3. Place your input video in the input_videos directory.

4. Ensure you have the pre-trained model file (**models/best.pt**) and necessary stub files in the **models** and **stubs** directories.

## Usage

To process a football match video, run the following command:

bash
```
python main.py
```

This will read the video, perform analysis, and generate an annotated output video saved as **output_videos/output_video.avi**.

## File Structure

- **main.py**: Main script orchestrating the analysis pipeline.
- **utils.py**: Utility functions for reading and saving videos.
- **trackers.py**: Module for detecting and tracking objects.
- **team_assigner.py**: Assigns players to teams based on jersey colors.
- **player_ball_assigner.py**: Assigns ball possession to players.
- **camera_movement_estimator.py**: Estimates and adjusts for camera movements.
- **view_transformer.py**: Transforms player and ball positions for better visualization.
- **speed_and_distance_estimator.py**: Calculates speed and distance metrics.
- **output_videos/**: Directory for saving annotated output videos.
- **input_videos/**: Directory for input videos to analyze.

## Sample Output

# Future Enhancements
- Add support for multi-camera analysis.
- Enhance the ball possession logic with advanced proximity metrics.
- Incorporate live-stream analysis.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

[YOLOv5](https://docs.ultralytics.com/) for object detection.
Football data visualization techniques inspired by [StatsBomb](https://statsbomb.com/).

