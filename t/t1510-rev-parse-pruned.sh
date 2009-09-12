#!/bin/sh
#
# Copyright (c) 2005 Junio C Hamano
#

test_description='test git rev-parse core.prunable

Test support for the core.prunable option which allows certain object
types to be removed from the database without interrupting
operations.'

. ./test-lib.sh
GIT_OBJECT_DIRECTORY=.git/objects

git config core.prunable blob &&
echo foo >foo.txt &&
git add foo.txt &&
git commit -m "Add a file" &&
blob=$( git rev-parse HEAD:foo.txt ) &&
git rev-list --objects HEAD
rm -f $GIT_OBJECT_DIRECTORY/${blob:0:2}/${blob:2:38} &&
git rev-list --objects HEAD
git ls-tree HEAD

test_done
