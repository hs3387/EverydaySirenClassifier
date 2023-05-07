# EverydaySirenClassifier


##Files

<div align="center">

<samp>

<h1>Everyday Siren Classification: An ESC Implementation</h1>

<h3> Hayagreevan Sriram  (hs3387@columbia.edu) <br> Madeleine Kearns (mk4652@columbia.edu) <br> Madhav Bhat (mb4989@columbia.edu)</h3>
</samp>   

</div>     


## File Structure
<!---------------------------------------------------------------------------------------------------------------->
The structure of the repository is as follows: 


- model.h

- model.tflite

- Data
	- The folder has the three subfolders as follows
		- ambulance
		- firetruck
		- traffic
	- The files in those folder are split into
		- png files that represent the spectrograms of the whole audios
		- wav files with no prefix (orginal dataset files)
		- wav files with a prefix '[16]' signifying its resampled rate 16kHz
		- wav files with a prefix '[38]' signifying its recreted oudness of -38LUFS
		- wav files with a prefix '[chunk]' which are the same samples but with different durations
- Full Model
	- 1st Model
		- simple_audio_adapt.ipynb
		- fullSizeTFModel.zip
	- 2nd Model
		- updated_data_model.ipynb
		- Full Size TF Model.zip
		
- UI Mockups
	- anrdoid auto mockup.jpg
	- carplay_mockup.jpg
	- An important direction for further development of this siren classifier is to utilize it as an aid for hearing-impaired drivers. By leveraging the capabilities of the platforms like the Arduino Nano 33 BLE Sense, we can create a solution that provides visual feedback to represent approaching sirens. This solution can be implemented as a standalone product or as an add-on to existing systems such as the Head-Up Display (HUD) or the navigation and entertainment system of cars. In the standalone product approach visual indicators such as LEDs or symbols on a graphical display can represent different siren types. As a sirened vehicle approaches the driver, the corresponding visual indicator would activate, providing the necessary alert to the hearing-impaired driver. Alternatively, integrating this into the car's HUD or navigation system would involve developing interfaces that communicate with a car and would enhance the overall user experience by providing a seamless and intuitive interface. Moreover, given the proliferation of Smartphones for navigation and the use of highly programmable applications like systems, such as Google Maps, Android Auto, and Apple CarPlay, building an API that works with these popular applications and systems would enable the ESC system to send signals to and trigger visual responses like flashing symbols on the user interface. The onboard communication protocols of the Arduino Nano, like BLE and Zigbee, both widely used in various applications, can be utilized to establish these integrations. To improve cost-effectiveness, building our model as a TFLM model for the ESP32, a board known for its affordability as well as versatility, can support a wider variety of integrations and make the solution more accessible to a larger user base. Additional training on the system can also add features that would allow computing factors like which direction the siren is originating from and even detect if it is approaching or moving away. By focusing on these use case scenarios and exploring integration options, we can maximize the impact of our ESC system and provide valuable support for hearing-impaired drivers, enhancing their safety and driving experience.

- Arduino Code
	- version 1
		- This was the first version we attempted using a modified version of an existing library code. While we managed to get this working as a siren classifier, it failed to differentiate between firetruck and ambulance sounds effectively.
	- version 2
		- This version was created using the Edge Impulse framework and includes a model we trained using siren sounds recorded using the ble sense's microphone. This version is much better at differentiating between the two sirens and runs more efficiently as it uses a much smaller model.
		
## Instructions
	- For running the version 1, you need to install the Arduino_TensorFlowLite library followed by simply compiling and uploading the embedded_ai.ino using the Arduino IDE.
	- For running version 2, import the arduino_library_code.zip as a library in Arduino IDE following which you can compile and upload the embedded_ai_final_2.ino in the same manner as above.
	
