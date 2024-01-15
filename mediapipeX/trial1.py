import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('hand landmarker result: {}'.format(result))

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='/path/to/model.task'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with HandLandmarker.create_from_options(options) as landmarker:
  # The landmarker is initialized. Use it here.
  # ...
    import mediapipe as mp

# Use OpenCV’s VideoCapture to start capturing from the webcam.

# Create a loop to read the latest frame from the camera using VideoCapture#read()

# Convert the frame received from OpenCV to a MediaPipe’s Image object.
mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=numpy_frame_from_opencv)
    # Send live image data to perform hand landmarks detection.
# The results are accessible via the `result_callback` provided in
# the `HandLandmarkerOptions` object.
# The hand landmarker must be created with the live stream mode.
landmarker.detect_async(mp_image, frame_timestamp_ms)
HandLandmarkerResult:
    Handedness:
        Categories #0:
        index        : 0
        score        : 0.98396
        categoryName : Left
    Landmarks:
        Landmark #0:
        x            : 0.638852
        y            : 0.671197
        z            : -3.41E-7
        Landmark #1:
        x            : 0.634599
        y            : 0.536441
        z            : -0.06984
        ... (21 landmarks for a hand)
    WorldLandmarks:
        Landmark #0:
        x            : 0.067485
        y            : 0.031084
        z            : 0.055223
        Landmark #1:
        x            : 0.063209
        y            : -0.00382
        z            : 0.020920
        ... (21 world landmarks for a hand)