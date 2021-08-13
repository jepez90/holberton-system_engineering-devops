# kill the proccess called killmenow

exec  { 'kill Poccess':
    command  => 'pkill killmenow',
    provider => 'shell'

}
