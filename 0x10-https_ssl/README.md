<div align=center>

***holberton-system_engineering-devops***
<hr />
 <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/banner_shell.svg" alt="Logo BASH" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.system_engineering-devops.0x10" alt="badget visitors"></a>
</div>

# Project: 0x10. HTTPS SSL

> Excercises about: how to configure HTTPS and SSL.


## Files in this Folder:

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **0-world_wide_web**<br />
Bash script must accept 2 arguments:
    * **domain**:
        * type: string
        * what: domain name to audit
        * mandatory: yes
    * **subdomain**:
        * type: string
        * what: specific subdomain to audit
        * mandatory: no
Output: ***The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]***
When only the parameter **domain** is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
When passing **domain** and **subdomain** parameters, display information for the specified subdomain
Ignore **shellcheck** case **SC2086**
Must use:
    * **awk**
    * at least one Bash function
You do not need to handle edge cases such as:
    * Empty parameters
    * Nonexistent domain names
    * Nonexistent subdomains

* <img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logo_shell.svg" alt="Logo Shell" height="20"> **1-haproxy_ssl_termination**<br />
File to configurate the HAProxy load balancer as SSL
    * HAproxy must be listening on port TCP 443
    * HAproxy must be accepting SSL traffic
    * HAproxy must serve encrypted traffic that will return the / of your web server
    * When querying the root of your domain name, the page returned must contain Holberton School
    * Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
