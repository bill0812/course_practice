import tellopy
from time import sleep


def handler(event, sender, data, **args):
    send_msg = sender
    
    if event is send_msg.EVENT_FLIGHT_DATA :
        print('record_log: %s: %s' % (event.name, str(data)))

def main():
    # 建立 tellopy.Tello 物件
    drone = tellopy.Tello()

    # # connect to tello
    drone.connect()

    # # wait few seconds for connection via wifi
    drone.wait_for_connection(20.0)

    # drone.subscribe
    # drone.subscribe(drone.EVENT_FILE_RECEIVED,handler)

#     drone.take_picture()
#     sleep(30)

    # tello take off and sleep
    drone.takeoff()
    sleep(10)

    drone.forward(17)
    sleep(5)
    drone.forward(0)
    sleep(5)

    drone.clockwise(32.0)
    sleep(5)
    drone.clockwise(0.0)
    sleep(5)

    drone.forward(17)
    sleep(5)
    drone.forward(0)
    sleep(5)

    drone.clockwise(32.0)
    sleep(5)
    drone.clockwise(0.0)
    sleep(5)

    drone.forward(17)
    sleep(5)
    drone.forward(0)
    sleep(5)

    drone.clockwise(32.0)
    sleep(5)
    drone.clockwise(0.0)
    sleep(5)

    drone.forward(17)
    sleep(5)
    drone.forward(0)
    sleep(5)

    drone.clockwise(32.0)
    sleep(5)
    drone.clockwise(0.0)
    sleep(5)

#     drone.forward(20)
#     sleep(5)
#     drone.forward(0)
#     sleep(5)

#     drone.clockwise(90.0)
#     sleep(5)
#     drone.clockwise(0.0)
#     sleep(10)

#     drone.forward(20)
#     sleep(5)
#     drone.forward(0)
#     sleep(5)

#     drone.clockwise(90.0)
#     sleep(10)
#     drone.clockwise(0.0)
#     sleep(10)

#     drone.forward(20)
#     sleep(10)
#     drone.forward(0)
#     sleep(5)

#     drone.clockwise(60.0)
#     sleep(10)

    # tello up and sleep
#     drone.up(20)
#     sleep(5)

#     drone.up(0)
#     sleep(5)

#     # tello down and sleep
#     drone.down(20)
#     sleep(5)

#     # tello right and sleep
#     drone.right(20)
#     sleep(5)

#     # tello right and sleep
#     drone.right(0)
#     sleep(5)

#     drone.clockwise(90.0)
#     sleep(10)

#     # tello left and sleep
#     drone.left(20)
#     sleep(5)

#     drone.left(0)
#     sleep(5)

#     drone.clockwise(90.0)
#     sleep(10)

#     # tello flip backleft
#     drone.flip_backleft()

    # tello land and sleep
    drone.land()
    sleep(5)

    # quit tello
    drone.quit()

if __name__ == '__main__':
    # 觀看套件詳細說明
    help(tellopy)
    main()