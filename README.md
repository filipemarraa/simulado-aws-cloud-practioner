# Simulado AWS Cloud Practitioner

Aplicativo desktop simples (Tkinter) para praticar questões de prova AWS Certified Cloud Practitioner. Inclui seleção de simulados e execução de questionários com correção imediata.

## Requisitos
- Python 3.8+ (Tkinter já vem por padrão no macOS/Windows)
- macOS, Windows ou Linux com ambiente gráfico

## Como executar

Opção 1 — Versão Web (recomendado):
- Abra o arquivo `web/index.html` no navegador (funciona offline)
- macOS: `open web/index.html`
- Windows: duplo clique no arquivo

Opcional (servidor local):
- `cd web`
- `python3 -m http.server 8080`
- Abra http://localhost:8080/

Opção 2 — App Tkinter (legado):
- macOS/Linux:
	- Dê permissão de execução e rode o script
		- `chmod +x run.sh`
		- `./run.sh`

Opção 3 (direto com Python):
- `python3 app.py`

Se você tiver múltiplas versões do Python, garanta que está usando a que possui Tkinter instalado.

## Estrutura
- `app.py` — app Tkinter com banco de questões e UI de simulado
- `web/` — versão web estática (HTML/CSS/JS)
- `run.sh` — script simples para iniciar o app
- `README.md` — este arquivo

## Notas
- Em macOS, suprimimos avisos de depreciação do Tkinter com `TK_SILENCE_DEPRECATION=1` já no código.
- O app exporta um TXT com todas as perguntas (sem gabarito) pelo botão "Exportar TXT".

## Próximos passos sugeridos
- Adicionar `requirements.txt` (opcional, hoje só usa stdlib)
- Persistir progresso/estatísticas por simulado
- Tema claro/escuro e acessibilidade (contraste/foco)
- Empacotar como app (pyinstaller) para distribuição sem Python
