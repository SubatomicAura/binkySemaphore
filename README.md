# Binky Learns Semaphore

**Description of project**

A 3D printed binky that signs blaseball scores in semaphore. Uses a Raspberry Pi with Python to get Blaseball data and to drive the servos.

Binky.py is the main program while semaphore.py is the dictionary with all the letters/numbers and their related angles

***NOTE***

semaphore.py is based off 360 degrees with 0 degrees being the flag pointing straight down. These angles also have not been 100% tested to be accurate and may need to be altered 


Links of insperation / references / other related things
* https://github.com/jmaliksi/blaseball-mike - Python library to get Blaseball data
* https://www.tinkercad.com/things/j3xwBmS7Pqz - 3D objects
* http://woodsgood.ca/projects/2019/04/03/flagman-the-semaphore-clock/ - Idea to do the gearing since micro servos only go 180
* https://www.101computing.net/semaphore-code-using-python-turtle/ - Rough template on how to get turn a string of characters into semaphore commands
* https://www.youtube.com/watch?v=xHDT4CwjUQE - Python Servo Code
