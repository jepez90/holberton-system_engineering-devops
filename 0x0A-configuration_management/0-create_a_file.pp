# creates a file named Holberton

$cont = 'I love Puppet'

file{'Holberton':
    path     => '/tmp/Holberton',
    ensure   => 'absent',
    content  => $cont,
    mode     => '0744',
    owner    => 'www-data',
    group    => 'www-data'
}
