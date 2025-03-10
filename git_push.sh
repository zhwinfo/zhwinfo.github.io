git add -u
git commit -m 'update'
git checkout --orphan master
git add .
git commit -m 'update'
git push -f origin master
git checkout backup
git branch -D master
