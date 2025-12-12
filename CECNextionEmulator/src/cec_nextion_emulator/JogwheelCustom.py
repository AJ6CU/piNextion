###################--------------TkDial-Jogwheel--------------###################
# URL = https://github.com/Akascape/TkDial/blob/main/tkdial/jogwheel.py
# Part of TKDial

import tkinter.ttk as ttk
import math

from Jogwheel import Jogwheel

class JogwheelCustom(Jogwheel):
    jogwheel_num = 0
    def __init__(self, master=None, **kw):


        self.foregroundColor={"normal":ttk.Style().lookup(master.cget('style'),'foreground'),
                              "disabled":ttk.Style().lookup(master.cget('style'),'background')
                              }
        self.textColor={    "normal":ttk.Style().lookup(master.cget('style'),'foreground'),
                            "disabled":"gray"
                              }
        self.buttonColor={  "normal":'yellow',
                            "disabled":"gray"
                              }

        self.scaleColor={"normal":'blue',
                         "disabled":"gray"
                         }


        self.initialValue = 0           # Provides default value on creation. Avoids requiring a set operation
        self.lastValue = 0              # lastValue saves the current value thru enable/disable operations
        self.angle_boundaries = {}  # Used to identify boundaries for touch zones
        self.last_segment = None



        if "name" in kw:
            kw.pop("name")
        if "value" in kw:
            self.initialValue = kw.pop("value")

        super().__init__(master,
                        bg=ttk.Style().lookup(master.cget('style'),'background'),
                        fg=ttk.Style().lookup(master.cget('style'),'background'),
                        text_font=ttk.Style().lookup(master.cget('style'),'font'),
                        **kw
        )

        x1 = y1 = self.arc_pos
        x2 = y2 = self.radius - self.arc_pos

        self.circle_center_x = x2-x1
        self.circle_center_y = y2-y1

        self.create_touch_boundaries()

        self.lastValue = self.initialValue      #Set the initial value for the jogwheel
        self.set(self.lastValue)
        self.setStateDisabled()


    def setStateDisabled(self):
        self.configure(state="disabled", scroll=False)
        self.lastValue = self.get()
        self.configure( fg=self.foregroundColor["disabled"],
                        scale_color=self.scaleColor["disabled"],
                        button_color=self.buttonColor["disabled"],
                        text_color=self.textColor["disabled"]
                        )

    def setStateNormal(self):
        self.configure(state="normal", scroll=True)
        self.set(self.lastValue)
        self.configure( fg=self.foregroundColor["normal"],
                        scale_color=self.scaleColor["normal"],
                        button_color=self.buttonColor["normal"],
                        text_color=self.textColor["normal"]
                        )

    def create_touch_boundaries(self):
        lines = int( self.absolute)+1
        base_angle_degrees = ((360-abs(self.start_angle + self.end_angle)))/lines

        for i in range (lines):
            theAngle = (base_angle_degrees * i) + self.start_angle
            bound1 = int(theAngle - (base_angle_degrees / 2))
            bound2 = int(theAngle + (base_angle_degrees / 2))
            if bound1 > 360:
                bound1 -= 360
            if bound2 > 360:
                bound2 -= 360

            self.angle_boundaries[i] = [theAngle, bound1, bound2]
        if JogwheelCustom.jogwheel_num == 0:
            print(self.start, self.max)
            print(self.start, self.max, self.angle_boundaries)
            print("lines", lines, "absolute", self.absolute, "start_angle", self.start_angle, "end_angle", self.end_angle)
            print("base_angle_degrees", base_angle_degrees)
            JogwheelCustom.jogwheel_num += 1

    def find_key_by_range(self, data_dict, target_value):
        for key, (center_angle, min_val, max_val) in data_dict.items():
            if min_val > max_val:
                if target_value >= min_val or target_value < max_val:
                    return key
            else:
                if min_val <= target_value < max_val:
                    return key

        return None

    def on_circle_release(self, x, y, circle_center_x, circle_center_y):

        newAngle = math.degrees(math.atan2(circle_center_y - y, x - circle_center_x))
        # print("new angle =", newAngle)
        if newAngle < 0:
            # print("in lower portion")
            # print("real angle = ", abs(newAngle))
            angle = abs(newAngle)
        else:
            # print("in upper portion")
            # print("real angle = ", 360-abs(newAngle))
            angle = 360 - abs(newAngle)

        result_key = self.find_key_by_range(self.angle_boundaries, angle)
        # print("value =", result_key)
        return result_key



    def rotate_needle(self, event):

        """
        Checks if the mouse button was released within the defined circle.
        """
        # Get the coordinates of the mouse release event
        release_x, release_y = event.x, event.y

        circle_center_x = self.radius/2
        circle_center_y = self.radius/2

        # Calculate the distance from the center of the circle to the release point
        distance = math.sqrt((release_x - circle_center_x) ** 2 + (release_y - circle_center_y) ** 2)

        # Check if the distance is less than or equal to the radius
        if distance <= self.radius:
            # print(f"Button released inside the circle at ({release_x}, {release_y})")
            # Call your desired function here
            new_segment = self.on_circle_release(release_x, release_y, circle_center_x, circle_center_y)

            if new_segment is not None:
                if new_segment != self.last_segment:
                    print(f"moved from {self.last_segment} to {new_segment}")
                    self.last_segment = new_segment
                    self.previous_angle = new_segment
                    self.set(new_segment)
        else:
            print(f"Button released outside the circle at ({release_x}, {release_y})")
    #
    #     angle = math.degrees(math.atan2(self.__y - event.y, event.x - self.__x))
    #     if self.previous_angle > angle:
    #         if self.max > self.start and self.start_angle > self.end_angle:
    #             self.set(self.value + self.scroll_steps)
    #         elif self.max < self.start and self.start_angle < self.end_angle:
    #             self.set(self.value + self.scroll_steps)
    #         else:
    #             self.set(self.value - self.scroll_steps)
    #     else:
    #         if self.max > self.start and self.start_angle > self.end_angle:
    #             self.set(self.value - self.scroll_steps)
    #         elif self.max < self.start and self.start_angle < self.end_angle:
    #             self.set(self.value - self.scroll_steps)
    #         else:
    #             self.set(self.value + self.scroll_steps)
    #
    #     self.previous_angle = angle


    def configure(self, **kwargs):
        """
        This function contains some configurable options
        """

        if "text" in kwargs:
             self.itemconfigure(
                tagOrId="text",
                text=kwargs.pop("text"))

        if "start" in kwargs:
            self.start = kwargs.pop("start")

        if "end" in kwargs:
            self.end = kwargs.pop("end")

        if "bg" in kwargs:
            super().configure(bg=kwargs.pop("bg"))

        if "width" in kwargs:
            super().configure(width=kwargs.pop("width"))

        if "height" in kwargs:
            super().configure(height=kwargs.pop("height"))

        if "scale_color" in kwargs:
            self.itemconfigure(tagOrId="min_scale",
                    fill=kwargs['scale_color'])
            self.itemconfigure(
                tagOrId="progress",
                outline=kwargs.pop("scale_color"))

        if "fg" in kwargs:
            self.itemconfigure(
                tagOrId="face",
                fill=kwargs.pop('fg'))

        if "text_color" in kwargs:
            self.itemconfigure(
                tagOrId="text",
                fill=kwargs.pop("text_color"))

        if "button_color" in kwargs:
            self.itemconfigure(
                tagOrId="needle",
                fill=kwargs.pop("button_color"))

        if "border_color" in kwargs:
            self.itemconfigure(
                tagOrId="face",
                outline=kwargs.pop("border_color"))

        if "scroll_steps" in kwargs:
            self.scroll_steps = kwargs.pop("scroll_steps")

        if "scroll" in kwargs:
            if kwargs["scroll"]==False:
                super().unbind('<MouseWheel>')
                super().unbind('<Button-4>')
                super().unbind('<Button-5>')
            else:
                super().bind('<MouseWheel>', self.scroll_command)
                super().bind("<Button-4>", lambda e: self.scroll_command(-1))
                super().bind("<Button-5>", lambda e: self.scroll_command(1))
            kwargs.pop("scroll")

        if "integer" in kwargs:
            self.set(self.value)
            self.integer = kwargs.pop("integer")

        if "state" in kwargs:
            self.state = kwargs.pop("state")
            self.needle_state()
            if self.state == "normal":
                self.set(self.lastValue)
                self.configure(fg=self.foregroundColor["normal"],
                               scale_color=self.scaleColor["normal"],
                               button_color=self.buttonColor["normal"],
                               text_color=self.textColor["normal"]
                               )
            else:
                self.lastValue = self.get()
                self.configure(fg=self.foregroundColor["disabled"],
                               scale_color=self.scaleColor["disabled"],
                               button_color=self.buttonColor["disabled"],
                               text_color=self.textColor["disabled"]
                               )

        if "progress" in kwargs:
                self.progress = kwargs.pop("progress")

        if "command" in kwargs:
            self.command = kwargs.pop("command")

        if len(kwargs)>0:
            raise ValueError("unknown option: " + list(kwargs.keys())[0])
