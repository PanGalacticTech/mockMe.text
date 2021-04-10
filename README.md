# mockMe.text

 a sCrIpT wRiTtEN tO hElP sPeEd uP tHe pRocEsS oF mOCkInG duMb tRaNsPHObIc cOmMeNtS onLiNE
 
 
 I got fed up of having to alternatly type lower case and upper case letters to mock dumb right wing & transphobic comments online, so I automated it.
 
 Either run mocking_script.py in python or double click mockMe.text.exe, and enter the text you wish to mock into the terminal. 
 
 It will return a mostly alternating string of upper and lower case characters, all words start lowercase and there is a 0.15 chance
 that it will reapeat lower or upper case characters for a more random effect.
 
 If you are not happy with the way this randomisation works, try changing the variable in line:
 
 `bit_flip_chance = 0.15`
 
 Entering `0` will ensure the text always alternates upper and lower cases after starting the word lower case.
 
 Entering higher numbers (floats from 0 to 1) will cause longer strings of the same case letters.
 
 Higher values will bias towards lower case due to it always starting on lower case.
