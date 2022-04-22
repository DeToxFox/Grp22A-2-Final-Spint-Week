# Project 3: Robot Obstacle Course

# Written by: Group 22A-2, Makenzie Roberts, Tyler Dinn, and David Turner
# Date written: April 11, 2022
# Project ID: Final Sprint Week. Project 3: Robot Obstacle Course

num_marker_one = False
num_marker_two = False
num_marker_three = False
media_custom_audio_0 = False
media_custom_audio_4 = False
media_custom_audio_1 = False
media_custom_audio_2 = False
marker_found = False


def room_one():
    # This will take the robot to the center of doorway, doorway 1
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2.20)
    # Rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Calls the "Scan for a marker" function
    scan_for_marker()

    if (num_marker_one == True):  # This is if room 1 is fire
        print("room 1 marker 1")
        # Going into the room after scanning the first marker
        chassis_ctrl.set_trans_speed(0.75)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.65)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        scan_for_marker()  # Scans for F Marker

        # Exit room 1
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(-180, 4.65)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()

        # Move to the Manual Reset Point
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.move_with_distance(0, 5)  # take the robot to first part of 45 deg angle
        chassis_ctrl.move_with_distance(0, 2.6)  # ~45 deg distance
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()
        time.sleep(10)

    elif (num_marker_two == True):  # This is if room 1 is poison
        print("room 1 marker 2")
        chassis_ctrl.set_trans_speed(0.88)
        # This room is poison, continue on to the next room/position
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        # Move to the Manual Reset Point
        chassis_ctrl.move_with_distance(0, 5)  # take the robot to first part of 45 deg angle
        chassis_ctrl.move_with_distance(0, 2.6)  # ~45 deg distance
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()
        time.sleep(10)

    elif (num_marker_three == True):  # This is if room 1 has a person
        print("room 1 marker 3")
        chassis_ctrl.set_trans_speed(0.75)
        # Move to target inside the room
        chassis_ctrl.move_with_distance(0, 4.65)  # original 4.65
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()

        # This scans for a person similar to scanning for target F
        scan_for_person_and_play_sound()

        # Exit room 1
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        return_to_start_of_course(1)


def room_two():
    #  This will take the robot to the center of doorway, doorway 2 from manual reset point
    chassis_ctrl.set_trans_speed(0.88)
    chassis_ctrl.move_with_distance(0, 4)
    chassis_ctrl.move_with_distance(0, 1.19)  # original was 1.02, second was at 1.29
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Calls the "Scan for a marker" function
    scan_for_marker()

    if (num_marker_one == True):  # This is if room 2 is fire
        print("room 2 marker 1")
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1)
        chassis_ctrl.move_with_distance(0, 4.02)
        # Calls the "Scan for a marker" function
        scan_for_marker()

        # Exit room 2
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1)
        chassis_ctrl.move_with_distance(0, 4.02)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # positioning for room 3
        gimbal_ctrl.recenter()

    elif (num_marker_two == True):  # This is if room 2 is poison
        print("room 2 marker 2")
        # This room is poison, rotate and get ready to have "start" call room 3
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()


    elif (num_marker_three == True):  # This is if room 2 has a person
        print("room 2 marker 3")
        # Going into the room after scanning the first marker
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1)
        chassis_ctrl.move_with_distance(0, 4.02)

        # This scans for a person similar to scanning for target F
        scan_for_person_and_play_sound()

        # Exit room 2
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()
        return_to_start_of_course(2)


def room_three():
    # This will take the robot to the center of doorway, doorway 3
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 3.97)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Calls the "Scan for a marker" function
    scan_for_marker()

    if (num_marker_one == True):  # This is if room 3 is fire
        print("room 3 marker 1")
        # Going into the room after scanning the first marker
        chassis_ctrl.set_trans_speed(0.88)
        # Move to the target in room
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.21)
        scan_for_marker()  # Scans for F Marker

        # Exit room 3
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.21)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)  # Positioning to move to room 4
        gimbal_ctrl.recenter()

    elif (num_marker_two == True):  # This is if room 3 is poison
        print("room 3 marker 2")
        # This room is poison, rotate and get ready to have "start" call room 4
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()

    elif (num_marker_three == True):  # This is if room 3 has a person
        print("room 3 marker 3")
        chassis_ctrl.set_trans_speed(0.88)
        gimbal_ctrl.recenter()
        # Move to the target in room
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.21)

        # This scans for a person similar to scanning for target F
        scan_for_person_and_play_sound()

        # Exit room 3
        return_to_start_of_course(3)


