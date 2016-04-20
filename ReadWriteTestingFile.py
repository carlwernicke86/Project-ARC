import pygame
from KeyList import key_list
from KeyList import key_decoder

ControlOptions = open('ControlOptions.txt', 'w')
ControlOptions.write("SPACEBAR"+"\n")
ControlOptions.write("N"+"\n")
ControlOptions.write("M"+"\n")
ControlOptions.write("F")
ControlOptions.close()
ControlOptions = open('ControlOptions.txt', 'r')
CtrlOp_jump = ControlOptions.readline()
CtrlOp_left = ControlOptions.readline()
CtrlOp_right = ControlOptions.readline()
CtrlOp_intr = ControlOptions.readline()
print CtrlOp_jump
print CtrlOp_left
print CtrlOp_right
print CtrlOp_intr
key_jump = [item for item in key_list if item[1]+"\n" == CtrlOp_jump]
key_left = [item for item in key_list if item[1]+"\n" == CtrlOp_left]
key_right = [item for item in key_list if item[1]+"\n" == CtrlOp_right]
key_interact = [item for item in key_list if item[1] == CtrlOp_intr]
key_jump = key_jump[0][0]
key_left = key_left[0][0]
key_right = key_right[0][0]
key_interact = key_interact[0][0]
print key_jump
print key_left
print key_right
print key_interact

"""
tester = "B"
key_list = [(pygame.K_a, "A"), (pygame.K_b, "B"), (pygame.K_c, "C")]
key_str = [item for item in key_list if tester in item][0][0] #Returns string B
#print key_str
key_translate = [("A", 5), ("B", 6), ("C", 7)]
key_decoded = [item for item in key_translate if key_str in item] #Returns int 6
#print key_decoded

KEYS = [pygame.K_BACKSPACE, pygame.K_TAB, pygame.K_RETURN, pygame.K_SPACE, pygame.K_COMMA, pygame.K_MINUS, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_SEMICOLON, pygame.K_EQUALS, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET, pygame.K_BACKSLASH, pygame.K_BACKQUOTE, pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r, pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x, pygame.K_y, pygame.K_z, pygame.K_DELETE, pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9, pygame.K_KP_MULTIPLY, pygame.K_KP_DIVIDE, pygame.K_KP_MINUS, pygame.K_KP_PLUS, pygame.K_KP_ENTER, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_HOME, pygame.K_END, pygame.K_PAGEUP, pygame.K_PAGEDOWN, pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4, pygame.K_F5, pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_F10, pygame.K_F11, pygame.K_F12, pygame.K_F13, pygame.K_F14, pygame.K_F15, pygame.K_CAPSLOCK, pygame.K_SCROLLOCK, pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_RCTRL, pygame.K_LCTRL, pygame.K_RALT, pygame.K_LALT]
#print KEYS
"""