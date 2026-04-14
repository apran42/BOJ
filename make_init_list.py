import os
import re

def initialize_checklist():
    problem_id_pattern = re.compile(r'\d+')
    checked_ids = []

    # 현재 폴더들을 순회하며 문제 번호 수집
    for root, dirs, files in os.walk("."):
        if '.git' in root: continue
        
        folder_name = os.path.basename(root)
        match = problem_id_pattern.search(folder_name)
        if match:
            checked_ids.append(match.group())

    # 중복 제거 및 정렬하여 저장
    with open("checked_problems.txt", "w", encoding="utf-8") as f:
        for pid in sorted(list(set(checked_ids)), key=int):
            f.write(f"{pid}\n")
    
    print(f"✅ {len(checked_ids)}개의 문제를 체크리스트에 등록했습니다.")

if __name__ == "__main__":
    initialize_checklist()