def room_four():
    # This will take the robot to the center of doorway, doorway 4
    chassis_ctrl.move_with_distance(0, 5)
    chassis_ctrl.move_with_distance(0, 2)
    chassis_ctrl.move_with_distance(0, 3.25)
    # rotate to face the door
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    # Calls the "Scan for a marker" function
    scan_for_marker()

    if (num_marker_one == True):  # This is if room 4 is fire
        print("room 4 marker 1")
        # Going into the room after scanning the first marker
        chassis_ctrl.set_trans_speed(0.88)
        # Move to the target in room
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.30)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        scan_for_marker()  # Scans for F Marker

        # Exiting room 4 after putting out the fire, return to hallway
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.30)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)

        # This will call return to start function
        return_to_start_of_course(4)

    elif (num_marker_two == True):  # This is if room 4 is poison
        print("room 4 marker 2")
        # This room is poison, rotate and get ready to have the robot return to start
        chassis_ctrl.set_trans_speed(0.88)
        return_to_start_of_course(4)

    elif (num_marker_three == True):  # This is if room 4 has a person
        print("room 4 marker 3")
        gimbal_ctrl.recenter()
        chassis_ctrl.set_trans_speed(0.88)

        # Move to the target in room 4
        chassis_ctrl.move_with_distance(0, 2.70)  # was 2.60
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.30)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()

        # This scans for a person similar to scanning for target F
        scan_for_person_and_play_sound()

        # Exiting room 4 after finding a person, return to hallway
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.30)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)  # was 2.60
        # This will call return to start
        return_to_start_of_course(4)


def return_to_start_of_course(roomNum):
    if (roomNum == 1):
        print("This is room # ", roomNum)
        print("return to start from room 1")
        # Exit room 1
        chassis_ctrl.set_trans_speed(0.75)
        chassis_ctrl.move_with_distance(-180, 4.65)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.41)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        # Manual Reset then moving back to the room
        time.sleep(10)
        move_to_room_from_start(1)

    elif (roomNum == 2):
        print("This is room # ", roomNum)
        print("return to start from room 2")
        # Exit room 2
        chassis_ctrl.move_with_distance(0, 1)
        chassis_ctrl.move_with_distance(0, 4.02)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # positioning to go back to manual reset point
        gimbal_ctrl.recenter()
        # Return to manual reset point and then home/start
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.29)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)
        gimbal_ctrl.recenter()
        # Sleep timer
        time.sleep(10)
        # Return home
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.0)
        chassis_ctrl.move_with_distance(0, 1.01)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        time.sleep(10)
        move_to_room_from_start(2)

    elif (roomNum == 3):
        print("This is room # ", roomNum)
        print("return to start from room 3")
        # Exit room 3
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 180)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.21)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 4.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 1.50)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.40)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)  # NOTE: This is because of person found
        gimbal_ctrl.recenter()
        # Return to manual reset point and then home/start
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.37)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)
        gimbal_ctrl.recenter()
        # Sleep timer
        time.sleep(10)
        # Return home
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 4.0)
        chassis_ctrl.move_with_distance(0, 1.01)
        chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
        gimbal_ctrl.recenter()
        time.sleep(10)
        move_to_room_from_start(3)

    elif (roomNum == 4):
        print("This is room # ", roomNum)
        # This "if" statement evaluates if its room 4 and marker 2 (poison) and return home
        if roomNum == 4 and num_marker_two == True:
            print("IF room 4 AND IF marker IS 2/Poison")
            chassis_ctrl.set_trans_speed(0.88)
            chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
            gimbal_ctrl.recenter()
            # Return to manual reset point and then start
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 2)
            chassis_ctrl.move_with_distance(0, 3.25)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 4.37)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
            gimbal_ctrl.recenter()
            chassis_ctrl.move_with_distance(0, 2.70)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)
            gimbal_ctrl.recenter()
            # Sleep timer
            time.sleep(10)
            # Return start
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 4.0)
            chassis_ctrl.move_with_distance(0, 1.01)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
            gimbal_ctrl.recenter()
            happy_dance()

        # After exiting room 4 after fighting a fire or finding a person and returning to start
        else:
            print("ELSE its not poison there was a fire or a person in the room")
            chassis_ctrl.set_trans_speed(0.88)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 90)
            gimbal_ctrl.recenter()
            # Return to manual reset point and then start
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 2)
            chassis_ctrl.move_with_distance(0, 3.25)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 4.37)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 40)
            gimbal_ctrl.recenter()
            chassis_ctrl.move_with_distance(0, 2.70)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 50)
            gimbal_ctrl.recenter()
            # Sleep timer
            time.sleep(10)
            # Return start
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 5)
            chassis_ctrl.move_with_distance(0, 4.0)
            chassis_ctrl.move_with_distance(0, 1.01)
            chassis_ctrl.rotate_with_degree(rm_define.clockwise, 180)
            gimbal_ctrl.recenter()
            happy_dance()  # calls the function for the victory dance


