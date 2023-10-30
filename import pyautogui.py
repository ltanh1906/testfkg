import time
import pygetwindow as gw
import pyautogui
import tkinter as tk
import pickle
from PIL import Image, ImageDraw
import json
def crop_image(captured_image_path, save_path, x, y, width, height):
    try:
        # Load ảnh đã chụp
        captured_image = pyautogui.screenshot(captured_image_path)
        
        # Cắt ảnh theo tọa độ và kích thước chỉ định
        cropped_image = captured_image.crop((x, y, x + width, y + height))
        
        # Lưu ảnh đã cắt
        cropped_image.save(save_path)
    except Exception as e:
        print("")

# Kích thước của mỗi ô
def get_pixel_colors(image_path, x, y):
    img = Image.open(image_path)
    pixel_color = img.getpixel((x, y))
    return pixel_color
# Hàm để chèn dấu chấm màu đỏ vào trung tâm của mỗi ô
def mark_cells(image_path):
    cell_width = int(360 / 13)
    cell_height = int(200 / 4)
    my_arrays = []
    for i in range(4):
        if i == 0: mau = 'xanh'
        if i == 1: mau = 'do'
        if i == 2: mau = 'vang'
        if i == 3: mau = 'luc'

        for j in range(13):
            # Tính toán tọa độ trung tâm của mỗi ô
            x = j * cell_width + cell_width // 2
            y = i * cell_height + cell_height // 2

            color_at_xy = get_pixel_colors(image_path, x, y)
            
            if color_at_xy == (52, 32, 2):
                info = {"color": mau, "value": j+1, "isset": "X"}
                my_arrays.append(info)
            else:
                info = {"color": mau, "value": j+1, "isset": "O"}
                my_arrays.append(info)
        
    return my_arrays

def on_capture_click():
    windows = gw.getAllTitles()
    for win in gw.getWindowsWithTitle('FLOWER KNIGHT GIRL ～X指定～ - FANZA GAMES - Opera'):
        if win.title in windows:
            window = win
            break

    if window:
        # Lấy tọa độ và kích thước của cửa sổ
        x, y, width, height = window.left, window.top, window.width, window.height

        # Chụp ảnh của cửa sổ
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

        # Lưu ảnh chụp được
        screenshot.save(save_path)
        captured_image_path = save_path

        # Đường dẫn để lưu ảnh đã cắt
        cropped_image_path = "ten_anh_da_cat.png"

        # Tọa độ và kích thước để cắt ảnh
        x_coord = 1595  # Thay thế giá trị x bạn muốn cắt
        y_coord = 177  # Thay thế giá trị y bạn muốn cắt
        width = 360    # Thay thế giá trị chiều rộng bạn muốn cắt
        height = 200   # Thay thế giá trị chiều cao bạn muốn cắt

        # Gọi hàm cắt ảnh
        crop_image(captured_image_path, cropped_image_path, x_coord, y_coord, width, height)
    
    return 1

def compare_arrays(array1, array2):
    for item1, item2 in zip(array1, array2):
        # So sánh từng thuộc tính của các phần tử
        if item1['isset'] != item2['isset']:
            return item2

    return True

def get_solution(current_value, next_card_color, current_array):
    print(next_card_color)
    if current_value == 1 :
        print("card A")
        return 'up'
    if current_value == 13 :
        print("card K")
        return 'down'
    
    up = 0
    down = 0
    draw = 0
    card_left = 0
    
    for i in current_array:
        if i['color'] == next_card_color and i['isset'] == "O":
            card_left +=1
            if current_value == i['value']: draw += 1
            if current_value > i['value']: down += 1
            if current_value < i['value']: up += 1
    print(f"Current: {current_value}, Up: {up}, Down: {down}, Card Left: {card_left}")
    if card_left - up - draw == 0:
        return 'up'
    if card_left - down - draw == 0:
        return 'down'
    
    return 'draw'

def mark_cells1(image_path):
    on_capture_click()
    image_path = 'ten_anh.png'
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    x = 1370
    y = 632
    draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill="red")

    img.save("marked_image.png")  # Lưu ảnh đã chèn dấu chấm

