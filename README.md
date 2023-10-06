# Ball Trajectory Classification (BTC)

## BTC Objectives
* to improve the performance of ball tracking. : During the ball detection process for ball tracking, there are frames that fail the detection. In this case, the ball's position information should be filled in the corresponding frame, and the information should contain the ball's movement, for example, whether the ball was moving straight on the ground or parabolic in the air.
* to be considered the method to classify accurately, even if some error or wrong detection is mixed in the ball detection result.
* to evaluate a player’s or a team’s performance.
* to analyze 3D characteristics of the ball and to achieve automatic trajectory segmentation and classification. 

## BTC Work Process Overview
![work_process](/work_process.png)
  - Categorization method : I categorize the ball at each interval into one of *seven* trajectory classes, e.g., linear, parabolic, combination of linear and parabolic(l+p), combination of parabolic and linear(p+l), two different angles of parabolic(p+p), two different angles of linear(l+l) and unclassifiable.

  1.  First of all, I create an artificial ball video.
  2.  I train a classification model with the extracted features.
  3.  Based on a real soccer game video (input video), I detect the ball and extract the ball's position data. During this process, I decompose the video into a fixed number of frames per second (FPS = 25 in my case).
  4. With the position data, I extract the features (velocity, acceleration, jerk, and moving average...) needed for the classification.
  5.  Finally, I predict the ball's trajectory with the trained predictor.

## BTC Code Files Architecture Overview 
![architecture](/BTC_architecture.png)
- Directories
1. input/ 
   - *video.mp4* : artificial ball video
   - *original_coordinates.csv* : ball position data of video.mp4
   - *annotations.csv* : ball trajectory data of video.mp4

   - *challengeset_video.mp4* : input video used with the trained model in the future

2. working/
   - *features.csv* : extracted feature data (velocity, acceleration, jerk,,,) from *'original_coordinates.csv' file*.
   - *normalized_Xtest_features.csv* : normalized X test data.

   - *tracked_coordinates_challengeset_video.csv* : tracked ball position data of the input video from using yoloV5.
   - *features_challengeset.csv* : extracted feature data (velocity, acceleration, jerk,,,) from *'tracked_coordinates_challengeset_video.csv'* file.
   - *normalized_Xtest_features_challengeset.csv*  : normalized X test data of the input video. 

3. trained/
   - *btc_saved_scaler.pkl* : scaler for normalizing features.
   - *btc_saved_predictor.pkl* : trained model predictor.

4. output/
   - *btc_prediction.csv* : ball trajectory prediction result of input video.

- Source files
1. *btc_dataset_generator.ipynb* : to generate an artificial ball video used to train a machine-learning model.
2. *btc_trainer.ipynb* : to extract neccessary features and to train the model.
3. *btc_predictor.ipynb* : to make a new prediction with a new input video and the trained model.
4. *btc_yolo_ball_tracker.ipynb* : to detect the ball position in the input video using yoloV5. 