def move_to_room_from_start(roomNum):
    if (roomNum == 1):  # moving back to room 1 from start
        print("return to room 1 from start")
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.20)
        # Move to the Manual Reset Point
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.6)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()
        time.sleep(10)  # once this "if" block is complete, "start" will call room 2

    elif (roomNum == 2):  # moving back to room 2 from start
        print("return to room 2 from start")
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.31)
        # Move to the Manual Reset Point
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.6)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()
        time.sleep(10)
        # from the Manual Resest Point to room 2
        chassis_ctrl.move_with_distance(0, 4)
        # once this "elif" block is complete, "start" will call room 3
        chassis_ctrl.move_with_distance(0, 1.19)

    elif (roomNum == 3):  # moving back to room 3 from start
        print("return to room 3 from start")
        chassis_ctrl.set_trans_speed(0.88)
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.31)
        # Move to the Manual Reset Point
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 2.6)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 50)
        gimbal_ctrl.recenter()
        chassis_ctrl.move_with_distance(0, 2.70)
        chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 40)
        gimbal_ctrl.recenter()
        time.sleep(10)
        # from the Manual Resest Point to room 2
        chassis_ctrl.move_with_distance(0, 4)
        chassis_ctrl.move_with_distance(0, 1.29)
        # from room 2 to room 3
        chassis_ctrl.move_with_distance(0, 5)
        chassis_ctrl.move_with_distance(0, 3.97)  # once this "elif" block is complete, "start" will call room 4


# there is no returning to room 4 as that is the last room in the course and once any marker is scanned at room 4
# the robot returns to the start for the last time

def vision_recognized_marker_number_one(msg):  # this will be for fire
    global marker_found
    global num_marker_one
    global media_custom_audio_4
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_flash)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_one)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    media_ctrl.play_sound(rm_define.media_custom_audio_4, wait_for_complete_flag=True)
    print("There is a FIRE!!")
    marker_found = True
    num_marker_one = True
    media_custom_audio_4 = True
    led_ctrl.turn_off(rm_define.armor_all)


def vision_recognized_marker_number_two(msg):  # this will be for poison
    global marker_found
    global num_marker_two
    global media_custom_audio_2
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 193, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 193, 0, rm_define.effect_flash)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_two)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    media_ctrl.play_sound(rm_define.media_custom_audio_2, wait_for_complete_flag=True)
    media_ctrl.play_sound(rm_define.media_custom_audio_2, wait_for_complete_flag=True)
    print("Poison, move on")
    marker_found = True
    num_marker_two = True
    media_custom_audio_2 = True
    led_ctrl.turn_off(rm_define.armor_all)


