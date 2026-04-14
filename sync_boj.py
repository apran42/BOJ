import os
import re
import time
import cloudscraper

def sync():
    CHECKLIST_FILE = "checked_problems.txt"
    new_base_url = "https://d2gd6pc034wcta.cloudfront.net/tier/"
    target_pattern = re.compile(r'<img src="https://static\.solved\.ac/tier_small/(\d+)\.svg".*?/>\s*([A-Za-z\s]+)')
    tier_names = ["Unrated", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I", "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I", "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I", "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I", "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I", "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I", "Master"]

    # 1. 기존 리스트 로드
    checked_ids = set()
    if os.path.exists(CHECKLIST_FILE):
        with open(CHECKLIST_FILE, 'r') as f:
            checked_ids = {line.strip() for line in f if line.strip()}

    scraper = cloudscraper.create_scraper()
    newly_checked = []

    # 2. 탐색 및 수정
    for root, dirs, files in os.walk("."):
        if '.git' in root: continue
        folder_name = os.path.basename(root)
        pid_match = re.search(r'\d+', folder_name)
        if not pid_match: continue
        pid = pid_match.group()

        if pid in checked_ids: continue # 이미 한 건 패스

        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                if lines and target_pattern.search(lines[0]):
                    res = scraper.get(f"https://solved.ac/api/v3/problem/show?problemId={pid}")
                    if res.status_code == 200:
                        lvl = res.json()['level']
                        lines[0] = target_pattern.sub(f'<img src="{new_base_url}{lvl}.svg" style="height:20px" /> {tier_names[lvl]}', lines[0])
                        with open(path, 'w', encoding='utf-8') as f:
                            f.writelines(lines)
                        print(f"✨ Fixed: {pid}")
                        newly_checked.append(pid)
                        time.sleep(0.5)

    # 3. 리스트 업데이트
    if newly_checked:
        with open(CHECKLIST_FILE, 'a') as f:
            for pid in newly_checked:
                f.write(f"{pid}\n")