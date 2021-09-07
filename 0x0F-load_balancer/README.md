<div align=center>

***holberton-system_engineering-devops***
<hr />
 <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/banner_shell.svg" alt="Logo BASH" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.system_engineering-devops.0x0F" alt="badget visitors"></a>
</div>

# Project: 0x0F. Load balancer

> Excercises about: how to use and configure load balancers.


## Files in this Folder:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **0-custom_http_response_header**<br />
Bash script that Configure Nginx so that its HTTP response contains a custom header (on **web-01** and **web-02**)
The name of the custom HTTP header must be **X-Served-By**
The value of the custom HTTP header must be the hostname of the server Nginx is running on

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **1-install_load_balancer**<br />
Bash script that configures a new Ubuntu machine with HAProxy that send traffic to **web-01** and **web-02**
Distribute requests using a roundrobin algorithm
