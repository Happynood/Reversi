import colors

screen_width = 1000
screen_height = 800
background_image = 'image/background.png'

frame_rate = 60

row_count = 8
column_count = 8
line_color = colors.BLACK

figure_color = colors.WHITE
figure_enemy_color = colors.BLACK

text_color = colors.YELLOW1

font_name = 'Arial'
font_size = 20

effect_duration = 20

sounds_effects = dict(
    lose='sound/lose.wav',
    motion='sound/motion.mp3',
    start='sound/start.wav',
    win='sound/win.wav',
)

message_duration = 2

paddle_color = colors.RED1
paddle_radius = 10
button_text_color = colors.WHITE,
button_normal_back_color = colors.INDIANRED1
button_hover_back_color = colors.INDIANRED2
button_pressed_back_color = colors.INDIANRED3

menu_offset_x = 20
menu_offset_y = 300
menu_button_w = 80
menu_button_h = 50