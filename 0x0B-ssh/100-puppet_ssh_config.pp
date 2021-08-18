# connect with the server using puppet

exec { "connect":
    command  => 'echo "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config':
    path     => '/bin/'
    provider => 'shell'
}
