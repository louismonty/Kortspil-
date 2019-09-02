import pygame




def box_one_detection():
    m_x,m_y = pygame.mouse.get_pos()
    box_color=254,254,254
    #box one detection 
    if m_x > 10 and m_x < 260 and m_y > 500 and m_y < 600:
        box_color = 255,192,255
    return(box_color)

def box_one_detection_click():
    m_x,m_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if m_x > 10 and m_x < 260 and m_y > 500 and m_y < 600:
            return(True)
        else:
            return(False)




def box_two_detection():
    m_x,m_y = pygame.mouse.get_pos()
    box_color=254,254,254
    #box two detection 
    if m_x > 280 and m_x < 530 and m_y > 500 and m_y < 600:
        box_color = 255,192,255
    return(box_color)

def box_two_detection_click():
    m_x,m_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if m_x > 280 and m_x < 530 and m_y > 500 and m_y < 600:
            return(True)
        else:
            return(False)

def box_three_detection():
    m_x,m_y = pygame.mouse.get_pos()
    box_color=254,254,254
    #box tree detection 
    if m_x > 550 and m_x < 800 and m_y > 500 and m_y < 600:
        box_color = 255,192,255
    return(box_color)

def box_three_detection_click():
    m_x,m_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if m_x > 550 and m_x < 800 and m_y > 500 and m_y < 600:
            return(True)
        else:
            return(False)

def box_four_detection():
    m_x,m_y = pygame.mouse.get_pos()
    box_color=254,254,254
    #box four detection 
    if m_x > 820 and m_x < 1100 and m_y > 500 and m_y < 600:
        box_color = 255,192,255
    return(box_color)

def box_four_detection_click():
    m_x,m_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        if m_x > 820 and m_x < 1100 and m_y > 500 and m_y < 600:
            return(True)
        else:
            return(False)
    