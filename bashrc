#!/bin/bash
# .bashrc v48

export PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/git/bin'
for dir in $(find ~/bin -type d)
do
	export PATH=$PATH:$dir
done

export tmpdir="/local"
