# \Author: Andre Vieira da Silva.
# date 2020-03-20
###################################
# script to commit in the gitlab
# - my thesis - Ph.D. physics
###################################

# Instructions to run this script
# to do commit
# chmod +x commit.sh
# ./commit.sh "write the message here"


# Update the latest version before to push to repo, please!
#make

#echo "make, done!"

echo "${1}"

# git-add - command to add any new or modified files to the index
echo "Add changes in files or directory..."
git add .

# The git commit command will save all staged changes, 
# along with a brief description from the user, 
# in a “commit” to the local repository.
echo "committing..."
git commit -m "${1}"

# The git push command is used to upload local repository 
# content to a remote repository. Pushing is how you transfer 
# commits from your local repository to a remote repo. 
echo "and push to remote repository right now!"
git push origin master


echo "All done!"