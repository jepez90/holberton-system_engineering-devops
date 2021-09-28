# fix an typo error in an file of config for wordpress

exec  { 'update file':
    command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
    provider => 'shell'
}
