# April 19, 2022 Robot Code

num_marker_one = False
num_marker_two = False
num_marker_three = False
marker_found = False


def room_one():
    # This will take the robot to the center of doorway, doorway 1
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.41)
    # Rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    scan_for_marker()

    if (num_marker_one == True):  # This is if room 1 is fire
        print("room 1 marker 1")
        # Going into the room after scanning the first marker
        chassis_ctrl.set_trans_speed(0.5)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 4.65)  # original 4.65
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        scan_for_marker()  # Scans for F Marker

        # Exit room 1
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(-180, 4.65)  # original 4.65
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra

        # Move to the Manual Reset Point
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
        chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(10)

    elif (num_marker_two == True):  # This is if room 1 is poison
        print("room 1 marker 2")
        chassis_ctrl.set_trans_speed(0.75)
        # This room is poison, continue on to the next room/position
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        # Move to the Manual Reset Point
        chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
        chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(10)

    elif (num_marker_three == True):  # This is if room 1 has a person
        print("room 1 marker 3")
        chassis_ctrl.set_trans_speed(0.5)
        # Move to target inside the room
        chassis_ctrl.move_with_distance(0, 4.65)  # original 4.65
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra

        # This scans for a person similar to scanning for target F
        scan_for_person_and_play_sound()
        print("There might be a person in there??")
        # Exit room
        # chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # original
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra

        return_to_start_of_course(1)  # NOTE: Part of Lesson 44 example


def room_two():
    #  This will take the robot to the center of doorway, doorway 2 from manual reset point
    chassis_ctrl.set_trans_speed(0.75)
    chassis_ctrl.move_with_distance(0, 4)
    chassis_ctrl.move_with_distance(0, 1.29)  # original was 1.02
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    scan_for_marker()

    if (num_marker_one == True):
        print("room 2 marker 1")
        # This is if room 2 is fire
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1)
        chassis_ctrl.move_with_distance(0, 4.02)
        # Calls the "Scan for a marker" function
        scan_for_marker()

        # Exit room 2
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 1)
        chassis_ctrl.move_with_distance(0, 4.02)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # positioning for room 3
        gimbal_ctrl.recenter()

    elif (num_marker_two == True):  # This is if room 2 is poison
        print("room 2 marker 2")
        # This room is poison, rotate and get ready to have "start" call room 3
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra


    elif (num_marker_three == True):  # This is if room 2 has a person
        print("room 2 marker 3")
        # @ this time we dont know if this room will have a person in it
        # Going into the room after scanning the first marker
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1)
        chassis_ctrl.move_with_distance(0, 4.02)

        # This scans for a person similar to scanning for target F
        scan_for_person_and_play_sound()
        print("There might be a person in there??")
        # Exit room 2
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()  # added in extra

        return_to_start_of_course(2)  # NOTE: Part of Lesson 44 example


def room_three():
    # This will take the robot to the center of doorway, doorway 3
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 4.01)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()  # added in extra
    # Calls the "Scan for a marker" function
    scan_for_marker()

    if (num_marker_one == True):  # This is if room 3 is fire
        print("room 3 marker 1")
        # Going into the room after scanning the first marker
        chassis_ctrl.set_trans_speed(0.75)
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
        scan_for_marker()  # Scans for F Marker

        # Exit room 3
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
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # Positioning to move to room 4
        gimbal_ctrl.recenter()  # added in extra

    elif (num_marker_two == True):  # This is if room 3 is poison
        print("room 3 marker 2")
        # This room is poison, rotate and get ready to have "start" call room 4
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()  # added in extra

    elif (num_marker_three == True):  # This is if room 3 has a person
        print("room 3 marker 3")
        chassis_ctrl.set_trans_speed(0.75)

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

        # This scans for a person similar to scanning for target F
        scan_for_person_and_play_sound()
        print("There might be a person in there??")
        # Exit room
        gimbal_ctrl.recenter()  # added in extra

        return_to_start_of_course(3)  # NOTE: Part of Lesson 44 example


