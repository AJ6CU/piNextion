
<img width="788" height="759" alt="main_window_start" src="https://github.com/user-attachments/assets/83fc2f11-8f6f-4db7-b41c-8b3ed0df1443" />



CECNextionEmulator is a Nextion emualtor for the KD8CEC software that runs on the uBITX. Since it is pretends to be a Nextion (at least as far as the CEC software can tell), there is no software changes required. It also works with both the original 1.x KD8CEC software as well as my CEC 2.0 fork that targets Pico and Teensy MCU's.

Installation requires you to reroute the wires that went originally to the Nextion thru a USB to TTL Serial converter such as https://www.amazon.com/dp/B0BJKCSZZW. 


<img width="606" height="384" alt="ttl-usb" src="https://github.com/user-attachments/assets/8517d695-b6ff-461b-b12f-36c737beb3f1" />


Using the original Nextion harness colors:

- Black - Ground
- Red - Power ( I left the jumper off)
- Blue -   TXD (Nextion) to  RX Pin (D8) (Raduino)
- Yellow - RXD (Nextion) to  TX Pin (D9)  (Raduino)

Unless you are real good at crimping jst connectors, I would highly recommend you get a pre-crimpt set like:
https://www.amazon.com/dp/B0CM315RFP

<img width="292" height="320" alt="Screenshot 2025-12-08 153435" src="https://github.com/user-attachments/assets/468b2b5b-952f-436a-9b5f-cbfcc2ab29af" />

I created a harness using a 4 slot male connector for the plug that would have gone into the nextion  and mated it to a 6 slot female connector that plugs into the TTL-USB connector. (seel below). With this connector, i can swap between the TTL-USB and the Nextion by just a quick unplug/plug operation.

<img width="1952" height="672" alt="wiring_harness" src="https://github.com/user-attachments/assets/dd9e0055-9c7c-427f-8c55-186f3b58ccbe" />

###Key Features
1. Touchscreen and Mouse support
2. Use of dials for ATT, IFS and Frequency Tuning
3. Ability to change individual digits of VFO A from main screen
4. Channel Scanning - Any or all the 20 Channels can be put into a set to be scanned
5. Indication that VFO is displaying the TX Frequency (very useful for CW)
6. Local backup/restore of key Radio settings

I have included some screen shots below.

**The first time you run cecNext you will see this. You need to select the communication port**
<img width="323" height="240" alt="startupscreen_selectport" src="https://github.com/user-attachments/assets/aa67e1fe-0284-4622-84ed-2bea8c492a3b" />

**Channel Scanning**
<img width="801" height="735" alt="channel_scanning" src="https://github.com/user-attachments/assets/b5c11af8-c9b9-4590-b461-1ab8ef110302" />

**Backup**
<img width="848" height="705" alt="backup_screen" src="https://github.com/user-attachments/assets/a7cf0624-364e-4ad6-a754-698c55392b32" />

**Per Digit Tuning on Main Screen**
<img width="790" height="763" alt="per_digit_tuning" src="https://github.com/user-attachments/assets/58a208ce-3b8b-4fde-bfc8-cd2def66a53a" />

**CW Settings**
<img width="1021" height="532" alt="cw_settings" src="https://github.com/user-attachments/assets/060df551-c9ac-4ce6-9047-bdc36cf56134" />

**Preferences**
<img width="449" height="481" alt="general_settings" src="https://github.com/user-attachments/assets/b7fadfac-2192-4140-8bc1-b3f556c11a29" />




###Unsupported Features of Original Nextion/CEC Screens
The following are the features from the original Nextion/CEC screens that have not yet (and may never) be supported:
1. Anything dependent on the auxilary processor
2. Band scanning
3. CW decoding
4. Monitoring A0-A7 Analog lines
5. Let me know what else...

I have created an initial Alpha release for those brave folks. You can download it here
https://github.com/AJ6CU/NextionEmulatorforCEC_Firmware/releases/tag/Alpha1

Please feel free to add to the issues list any surprises you might find!

73
Mark
AJ6CU