def reset_game():
    first_array = [{'color': 'xanh', 'value': 1, 'isset': 'O'}, {'color': 'xanh', 'value': 2, 'isset': 'O'}, {'color': 'xanh', 'value': 3, 'isset': 'O'}, {'color': 'xanh', 'value': 4, 'isset': 'O'}, {'color': 'xanh', 'value': 5, 'isset': 'O'}, {'color': 'xanh', 'value': 6, 'isset': 'O'}, {'color': 'xanh', 'value': 7, 'isset': 'O'}, {'color': 'xanh', 'value': 8, 'isset': 'O'}, {'color': 'xanh', 'value': 9, 'isset': 'O'}, {'color': 'xanh', 'value': 10, 'isset': 'O'}, {'color': 'xanh', 'value': 11, 'isset': 'O'}, {'color': 'xanh', 'value': 12, 'isset': 'O'}, {'color': 'xanh', 'value': 13, 'isset': 'O'}, {'color': 'do', 'value': 1, 'isset': 'O'}, {'color': 'do', 'value': 2, 'isset': 'O'}, {'color': 'do', 'value': 3, 'isset': 'O'}, {'color': 'do', 'value': 4, 'isset': 'O'}, {'color': 'do', 'value': 5, 'isset': 'O'}, {'color': 'do', 'value': 6, 'isset': 'O'}, {'color': 'do', 'value': 7, 'isset': 'O'}, {'color': 'do', 'value': 8, 'isset': 'O'}, {'color': 'do', 'value': 9, 'isset': 'O'}, {'color': 'do', 'value': 10, 'isset': 'O'}, {'color': 'do', 'value': 11, 'isset': 'O'}, {'color': 'do', 'value': 12, 'isset': 'O'}, {'color': 'do', 'value': 13, 'isset': 'O'}, {'color': 'vang', 'value': 1, 'isset': 'O'}, {'color': 'vang', 'value': 2, 'isset': 'O'}, {'color': 'vang', 'value': 3, 'isset': 'O'}, {'color': 'vang', 'value': 4, 'isset': 'O'}, {'color': 'vang', 'value': 5, 'isset': 'O'}, {'color': 'vang', 'value': 6, 'isset': 'O'}, {'color': 'vang', 'value': 7, 'isset': 'O'}, {'color': 'vang', 'value': 8, 'isset': 'O'}, {'color': 'vang', 'value': 9, 'isset': 'O'}, {'color': 'vang', 'value': 10, 'isset': 'O'}, {'color': 'vang', 'value': 11, 'isset': 'O'}, {'color': 'vang', 'value': 12, 'isset': 'O'}, {'color': 'vang', 'value': 13, 'isset': 'O'}, {'color': 'luc', 'value': 1, 'isset': 'O'}, {'color': 'luc', 'value': 2, 'isset': 'O'}, {'color': 'luc', 'value': 3, 'isset': 'O'}, {'color': 'luc', 'value': 4, 'isset': 'O'}, {'color': 'luc', 'value': 5, 'isset': 'O'}, {'color': 'luc', 'value': 6, 'isset': 'O'}, {'color': 'luc', 'value': 7, 'isset': 'O'}, {'color': 'luc', 'value': 8, 'isset': 'O'}, {'color': 'luc', 'value': 9, 'isset': 'O'}, {'color': 'luc', 'value': 10, 'isset': 'O'}, {'color': 'luc', 'value': 11, 'isset': 'O'}, {'color': 'luc', 'value': 12, 'isset': 'O'}, {'color': 'luc', 'value': 13, 'isset': 'O'}]
    with open('your_array.json', 'w') as file:
        json.dump(first_array, file)

def mouse_move(updown):
    start_x, start_y = 1570, 564
    # Điểm kết thúc
    if updown == 'up':
        end_x, end_y = 1045, 304
    if updown == 'down':
        end_x, end_y = 983, 831
    # Di chuyển chuột đến điểm bắt đầu
    pyautogui.moveTo(start_x, start_y)
    # Ấn chuột tại điểm bắt đầu
    pyautogui.mouseDown()
    # Di chuyển chuột đến điểm kết thúc
    pyautogui.moveTo(end_x, end_y)
    # Thả chuột
    pyautogui.mouseUp()
    delay = 1
    time.sleep(delay)
    # Ấn chuột tại vị trí chỉ định
    click_next()

def click_next():
    pyautogui.click(1851, 890)
    time.sleep(2)
    pyautogui.click(1851, 890)

def click_first():
    time.sleep(0.3)
    pyautogui.click(1569, 745)
    time.sleep(0.5)
    pyautogui.click(1503, 870)
    time.sleep(1)

# Đường dẫn để lưu ảnh
save_path = "ten_anh.png"
xanh = (1, 193, 254)
vang = (255, 179, 0)
luc = (2, 209, 143)
do = (253, 152, 153)
# Gọi hàm để chọn và chụp ảnh của cửa sổ đã xác định
# mark_cells1('123')
reset_game()
for i in range(51):
    
    capture = on_capture_click()
    if capture == 1:
        next_card = get_pixel_colors('ten_anh.png', 1370, 632)
        if next_card == xanh: next_card = 'xanh'
        elif next_card == vang: next_card = 'vang'
        elif next_card == luc: next_card = 'luc'
        elif next_card == do: next_card = 'do'
        else: exit()
        cropped_image_path = "ten_anh_da_cat.png"
        old_array = []
        current_array = []
        current_array = mark_cells(cropped_image_path)

        with open('your_array.json', 'r') as file: old_array = json.load(file)

        current_card = compare_arrays(old_array, current_array)['value']
        result = get_solution(current_card, next_card, current_array)
        print(f"Choice:{result}")
        if result != 'draw':
            mouse_move(result)
        else:
            click_next()
        
        if i == 0:
            click_first()
        
        with open('your_array.json', 'w') as file: json.dump(current_array, file)
        if i == 50:
            reset_game()
            print('Game clear!!!')
        # time.sleep(1)

