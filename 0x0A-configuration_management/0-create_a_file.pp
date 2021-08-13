# creates a file named Holberton

$cont = 'I love Puppet'

file{'holberton':
    path     => '/tmp/holberton',
    content  => $cont,
    mode     => '0744',
    owner    => 'www-data',
    group    => 'www-data'
}
