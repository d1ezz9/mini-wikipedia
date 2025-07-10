import requests, re
from urllib.parse import quote

def search(q):
    r = requests.get(f"https://ru.wikipedia.org/w/api.php?action=query&list=search&srsearch={quote(q)}&format=json&srlimit=5").json()
    return [x['title'] for x in r.get('query',{}).get('search',[])]

def article(title):
    r = requests.get(f"https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=True&explaintext=True&titles={quote(title)}").json()
    p = next(iter(r.get('query',{}).get('pages',{}).values()))
    return None if 'missing' in p else re.sub(r'\n{3,}','\n\n',p.get('extract','')).strip()

def select(a):
    print("\nНайдено:")
    for i,t in enumerate(a,1): print(f"{i}. {t}")
    try: return a[int(input("\n№: "))-1] if len(a)>1 else a[0]
    except: return None

print("mini-wikipedia (выход - пустой запрос.)")
while q:=input("\n> ").strip():
    if not (a:=search(q)): print("Не найдено"); continue
    if (t:=select(a)) and (c:=article(t)): print(f"\n{t}\n{'='*50}\n{c}\n")
