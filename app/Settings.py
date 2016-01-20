from enum import Enum

settings = {}

settings['comport'] = 3
settings['servoMinMicroseconds'] = 500
settings['servoMaxMicroseconds'] = 2500

settings['minTemp'] = -30
settings['maxTemp'] = 150

settings['lrServoMin'] = settings['servoMinMicroseconds']
settings['lrServoMax'] = settings['servoMaxMicroseconds']
settings['lrStep'] = 10
settings['lrServoCenter'] = (settings['lrServoMin'] + settings['lrServoMax'])/2
settings['lrSwapDirection'] = False

settings['udServoMin'] = settings['servoMinMicroseconds']
settings['udServoMax'] = settings['servoMaxMicroseconds']
settings['udStep'] = 10
settings['udServoCenter'] = (settings['udServoMin'] + settings['udServoMax'])/2
settings['udSwapDirection'] = False