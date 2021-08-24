# Install nginx server and configure to add a custom header to response

exec  {'install_nginx':
    command  => 'apt-get -y update; apt-get -y install nginx',
    provider => 'shell'
}

exec  {'configure_nginx':
    command  => 'sed -i "s/server_name _;/server_name _;\n add_header X-Served-By $hostname always;\n/" /etc/nginx/sites-available/default',
    provider => 'shell'
}

exec  {'restart_nginx':
    command  => 'sudo service nginx restart',
    provider => 'shell'
}
