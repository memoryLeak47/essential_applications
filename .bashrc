#!/bin/bash
# .bashrc v48

export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games'
for dir in $(find ~/bin -type d)
do
	PATH=$PATH:$dir
done

export tmpdir="/local"
if [ ! -d $tmpdir ]; then
	mkdir "$tmpdir"
fi
