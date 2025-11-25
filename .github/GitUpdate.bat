@echo off
echo Using Git to Pull and Re-base with main
git pull --rebase origin main
git status
pause
git add .
git commit -m "Restore files after corruption. Reclaiming resonance."
git push origin main
