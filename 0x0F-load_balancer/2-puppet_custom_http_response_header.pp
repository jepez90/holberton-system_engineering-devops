# Install nginx server and configure to add a custom header to response

exec  {'install_nginx':
    command  => 'apt-get -y update; apt-get -y install nginx;sed -i "s/name _;/ _;\n add_header X-Served-By $hostname always;\n/" /etc/nginx/sites-available/default; sudo service nginx restart',
    provider => 'shell'
}
