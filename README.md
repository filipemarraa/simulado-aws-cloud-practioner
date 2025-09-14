# Simulado AWS Cloud Practitioner

[🔗 Acesse o simulado online](https://simulado-aws-cloud-practioner.vercel.app/)

Simulado interativo para praticar questões do exame AWS Certified Cloud Practitioner. Disponível em versão web responsiva e acessível, com banco de questões completo, timer, exportação, navegação por teclado e opções de apoio ao desenvolvedor.

## Funcionalidades

- **Web App 100% offline**: basta abrir `web/index.html` no navegador.
- **Banco de questões completo**: simulados organizados, múltipla escolha e correção automática.
- **Timer regressivo**: cronômetro de 90 minutos para simular o tempo real da prova.
- **Resultados detalhados**: feedback imediato, estatísticas e gabarito ao final.
- **Acessibilidade**: navegação por teclado, contraste aprimorado.
- **Responsivo**: funciona bem em celulares, tablets e desktops.
- **Animações suaves**: transições ao trocar de questão.
- **Botões de apoio**: Ko-fi (doação internacional) e Linktree (redes sociais e Pix).
- **Exportação TXT**: baixe todas as perguntas do simulado (sem gabarito).

## Estrutura do Projeto

```
aws-prova/
├── README.md
├── web/
│   ├── index.html         # Página principal do simulado
│   ├── styles.css         # Estilos responsivos e acessíveis
│   ├── script.js          # Lógica do quiz, timer, navegação, resultados
│   ├── simulados.js       # Banco de questões (convertido do app.py)
│   ├── qrcode-pix.png     # (Opcional) QR Code Pix para apoio
```

## Como usar

### Versão Web (recomendado)

1. Abra o arquivo `web/index.html` no navegador (funciona offline).
2. Para rodar localmente com servidor:
   ```sh
   cd web
   python3 -m http.server 8080
   ```
   Acesse: [http://localhost:8080](http://localhost:8080)

### Versão Desktop (legado, Tkinter)

- Requer Python 3.8+ com Tkinter.
- Execute o script `app.py` (não incluso na versão web).
- Ou use o `run.sh` se disponível.

## Recursos de Apoio

- **Doação internacional**: botão Ko-fi flutuante no rodapé.
- **Redes sociais e Pix**: botão Linktree flutuante no canto direito.
- **QR Code Pix**: adicione seu QR Code em `web/qrcode-pix.png` e insira no HTML se desejar.

## Acessibilidade e Usabilidade

- Navegação por teclado (Tab, setas, Enter/Espaço).
- Contraste alto para leitura.
- Layout adaptado para dispositivos móveis.
- Feedback visual e sonoro (se desejar, pode adicionar).

## Personalização

- Edite `simulados.js` para adicionar ou modificar questões.
- Ajuste estilos em `styles.css` para mudar cores, fontes ou espaçamentos.
- Adicione novos métodos de apoio (PicPay, Pix, etc) facilmente.

## Próximos Passos Sugeridos

- Persistir progresso/estatísticas por simulado (localStorage).
- Tema claro/escuro manual.
- Empacotar como PWA (instalável no celular).
- Adicionar testes automatizados.
- Melhorar exportação (PDF, CSV).

## Licença

Uso livre para fins de estudo. Não oficial da AWS.
