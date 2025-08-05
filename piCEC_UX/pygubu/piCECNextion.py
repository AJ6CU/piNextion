import piCEC_UXui as baseui
import mystyles  # Styles definition module


class piCECNextion(baseui.piCECNextionUI):
    def __init__(self, master=None, **kw):
        super().__init__(
            master,
            translator=None,
            on_first_object_cb=mystyles.setup_ttk_styles,
            theRadio=None
        )
        self.theRadio = None

    def attachRadio(self, radio):
        self.theRadio = radio

    def mode_lsb_CB(self):
        print("lsb change cb called")
        self.mode_select_VAR.set("LSB")
        self.theRadio.ccPut(2)

    def mode_usb_CB(self):
        print("usb change cb called")
        self.mode_select_VAR.set("USB")
        self.theRadio.ccPut(3)


    def mode_cwl_CB(self):
        print("cwl change cb called")
        self.mode_select_VAR.set("CWL")
        self.theRadio.ccPut(4)


    def mode_cwu_CB(self):
        print("cwu change cb called")
        self.mode_select_VAR.set("CWU")
        self.theRadio.ccPut(5)

    def band_up_CB(self):
         print("band up")

         tx_mode_switch_USB2pre = b'\x59\x58\x68\x03'
         tx_mode_switch_USB2com = b'\x02\x00\x00\x00'
         tx_mode_switch_USB2post = b'\xff\xff\x73'
         tx_mode_switch_USB2 = tx_mode_switch_USB2pre + tx_mode_switch_USB2com + tx_mode_switch_USB2post
         print('command =', tx_mode_switch_USB2)
         self.theRadio.radioPort.write(tx_mode_switch_USB2)

    #
    #     "TS_CMD_BAND": 3,