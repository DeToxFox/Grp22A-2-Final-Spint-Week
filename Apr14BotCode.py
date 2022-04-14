# File Name =  FinalBotCode
# The following code will be the scan rooms 1 - 4
# where markers could be any designation

marker_found = False


def room_one():
    # vision_recognized_marker_number_one = 1 # fire
    # vision_recognized_marker_number_two = 2 # poison
    # vision_recognized_marker_number_three = 3 # person
    # ops = vision_recognized_marker_number_one(msg)

    #  This will take the robot to the center of doorway, marker 1/doorway 1
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.41)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    scan_for_marker()

    # if(room_one_type == 1):
    #     # Going into the first room after scanning the first marker
    #     gimbal_ctrl.recenter()  # added in extra
    #     chassis_ctrl.move_with_distance(0, 4.65)  #  original 4.65
    #     scan_for_marker()
    #     #vision_recognized_marker_letter_F(msg):
    #     # Exiting the room after putting out the fire
    #     chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    #     gimbal_ctrl.recenter()  # added in extra
    #     chassis_ctrl.move_with_distance(0, 4.65)
    #     chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    #     gimbal_ctrl.recenter()  # added in extra

    # elif(room_one_type == 2):
    #     vision_recognized_marker_number_two()
    #     # This room is poison, continue on to the next room/position
    #     chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    #     gimbal_ctrl.recenter()  # added in extra
    #     # Run to the ~~45 angle
    #     chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
    #     chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
    #     chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
    #     gimbal_ctrl.recenter()  # added in extra
    #     chassis_ctrl.move_with_distance(0, 2.70)
    #     chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
    #     gimbal_ctrl.recenter()  # added in extra

    # elif(room_one_type == 3):
    #     # Going into the first room after scanning the first marker
    #     gimbal_ctrl.recenter()  # added in extra
    #     chassis_ctrl.move_with_distance(0, 4.65)
    #     scan_for_person_and_play_sound()
    #     # Exit room
    #     chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    #     gimbal_ctrl.recenter()  # added in extra
    #     chassis_ctrl.move_with_distance(0, 4.65)
    #     chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    #     gimbal_ctrl.recenter()  # added in extra
    #     return_to_start_of_course(1)
    #     move_to_room_from_start(1)

    # if(vision_recognized_marker_number_one(ops) == 1):
    # Going into the first room after scanning the first marker

    # chassis_ctrl.move_with_distance(0, 4.65)  #  original 4.65
    #     chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    #     gimbal_ctrl.recenter()  # added in extra
    #     print("Wooh a FIRE!!! in room 1")
    #     scan_for_marker()
    # # Exiting the room after putting out the fire, return to hallway
    #     chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
    #     gimbal_ctrl.recenter()  # added in extra
    #     chassis_ctrl.move_with_distance(0, 4.5)
    #     chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    #     gimbal_ctrl.recenter()  # added in extra
    #  # Run to the ~~45 angle
    #     chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
    #     chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
    #     chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
    #     gimbal_ctrl.recenter()  # added in extra
    #     chassis_ctrl.move_with_distance(0, 2.70)
    #     chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
    #     gimbal_ctrl.recenter()  # added in extra
    #     time.sleep(15)


def scan_for_marker():
    # Turn on detection and scan left and right until you hit a marker. global marker_found
    global marker_found  # Note: this had to be added in to force the validation to true once the marker is found,
    # then as it is evaluated "While True (marker_found) == False" since true is not same as
    # false then it will break out of the while loop.
    gimbal_ctrl.pitch_ctrl(7)  # Added in
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    marker_found = False
    while marker_found == False:
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)


def vision_recognized_marker_number_one(msg):  # this will be for fire
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    print("Weeee have a FIRE!!")
    # list = []
    # list.append_text(detect_marker_and_aim)
    # detect_marker_and_aim = 1
    # detect_marker_and_aim = 2
    # detect_marker_and_aim = 3
    if (detect_marker_and_aim == 2):
        print("Poison Run!!")
    elif (detect_marker_and_aim == 1):
        print("fire fire!!!")
    elif (detect_marker_and_aim == 3):
        print("person")
    # gun_ctrl.fire_once()
    marker_found = True


def vision_recognized_marker_number_two(msg):  # this will be for poison
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    # gun_ctrl.fire_once()
    print("Poison!!!!")
    marker_found = True


def vision_recognized_marker_number_three(msg):  # this will be if it's a person
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    print("3 Marker Found!")
    marker_found = True


def vision_recognized_marker_letter_F(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    print("F Marker Found!")
    marker_found = True


def vision_recognized_people(msg):
    global person_found
    vision_ctrl.disable_detection(rm_define.vision_detection_people)
    media_ctrl.play_sound(rm_define.media_sound_attacked)
    person_found = True


def scan_for_person_and_play_sound():
    global person_found
    vision_ctrl.enable_detection(rm_define.vision_detection_people)
    # having rotation before person_found=false stopped the program from progressing
    # gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, -250)
    # gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 250)
    person_found = False
    while person_found == False:
        # maybe move these lines above person_false, if im not on f mark it wont rotate
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)


def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Set the rotation speed of the gimbal and the speed of the robot in transit
    gimbal_ctrl.set_rotate_speed(100)  # added in extra
    chassis_ctrl.set_trans_speed(1.5)  # added in extra, 0.5 too slow, 0.70-0.75 ideal
    gimbal_ctrl.recenter()  # added in extra
    # room_one = 1
    # room_one = 2
    # room_one = 3
    # room_two = 1
    # room_two = 2
    # room_two = 3

    room_one()
    # room_two()
    # room_three()
    # room_four()