def vision_recognized_marker_number_three(msg):  # this will be if it's a person
    global marker_found
    global num_marker_three
    global media_custom_audio_1
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 36, 103, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 36, 103, 255, rm_define.effect_flash)
    vision_ctrl.detect_marker_and_aim(rm_define.marker_number_three)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    media_ctrl.play_sound(rm_define.media_custom_audio_1, wait_for_complete_flag=True)
    print("There is a person in the room")
    marker_found = True
    num_marker_three = True
    media_custom_audio_1 = True
    led_ctrl.turn_off(rm_define.armor_all)


def vision_recognized_marker_letter_F(msg):
    global marker_found
    vision_ctrl.detect_marker_and_aim(rm_define.marker_letter_F)
    vision_ctrl.disable_detection(rm_define.vision_detection_marker)
    gun_ctrl.fire_once()
    print("F marker found")
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
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
        gimbal_ctrl.recenter()  # added in extra
        if person_found == True:
            print("break worked for person scan")
            break
        print("break working if no marker picked up under person scan")
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        gimbal_ctrl.recenter()


def scan_for_marker():
    # Turn on detection and scan left and right until you hit a marker. global marker_found
    global marker_found  # Note: this had to be added in to force the validation to true once the marker is found,
    # then as it is evaluated "While True (marker_found) == False" since true is not same as
    # false then it will break out of the while loop.
    gimbal_ctrl.pitch_ctrl(7)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    marker_found = False
    while marker_found == False:
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_left, 90)
        gimbal_ctrl.recenter()
        if marker_found == True:
            print("break worked for general scan")
            break
        print("just after the break in general scan")
        gimbal_ctrl.rotate_with_degree(rm_define.gimbal_right, 90)
        gimbal_ctrl.recenter()


def happy_dance():
    time.sleep(8)
    chassis_ctrl.move_with_distance(-180, 1.46)
    chassis_ctrl.rotate_with_degree(rm_define.anticlockwise, 90)
    gimbal_ctrl.recenter()
    chassis_ctrl.move_with_distance(0, 2.46)
    gimbal_ctrl.recenter()
    print("We got to the finish line, time to happy dance!!")
    chassis_ctrl.set_wheel_speed(-100, -100, -100, -100)
    time.sleep(1)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
    chassis_ctrl.set_wheel_speed(100, 100, 100, 100)
    time.sleep(1)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 36, 103, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 36, 103, 255, rm_define.effect_marquee)
    chassis_ctrl.set_wheel_speed(100, 100, 100, 100)
    time.sleep(1)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 224, 0, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 224, 0, 255, rm_define.effect_marquee)
    media_ctrl.play_sound(rm_define.media_custom_audio_3)
    chassis_ctrl.set_wheel_speed(100, -100, 100, -100)
    time.sleep(3)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 69, 215, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 69, 215, 255, rm_define.effect_marquee)
    media_ctrl.play_sound(rm_define.media_custom_audio_3)
    chassis_ctrl.set_wheel_speed(-100, 100, -100, 100)
    time.sleep(3)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 0, 0, rm_define.effect_marquee)
    chassis_ctrl.set_wheel_speed(50, -200, -200, 50)
    time.sleep(1)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 50, 0, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 255, 50, 0, rm_define.effect_marquee)
    chassis_ctrl.set_wheel_speed(-200, 50, 50, -200)
    time.sleep(1)
    led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 36, 103, 255, rm_define.effect_flash)
    led_ctrl.set_top_led(rm_define.armor_top_all, 36, 103, 255, rm_define.effect_marquee)
    media_ctrl.play_sound(rm_define.media_custom_audio_5)
    print("Done the happy dance, couldn't be happier!!")


def start():
    global num_marker_one
    global num_marker_two
    global num_marker_three
    global media_custom_audio_0
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    # Set the rotation speed of the gimbal and the speed of the robot in transit
    gimbal_ctrl.set_rotate_speed(80)
    chassis_ctrl.set_trans_speed(1.5)
    gimbal_ctrl.recenter()

    media_ctrl.play_sound(rm_define.media_custom_audio_0, wait_for_complete_flag=True)
    time.sleep(3)
    media_custom_audio_0 = True

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

    room_four()
    num_marker_one = False
    num_marker_two = False
    num_marker_three = False