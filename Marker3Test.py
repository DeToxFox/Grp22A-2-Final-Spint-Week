# testing detecting a person in room 1 returning home and then
# returning to c/l of door 1 to carry on the course

room_one_type = 1  # fire
room_two_type = 2  # skip, poison
room_three_type = 3  # person
room_four_type = 1  # fire

marker_found = False


def room_three():
    # This will take the robot to the center of doorway, marker 3/doorway 3
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.41)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    # scan_for_marker()

    if (room_three_type == 3):
        # Going into the room after scanning the first marker
        chassis_ctrl.set_trans_speed(0.5)

        chassis_ctrl.move_with_distance(0, 4.65)  # original 4.65
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra

        # This scans for a person similar to scanning for a target
        scan_for_person_and_play_sound()
        print("There might be a person in there??")
        # Exit room
        # chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # original
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra

        return_to_start_of_course(1)  # NOTE: Part of Lesson 44 example
        # move_to_room_from_start(1)    # NOTE: Part of Lesson 44 example
        # else:
        #     (break):


def return_to_start_of_course(roomNum):
    if (roomNum == 1):
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.move_with_distance(-180, 4.65)  # original 4.65
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.41)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        move_to_room_from_start(1)

    # elif (roomNum == 2):


def move_to_room_from_start(roomNum):
    if (roomNum == 1):
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.41)

        chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
        chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(15)


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


def vision_recognized_marker_number_one(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    print("Weeee have a FIRE!!")
    # gun_ctrl.fire_once()
    marker_found = True


def vision_recognized_marker_number_two(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    # gun_ctrl.fire_once()
    print("Poison!!!!")
    marker_found = True


def vision_recognized_marker_number_three(msg):
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
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, -250)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 250)


def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Set the rotation speed of the gimbal and the speed of the robot in transit
    gimbal_ctrl.set_rotate_speed(100)  # added in extra
    chassis_ctrl.set_trans_speed(0.75)  # added in extra, 0.5 too slow, 0.70-0.75 ideal
    gimbal_ctrl.recenter()  # added in extra

    room_three()
