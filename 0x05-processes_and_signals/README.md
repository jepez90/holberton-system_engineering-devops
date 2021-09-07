<div align=center>

***holberton-system_engineering-devops***
<hr />
 <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/banner_shell.svg" alt="Logo BASH" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.system_engineering-devops.0x05" alt="badget visitors"></a>
</div>

# Project: 0x05. Processes and signals

> Excercises about:
    * What is a PID
    * What is a process
    * How to find a process’ PID
    * How to kill a process
    * What is a signal
    * What are the 2 signals that cannot be ignored


## Files in this Folder:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **0-what-is-my-pid**<br />
Bash script that displays its own PID.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **1-list_your_processes**<br />
Bash script that displays a list of currently running processes.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **2-show_your_bash_pid**<br />
Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process without use ***pgrep***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **3-show_your_bash_pid_made_easy**<br />
Bash script that displays the PID, along with the process name, of processes whose name contain the word ***bash*** without use ***ps***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **4-to_infinity_and_beyond**<br />
Bash script that displays ***To infinity and beyond*** indefinitely.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **5-dont_stop_me_now**<br />
Bash script that stops ***4-to_infinity_and_beyond*** process using ***kill***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **6-stop_me_if_you_can**<br />
Bash script that stops ***4-to_infinity_and_beyond*** process without useing ***kill*** or ***killall***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **7-highlander**<br />
Bash script that displays: 
    * ***To infinity and beyond*** indefinitely 
    * With a ***sleep 2*** in between each iteration
    * ***I am invincible!!!*** when receiving a ***SIGTERM*** signal

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **8-beheaded_process**<br />
Bash script that kills the process ***7-highlander***.

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **100-process_and_pid_file**<br />
Bash script that:
    * Creates the file ***/var/run/holbertonscript.pid*** containing its PID
    * Displays ***To infinity and beyond*** indefinitely
    * Displays ***I hate the kill command*** when receiving a SIGTERM signal
    * Displays ***Y U no love me?!*** when receiving a SIGINT signal
    * Deletes the file ***/var/run/holbertonscript.pid*** and terminates itself when receiving a SIGQUIT or SIGTERM signal


* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **101-manage_my_process, manage_my_process**<br />
Bash script that:
    * Indefinitely writes ***I am alive!*** to the file ***/tmp/my_process***
    * In between every ***I am alive!*** message, the program should pause for 2 seconds
Bash (init) script ***101-manage_my_process*** that manages ***manage_my_process***. with arguments ***start***, ***stop*** and ***restart***

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoC.svg" alt="Logo C" height="20"> **102-zombie.c**<br />
C program that creates 5 zombie processes.

