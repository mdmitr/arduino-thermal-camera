
class ArduinoCtrl():

    def __init__(self):
        self.mPosX = -1  # current X position in camera image
        self.mPosY = -1  # current Y position in camera image
        self.mMinX = -1  # minimum X position in camera image
        self.mMaxX = -1  # maximum X position in camera image
        self.mMinY = -1  # minimum Y position in camera image
        self.mMaxY = -1  # maximum Y position in camera image

        # servos settings (to be calibrated)
        self.mServoMinX = -1
        self.mServoMaxX = -1
        self.mServoMinY = -1
        self.mServoMaxY = -1

        # Images
        self.mCameraImage = None     # image from web camera (set externally)
        self.mThermalImage = None    # thermal image
        return

    def MoveToPoint(self, x, y):
        return

    def CalibrateTopLeft(self, x, y):
        return false

    def CalibrateBottomRight(self, x, y):
        return false

    def MeasureTemperature(self, x, y):
        return 0
