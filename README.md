# Enigma

This code Replicates the Working of Enigma that was used during WW. The mechanics and setting of this model is simmilar to the original machine. The settings for the model
can be changed from "config.json" file. 

- About Setting

-- "rotation_tick_rotor*" defines the no of ticks each rotor will rotate per letter of the string. 
-- Do not change Rotor left and right settings. Initially all the rotors are connected correctly to the counter parts, by changig tne "rotation_ticks" the setting inside the 
-- rotor will get scrambles more and more as the conversion continues.
-- "reflector" should be configured such a way that all the letters are connected exactly to its opposite letter, example if A->B then B->A .

<p align="center">
  <img src="https://raw.githubusercontent.com/RishabhSinha07/Enigma/master/Diagram/First.PNG" width="85%" title="Page Models" alt="Example of pages1">
</p>
