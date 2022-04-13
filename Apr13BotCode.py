# Apr 13 code changes/fixes
# Scans taken out, either use scan for room or use room type not both, if
# you can get room types to work then go back and do bonus

room_one_type = 1  # fire
room_two_type = 2  # skip, poison
room_three_type = 3  # person
room_four_type = 1  # fire

marker_found = False


def room_one():
    #  This will take the robot to the center of doorway, marker 1/doorway 1
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.41)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    # scan_for_marker()

    if (room_one_type == 1):
        # Going into the first room after scanning the first marker

        chassis_ctrl.move_with_distance(0, 4.65)  # original 4.65
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        print("Wooh a FIRE!!! in room 1")
        scan_for_marker()
        # Exiting the room after putting out the fire, return to hallway
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 4.5)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        # Run to the ~~45 angle
        chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
        chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(15)
    # else:
    #     (break)


def room_two():
    # This will take the robot to the center of doorway, marker 2/doorway 2
    chassis_ctrl.move_with_distance(0, 4)
    chassis_ctrl.move_with_distance(0, 1.02)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    # scan_for_marker()

    if (room_two_type == 2):
        # This room is poison, continue on to the next room/position
        print("Poison not cool")
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra


def room_three():
    # This will take the robot to the center of doorway, marker 3/doorway 3
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.01)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    # scan_for_marker()

    if (room_three_type == 3):
        # Move to the target in room
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 1.21)

        # This scans for a person similar to scanning for a target
        scan_for_person_and_play_sound()
        print("There might be a person in there??")
        # Exit room
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 1.21)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.40)
        # chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90) # NOTE: This is because of person found
        # gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # NOTE: Will get the bot to room 4
        gimbal_ctrl.recenter()  # added in extra, for the purpose of the line above
        # return_to_start_of_course(1)  # NOTE: Part of Lesson 44 example
        # move_to_room_from_start(1)    # NOTE: Part of Lesson 44 example
        # else:
        #     (break):


def room_four():
    print("get ready for room 4")
    #  This will take the robot to the center of doorway, marker 1/doorway 4
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2)
    chassis_ctrl.move_with_distance(0, 3.25)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    # scan_for_marker()

    if (room_four_type == 1):
        print("Wooh a FIRE!!! in room 4")
        chassis_ctrl.move_with_distance(0, 2.70)  # was 2.60
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.32)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        scan_for_marker()
        # Exiting the room after putting out the fire, return to hallway
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.32)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.55)  # was 2.60
        # Call home function
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        return_home()
    # else:
    #     (break)


def return_home():
    chassis_ctrl.set_trans_speed(1.5)  # added in extra, might be a touch fast, but seems like it runs better up to 45 deg
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.28)  # This takes the bot back to the 45 angle
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
    gimbal_ctrl.recenter()  # added in extra
    chassis_ctrl.set_trans_speed(0.5)  # slow the bot down for short angles
    chassis_ctrl.move_with_distance(0, 2.70)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)
    gimbal_ctrl.recenter()  # added in extra
    # Sleep timer would go here
    time.sleep(15)
    chassis_ctrl.set_trans_speed(0.75)  # to finish line, 1.5 is too fast, so try 0.75
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.0)
    chassis_ctrl.move_with_distance(0, 1.01)
    chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    gimbal_ctrl.recenter()  # added in extra


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
    gimbal_ctrl.set_rotate_speed(80)  # added in extra
    chassis_ctrl.set_trans_speed(0.75)  # added in extra, 0.5 too slow, 0.70-0.75 ideal
    gimbal_ctrl.recenter()  # added in extra
    room_one()
    room_two()
    room_three()
    room_four()