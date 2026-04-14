import os
import re
import time
import cloudscraper

def sync():
    CHECKLIST_FILE = "checked_problems.txt"
    new_base_url = "https://d2gd6pc034wcta.cloudfront.net/tier/"
    
    # 수정된 정규표현식: 
    # 1. <img ... /> 태그 전체를 매칭
    # 2. 뒤따라오는 공백 및 티어 이름(한글/영문/공백 포함)을 매칭
    target_pattern = re.compile(r'<img src="https://static\.solved\.ac/tier_small/(\d+)\.svg".*?/>\s*([가-힣A-Za-z\s]+)')
    
    tier_names = [
        "Unrated", "Bronze V", "Bronze IV", "Bronze III", "Bronze II", "Bronze I",
        "Silver V", "Silver IV", "Silver III", "Silver II", "Silver I",
        "Gold V", "Gold IV", "Gold III", "Gold II", "Gold I",
        "Platinum V", "Platinum IV", "Platinum III", "Platinum II", "Platinum I",
        "Diamond V", "Diamond IV", "Diamond III", "Diamond II", "Diamond I",
        "Ruby V", "Ruby IV", "Ruby III", "Ruby II", "Ruby I", "Master"
    ]

    # 1. 기존 리스트 로드 (이미 처리한 문제는 다시 요청하지 않음)
    checked_ids = set()
    if os.path.exists(CHECKLIST_FILE):
        with open(CHECKLIST_FILE, 'r', encoding='utf-8') as f:
            checked_ids = {line.strip() for line in f if line.strip()}

    scraper = cloudscraper.create_scraper()
    newly_checked = []

    # 2. 디렉토리 탐색
    for root, dirs, files in os.walk("."):
        if '.git' in root: 
            continue
            
        folder_name = os.path.basename(root)
        pid_match = re.search(r'\d+', folder_name)
        if not pid_match: 
            continue
            
        pid = pid_match.group()

        # 이미 체크된 문제라면 건너뜀
        if pid in checked_ids: 
            continue

        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    # 파일에 내용이 있고, 첫 줄에 패턴이 매칭되는지 확인
                    if lines and target_pattern.search(lines[0]):
                        # solved.ac API 호출
                        res = scraper.get(f"https://solved.ac/api/v3/problem/show?problemId={pid}")
                        
                        if res.status_code == 200:
                            data = res.json()
                            lvl = data['level']
                            
                            # 새로운 이미지 태그와 티어 이름 생성
                            # style="height:20px"를 유지하도록 구성
                            replacement = f'<img src="{new_base_url}{lvl}.svg" style="height:20px" /> {tier_names[lvl]}'
                            
                            # 기존 패턴 부분을 새로운 텍스트로 교체
                            lines[0] = target_pattern.sub(replacement, lines[0])
                            
                            # 파일 저장
                            with open(path, 'w', encoding='utf-8') as f:
                                f.writelines(lines)
                                
                            print(f"✨ 성공적으로 수정됨: {pid} ({tier_names[lvl]})")
                            newly_checked.append(pid)
                            
                            # API 부하 방지를 위한 짧은 대기
                            time.sleep(0.5)
                        else:
                            print(f"⚠️ API 호출 실패 (ID: {pid}): 상태 코드 {res.status_code}")
                    
                except Exception as e:
                    print(f"❌ 파일 처리 중 오류 발생 ({path}): {e}")

    # 3. 처리 완료된 리스트 업데이트
    if newly_checked:
        with open(CHECKLIST_FILE, 'a', encoding='utf-8') as f:
            for pid in newly_checked:
                f.write(f"{pid}\n")
        print(f"\n✅ 총 {len(newly_checked)}개의 문제가 동기화되었습니다.")
    else:
        print("\n✅ 새로 업데이트할 문제가 없습니다.")

if __name__ == "__main__":
    sync()