def return_to_start_of_course(roomNum):
    if (roomNum == 1):
        print("return to start from room 1")
        # Exit room 1
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.move_with_distance(-180, 4.65)  # original 4.65
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.41)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        # Manual Reset then moving back to the room
        time.sleep(10)
        move_to_room_from_start(1)

    elif (roomNum == 2):
        print("return to start from room 2")
        # Exit room 2
        chassis_ctrl.move_with_distance(0, 1)
        chassis_ctrl.move_with_distance(0, 4.02)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # positioning to go back to manual reset point
        gimbal_ctrl.recenter()
        # Return to manual reset point and then home/start
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.29)  # original was 1.02
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        # Sleep timer
        time.sleep(10)
        # Return home
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.0)
        chassis_ctrl.move_with_distance(0, 1.01)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(10)
        move_to_room_from_start(2)

    elif (roomNum == 3):
        print("return to start from room 3")
        # Exit room 3
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
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # NOTE: This is because of person found
        gimbal_ctrl.recenter()  # added in extra
        # Return to manual reset point and then home/start
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.37)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        # Sleep timer
        time.sleep(10)
        # Return home
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.0)
        chassis_ctrl.move_with_distance(0, 1.01)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(10)
        move_to_room_from_start(3)
    # elif (roomNum == 4):
    # Exit room 2
    # chassis_ctrl.set_trans_speed(0.75)
    # chassis_ctrl.move_with_distance(-180, 4.65)  #  original 4.65
    # chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    # gimbal_ctrl.recenter()  # added in extra
    # chassis_ctrl.move_with_distance(0, 5)
    # chassis_ctrl.move_with_distance(0, 2.41)
    # chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
    # gimbal_ctrl.recenter()
    # move_to_room_from_start(4)


def move_to_room_from_start(roomNum):
    if (roomNum == 1):  # moving back to room 1 from start
        print("return to room 1 from start")
        chassis_ctrl.set_trans_speed(0.75)  # added in extra, 0.5 too slow, 0.70-0.75 ideal
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.41)
        # Move to the Manual Reset Point
        chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
        chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(10)  # once this "if" block is complete, "start" will call room 2

    elif (roomNum == 2):  # moving back to room 2 from start
        print("return to room 2 from start")
        chassis_ctrl.set_trans_speed(0.75)  # added in extra, 0.5 too slow, 0.70-0.75 ideal
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.41)
        # Move to the Manual Reset Point
        chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
        chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(10)
        # from the Manual Resest Point to room 2
        chassis_ctrl.move_with_distance(0, 4)
        # original was 1.02, once this "elif" block is complete, "start" will call room 3
        chassis_ctrl.move_with_distance(0, 1.29)

    elif (roomNum == 3):  # moving back to room 3 from start
        print("return to room 3 from start")
        chassis_ctrl.set_trans_speed(0.75)  # added in extra, 0.5 too slow, 0.70-0.75 ideal
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.41)
        # Move to the Manual Reset Point
        chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
        chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()  # added in extra
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()  # added in extra
        time.sleep(10)
        # from the Manual Resest Point to room 2
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.29)
        # from room 2 to room 3
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.08)  # once this "elif" block is complete, "start" will call room 4

    # elif (roomNum == 4):
    # chassis_ctrl.move_with_distance(0, 5)
    # chassis_ctrl.move_with_distance(0, 2.41)

    # chassis_ctrl.move_with_distance(0, 5)  # to first part of 45 angle
    # chassis_ctrl.move_with_distance(0, 2.6)  # to first part of 45 angle
    # chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
    # gimbal_ctrl.recenter()  # added in extra
    # chassis_ctrl.move_with_distance(0, 2.70)
    # chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
    # gimbal_ctrl.recenter()  # added in extra
    # time.sleep(15)


def vision_recognized_marker_number_one(msg):  # this will be for fire
    global marker_found
    global num_marker_one
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    print("Weeee have a FIRE!!")
    marker_found = True
    num_marker_one = True


def vision_recognized_marker_number_two(msg):  # this will be for poison
    global marker_found
    global num_marker_two
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    # gun_ctrl.fire_once()
    print("Poison!!!!")
    marker_found = True
    num_marker_two = True


def vision_recognized_marker_number_three(msg):  # this will be if it's a person
    global marker_found
    global num_marker_three
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    print("3 Marker Found!")
    marker_found = True
    num_marker_three = True


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
    person_found = False
    while person_found == False:
        # maybe move these lines above person_false, if im not on f mark it wont rotate
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)


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


def start():
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Set the rotation speed of the gimbal and the speed of the robot in transit
    gimbal_ctrl.set_rotate_speed(80)  # added in extra
    chassis_ctrl.set_trans_speed(0.75)  # added in extra, 0.5 too slow, 0.70-0.75 ideal
    gimbal_ctrl.recenter()  # added in extra

    room_one()
    num_marker_one = False
    num_marker_two = False
    num_marker_three = False

    room_two()
    num_marker_one = False
    num_marker_two = False
    num_marker_three = False

    room_three()
    num_marker_one = False
    num_marker_two = False
    num_marker_three = False

    # room_four()
    # num_marker_one = False
    # num_marker_two = False
    # num_marker_three = False