# Week E Tutorial

This week we're going to play with speech recognition and speech generation and connect that to gestures.

## Setup

We're going to install a package called ros_vosk that's pretty useful for this:

```
cd ~/hri2024/src
sudo apt install python3-tk python3-bs4
git clone git@github.com:alphacep/ros-vosk.git
cd ..
catkin_make
```

Now you want to follow the instructions on the project's README page: https://github.com/alphacep/ros-vosk

Now we're going to go back to our weeke directory to develop our nodes.

## Speech Recognition

Play around a bit with the speech recognition node:

```roslaunch ros_vosk ros_vosk.launch```

*(note: this also loads a speech generator node)*

Listen to each of the topics published by the `speech_recognition` node and how parsing of whole and partial utterances work.

## Speech Generation

Vosk comes with a *very* basic speech generator node. You can publish strings to the `tts/phrase` topic to speak them.

* Write a node to listen for speech and then repeat that speech back
* Write a node that listens for speech commands from a user and responds (use gestures from project[0]):
** When a user says 'Hi' or 'Hello', the robot should wave
** When a user says 'yes' or 'no', the robot should nod or shake its head

* Write a node that listens for a string, then speaks that string using text to speech. If the string includes 'hello' then the user should wave, nod or shake for yes or no as well, when the speech engine gets to that word.