import pyautogui
import keyboard
import gc
import psutil

print('[Info] Press esc any moment to stop')
print('[Info] waiting to found a match...')

def action(param1, param2, param3):
    text_location = pyautogui.locateOnScreen(param1, grayscale=True, confidence=0.8)

    if text_location is not None:
        
        # if(tasklik):
        
        x, y = pyautogui.center(text_location)
        
        pyautogui.moveTo(x, y)
        pyautogui.click()
        
        print(param2)

        if param3 is True:     
            return
 
        pyautogui.sleep(5)

def is_process_running(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            return True
    return False    

def wait_for_text_and_click(interval=0):
    while True:

        if(is_process_running('League of Legends.exe')):
            print('[INFO] Match is running...')
            return

        if keyboard.is_pressed('esc'):
            return
        
        try:
            action("aceitar.png","[Success] Match accepeted", False)

        except pyautogui.ImageNotFoundException:
                    pass

        gc.collect()

        pyautogui.sleep(interval)

if __name__ == "__main__":
    wait_for_text_and_click()
