@echo off
python sync_boj.py
git add .
git commit -m "solve: sync new problem tiers"
git push
echo.
echo ✨ 동기화 및 푸시가 완료되었습니다!
pause