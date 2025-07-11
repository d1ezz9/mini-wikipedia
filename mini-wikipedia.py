import requests, re
from urllib.parse import quote

def search(q):
    try:
        r = requests.get(f"https://ru.wikipedia.org/w/api.php?action=query&list=search&srsearch={quote(q)}&format=json&srlimit=5", timeout=5).json()
        return [x['title'] for x in r.get('query',{}).get('search',[])] if r else []
    except: return []

def article(title):
    try:
        r = requests.get(f"https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=True&explaintext=True&titles={quote(title)}", timeout=5).json()
        p = next(iter(r.get('query',{}).get('pages',{}).values())),{}
        return None if 'missing' in p else re.sub(r'\n{3,}','\n\n',p.get('extract','')).strip()
    except: return None

def select(a):
    print("\nНайдено:")
    for i,t in enumerate(a,1): print(f"{i}. {t}")
    try: return a[int(input("\n№: "))-1] if len(a)>1 else a[0]
    except: return None

if __name__ == "__main__":
    print("mini-wikipedia (выход - пустой запрос.)")
    while q:=input("\n> ").strip():
        if not (a:=search(q)): print("Не найдено"); continue
        if not (t:=select(a)) or not (c:=article(t)): print("Ошибка"); continue
        print(f"\n{t}\n{'='*50}\n{c}\n")
