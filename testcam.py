import picamera

camera = picamera.PiCamera()
camera.rotation = 90
camera.start_preview()
while True: pass
camera.stop_preview()
