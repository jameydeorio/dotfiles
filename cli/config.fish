fish_vi_key_bindings

set --export PATH /usr/local/share/python /usr/local/bin /usr/bin /bin /usr/local/sbin /usr/sbin /sbin ~/bin $PATH
set --export GREP_OPTIONS '--color=auto --exclude=*.pyc --exclude=tags --exclude-dir=.git --exclude-dir=.tox'
set --export EDITOR vim

eval (python -m virtualfish)

grep (date "+%m/%d") /usr/share/calendar/calendar.music
grep (date "+%m/%d") /usr/share/calendar/calendar.history
grep (date "+%m/%d") /usr/share/calendar/calendar.computer
grep (date "+%m/%d") /usr/share/calendar/calendar.birthday
echo

