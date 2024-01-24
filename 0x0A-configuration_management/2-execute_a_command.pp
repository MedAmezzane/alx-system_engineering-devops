# Execute a command
exec { 'kill-killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  provider => shell,
}