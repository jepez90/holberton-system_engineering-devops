# Install nginx server and configure to add a custom header to response

exec  {'configure nginx':
    command  => 'apt-get -y update',
    command  => 'apt-get -y install nginx',
    command  => 'sed -i "s/server_name _;/server_name _;\n  add_header X-Served-By $hostname always;\n/" /etc/nginx/sites-available/default',
    command  => 'sudo service nginx restart',
    provider => 'shell'
}
