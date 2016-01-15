from enum import Enum

settings = {}

settings['servoMinMicroseconds'] = 500
settings['servoMaxMicroseconds'] = 2500

settings['lrServoMin'] = settings['servoMinMicroseconds']
settings['lrServoMax'] = settings['servoMaxMicroseconds']
settings['lrServoCenter'] = (settings['lrServoMin'] + settings['lrServoMax'])/2
settings['lrSwapDirection'] = False

settings['udServoMin'] = settings['servoMinMicroseconds']
settings['udServoMax'] = settings['servoMaxMicroseconds']
settings['udServoCenter'] = (settings['udServoMin'] + settings['udServoMax'])/2
settings['udSwapDirection'] = False