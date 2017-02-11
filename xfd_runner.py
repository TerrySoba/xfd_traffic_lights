import traffic_lights
import travis_ci_client
import time

print("Running TravisCI XFD...")

lights = traffic_lights.TrafficLights("clewarecontrol", "902971")

greenCount = 0

while True:
    buildSuccess = travis_ci_client.travisCiBuildWasSuccessfull("TerrySoba", "retro-game", "master")
    if buildSuccess:
        greenCount += 1
        print("Travis CI build was a success.")
        if (greenCount < 5):
            lights.setLights(False, False, True)
        else:
            lights.setLights(False, False, False)
    else:
        greenCount = 0
        print("Travis CI build failed.")
        lights.setLights(True, False, False)

    time.sleep(60)

