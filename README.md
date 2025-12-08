
<img width="798" height="773" alt="Screenshot 2025-12-03 at 3 19 21 PM" src="https://github.com/user-attachments/assets/13009740-ad1a-4c22-a96c-cb451b5dae75" />


CECNextionEmulator is a Nextion emualtor for the KD8CEC software that runs on the uBITX. Since it is pretends to be a Nextion (at least as far as the CEC software can tell), there is no software changes required. It also works with both the original 1.x KD8CEC software as well as my CEC 2.0 fork that targets Pico and Teensy MCU's.

Installation requires you to reroute the wires that went originally to the Nextion thru a USB to TTL Serial converter such as https://www.amazon.com/dp/B0BJKCSZZW. 

<img width="606" height="384" alt="Screenshot 2025-12-03 at 7 42 41 AM" src="https://github.com/user-attachments/assets/9ac17bbd-9300-4481-8913-949088214d43" />


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


I have created an initial Alpha release for those brave folks. You can download it here
https://github.com/AJ6CU/NextionEmulatorforCEC_Firmware/releases/tag/Alpha1

Please feel free to add to the issues list any surprises you might find!

73
Mark
AJ6CU
