import cv2
import subprocess
import logging

logging.basicConfig(filename='/home/pi/crosshair_camera.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting crosshair_camera.py")

try:
    # Initialize camera
    logging.info("Initializing camera...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logging.error("Failed to open camera")
        exit(1)
    logging.info("Camera initialized successfully")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Create a named window that can be resized
    logging.info("Creating named window...")
    cv2.namedWindow('AWM Crosshair', cv2.WINDOW_NORMAL)
    logging.info("Named window created")

    # Attempt to set the window to fullscreen using OpenCV
    try:
        logging.info("Attempting fullscreen with OpenCV...")
        cv2.setWindowProperty('AWM Crosshair', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        logging.info("Fullscreen attempt complete")
    except Exception as e:
        logging.error(f"Error setting fullscreen: {e}")

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.error("Failed to read frame")
            break

        # Draw crosshair
        h, w = frame.shape[:2]
        center = (w//2, h//2)
        color = (0, 255, 0)  # Green color for the crosshair

        # Draw vertical line
        cv2.line(frame, (center[0], center[1]-20), (center[0], center[1]+20), color, 2)
        # Draw horizontal line
        cv2.line(frame, (center[0]-20, center[1]), (center[0]+20, center[1]), color, 2)

        cv2.imshow('AWM Crosshair', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            logging.info("Quit key pressed")
            break

    cap.release()
    cv2.destroyAllWindows()
    logging.info("Exiting successfully")

except Exception as e:
    logging.error(f"An unexpected error occurred: {e}", exc_info=True)
    exit(1)