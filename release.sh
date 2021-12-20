#!/bin/bash

PS1="$"
basedir=`pwd`

echo "Starting release script"
cd "$basedir"


if [ -n "$1" ]
then
    commit_tag=$1
    if [ -n "$commit_tag" ]
    then
        echo " - release tag   '$commit_tag'"
    fi
else
	echo "  Please specify version tag to mark release commit!"
	echo "Aborting"
	exit 1
fi


echo " # Searching release base reference"
if [ -n "$1" ] && [ -n "$2" ]
then
	branch=$(git show-ref $2 2> /dev/null | head -1)
	if [ -n "$branch" ]
	then
		echo " - found branch  '$branch'"
	fi

    tag=$(git tag -l $2 2> /dev/null | head -n 1)
	if [ -n "$tag" ]
	then
		echo " - found tag     '$tag'"
	fi

	commit=$(git show --format=oneline $2 2> /dev/null | head -1)
	if [ -n "$commit" ]
	then
		echo " - found commit  '$commit'"
	fi
else
	echo "  Please specify branch,tag or commit hash to base on!"
	echo "Aborting"
	exit 1
fi


# Check valid reference
reference=$(echo "${branch:-${tag:-${commit}}}" | tr " " "\n" | head -1)
if [ -z "$reference" ]
then
    echo "  Given branch, tag or commmit hash '$2' does not seem to be valid - reference found '$reference'"
	echo "Aborting"
    exit 1
fi
echo " # Basing release on commit hash '${reference}'"


echo " # Checking repository state..."
# Check if repository is in clean state
# CLEAN   = merge
# UNCLEAN = fail
if [ -z "$(git status --porcelain)" ]
then
    echo " # Merging changes into working directory..."
    git merge --quiet --no-progress --no-ff --no-commit --allow-unrelated-histories -m "Wydano nową wersję $commit_tag" -m "Baza: $reference" $reference 
    if [ "$?" != "0" ]; then
        echo " - something did not merge cleanly"
        echo "   please review above details and finish the merge"
		echo "Aborting"
		exit 1
    fi

    echo " - merge done and release commit prepared"
elif [ -z "$3" ] || [ $3 != "--force" ]
then
	echo " - cannot release new version on unclean repository!"
	echo "Aborting"
	exit 1
fi


# Add all to index and commit
echo " # Commiting release..."
git add -A > /dev/null
git commit --quiet > /dev/nulls
if [ "$?" == "0" ]; then
	echo " - commit done"
else
	echo " - commit failed"
	echo "Aborting"
	exit 1
fi

# Add version tag
git tag $commit_tag > /dev/null
if [ "$?" == "0" ]; then
	echo " - tag created"
else
	echo " - tag adding failed, please add manually"
fi


echo "Succeed!"
exit 0
