## Rust Detector
**A real-time rust detection system aimed at improving railway track safety standards.**  
This project uses computer vision techniques to detect rust on railway tracks in real-time. It provides a cost-effective solution for maintaining track quality by identifying rust-affected areas using a webcam.

### Features:
- **Real-time detection**: Capture and detect rust using a webcam.
- **Highlighting rust areas**: Red rectangles mark rust-affected regions in the video stream.
- **Configurable HSV settings**: Easily adjust the color range to fine-tune rust detection.

### Libraries and Concepts Used:
- **OpenCV**: For image processing, video capture, and contour detection.
- **HSV Color Space**: Used to define the color range for rust detection.
- **Contour Detection**: Identifies and highlights rust-affected areas.

### Usage:
1. Ensure your webcam is connected.
2. Adjust the HSV color range in the code if necessary to match the lighting conditions and rust color.
3. Run the script, and the detected rust areas will be highlighted with red rectangles in the video stream.
4. Press the 'q' key to exit the program.

### Future Enhancements:
- Integrate machine learning models for more advanced pattern recognition and improved accuracy.
- Improve detection in varying environmental conditions like low light or rain.
