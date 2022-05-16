<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->






<!-- PROJECT LOGO -->
<br />
<h3 align="center">SIMC PID TUNER</h3>


  

  <p align="center">
    A program to estimate PI parameters form a single positive step-response 
    <br />


  </p>



<!-- About -->
## About

This program was made during work with our final theses at OsloMet. We identified that people tuning the PID parameters in our usecase, didn't want to spend 
time calculating and tuning for optimal parameters, since the system is non critical and would still operate with bad tuning parameters.

The suggested solution to this problem is to let the operator do one step-response and based on that estimate PI parameters. Some tuning might be needed, so the operator can tune
Theta and Max value to find a good fit.

## Compile
We choose to compile the file with pyinstaller
```python 
pyinstaller --noconfirm --onefile --windowed  "main.py"
```


<!-- LICENSE -->
## License

Distributed under the GPL license






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
