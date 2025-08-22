@echo off
for /f "usebackq delims=" %%i in (`git config user.name`) do set GIT_NAME=%%i
echo Committer: %GIT_NAME%
echo Commit message: %1
pause
git add .
git commit -m "%1"
git push