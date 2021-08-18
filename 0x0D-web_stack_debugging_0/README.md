<div align=center>

***holberton-system_engineering-devops***
<hr />
 <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/banner_shell.svg" alt="Logo BASH" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.system_engineering-devops.0x0A" alt="badget visitors"></a>
</div>

# Project: 0x0A. Configuration management

> Excercises about: How to use Puppet to automate configuration of servers.

## Files in this Folder:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_code_file.svg" alt="Logo Code" height="20"> **0-create_a_file.pp**<br />
Using Puppet, create a file in **/tmp** with the follow requirements:
    * File path is **/tmp/holberton**
    * File permission is **0744**
    * File owner is **www-data**
    * File group is **www-data**
    * File contains **I love Puppet**

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_code_file.svg" alt="Logo Code" height="20"> **1-install_a_package.pp**<br />
Using Puppet, install **puppet-lint**. Version must be **2.1.1**

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_code_file.svg" alt="Logo Code" height="20"> **2-execute_a_command.pp**<br />
Using Puppet, create a manifest that kills a process named **killmenow**.
    Must use the **exec** Puppet resource
    Must use **pkill**

