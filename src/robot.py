import re


import pyautogui
import subprocess
import time

from Display import DialogBox

from data_json import ConfigJSON


class Commands():

    def check_word_in_json(self,text, json_key_path):
        words = set(re.findall(r'\b\w+\b', text.lower()))
        json_section = ConfigJSON.get_value(json_key_path)
        if isinstance(json_section, dict):
            for key in json_section.keys():
                if key in words:                      
                    return json_section[key] 

        return False 
        
    def classify(self,string):
        global val
        words = set(re.findall(r'\b\w+\b', string.lower()))
        if "open" in words: 
            DialogBox.robot_command("\nOpening ")
            try:
                
                val=self.check_word_in_json(string,"robot.open")
                DialogBox.robot_command(val) 
                print(val)
                if val!=False: subprocess.Popen(val)
            except:
                DialogBox.robot_command(f"No such location {val}")
                print("No such location ",val)
        elif "volume" in words: 
            try:
                val=self.check_word_in_json(string,"robot.volume")
                DialogBox.robot_command(f"\nvolume {val}")
                print("getting",val)
                for i in range(5):
                    if val!=False: pyautogui.press(val)
            except:
                print("Error ",val)
        elif "switch" in words:
            try:
                val=self.check_word_in_json(string,"robot.machine")
                DialogBox.robot_command(f"\nPressed {val}")
                keys=val=val.split()
                pyautogui.hotkey(*keys)
            except:
                print("Error ",val)
   
