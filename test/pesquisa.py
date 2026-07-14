from ddgs import DDGS

termo = input("digite o que quer pesquisar: ")
with DDGS() as ddgs:
    resultados = ddgs.text(termo,max_results=5)
 
for i, r in enumerate(resultados, start=1):
    print(f"{i}. {r['title']} - {r['href']}")
