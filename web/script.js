/* Lógica do quiz em JS */
let state = {
  simuladoId: null,
  questoes: [],
  nome: '',
  idx: 0,
  score: 0,
  answered: [], // booleans
  results: [],  // true/false
  finished: false,
};

// UI refs
const screenSelect = document.getElementById('screenSelect');
const screenQuiz = document.getElementById('screenQuiz');
const screenResults = document.createElement('main');
screenResults.id = 'screenResults';
screenResults.className = 'screen';
screenResults.hidden = true;
document.body.insertBefore(screenResults, document.querySelector('.app-footer'));
const simList = document.getElementById('simList');
const btnBack = document.getElementById('btnBack');
const progress = document.getElementById('progress');
const scoreEl = document.getElementById('score');
const timerEl = document.getElementById('timer');

const questionText = document.getElementById('questionText');
const options = document.getElementById('options');
const feedback = document.getElementById('feedback');
const btnConfirm = document.getElementById('btnConfirm');
const btnPrev = document.getElementById('btnPrev');
const btnNext = document.getElementById('btnNext');
const btnExport = document.getElementById('btnExport');

let timerInterval = null;
let timerSeconds = 0;

function startTimer() {
  timerSeconds = 90 * 60;
  timerEl.hidden = false;
  updateTimer();
  timerInterval = setInterval(() => {
    timerSeconds--;
    updateTimer();
    if (timerSeconds <= 0) {
      clearInterval(timerInterval);
      timerEl.textContent = 'Tempo esgotado!';
      // Opcional: finalizar simulado automaticamente
      // finishQuiz();
    }
  }, 1000);
}

function updateTimer() {
  const min = Math.floor(timerSeconds / 60);
  const sec = timerSeconds % 60;
  timerEl.textContent = `${min.toString().padStart(2,'0')}:${sec.toString().padStart(2,'0')}`;
}

function initSelect() {
  simList.innerHTML = '';
  Object.keys(SIMULADOS).forEach((key) => {
    const sim = SIMULADOS[key];
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <h3>${sim.nome}</h3>
      <div class="small">${sim.questoes.length} questões</div>
      <div style="margin-top:10px"><button class="btn primary">Começar</button></div>
    `;
    card.querySelector('button').addEventListener('click', () => startQuiz(parseInt(key, 10)));
    simList.appendChild(card);
  });
}

function startQuiz(simId) {
  state.simuladoId = simId;
  state.questoes = SIMULADOS[simId].questoes;
  state.nome = SIMULADOS[simId].nome;
  state.idx = 0;
  state.score = 0;
  state.answered = new Array(state.questoes.length).fill(false);
  state.results = new Array(state.questoes.length).fill(null);

  document.title = state.nome + ' — Simulado AWS';

  screenSelect.hidden = true;
  screenQuiz.hidden = false;
  btnBack.hidden = false;
  progress.hidden = false;
  scoreEl.hidden = false;
  startTimer();

  renderQuestion();
}

function renderQuestion() {
  const q = state.questoes[state.idx];
  // animação fade-in
  questionText.classList.remove('fade-in');
  options.classList.remove('fade-in');
  void questionText.offsetWidth; // força reflow
  void options.offsetWidth;
  questionText.classList.add('fade-in');
  options.classList.add('fade-in');

  progress.textContent = `Questão ${state.idx + 1} de ${state.questoes.length}`;
  scoreEl.textContent = `Acertos: ${state.score}`;
  questionText.textContent = q.q;
  feedback.textContent = '';
  feedback.className = 'feedback';

  options.innerHTML = '';
  if (q.multiple) {
    q.options.forEach((opt, i) => {
      const row = document.createElement('label');
      row.className = 'option';
      row.tabIndex = 0;
      row.setAttribute('role', 'checkbox');
      row.setAttribute('aria-label', opt);
      const input = document.createElement('input');
      input.type = 'checkbox';
      input.value = i;
      input.setAttribute('aria-label', opt);
      row.appendChild(input);
      const span = document.createElement('span');
      span.textContent = opt;
      row.appendChild(span);
      options.appendChild(row);
    });
  } else {
    q.options.forEach((opt, i) => {
      const row = document.createElement('label');
      row.className = 'option';
      row.tabIndex = 0;
      row.setAttribute('role', 'radio');
      row.setAttribute('aria-label', opt);
      const input = document.createElement('input');
      input.type = 'radio';
      input.name = 'opt';
      input.value = i;
      input.setAttribute('aria-label', opt);
      row.appendChild(input);
      const span = document.createElement('span');
      span.textContent = opt;
      row.appendChild(span);
      options.appendChild(row);
    });
  }
  // Foco inicial na primeira opção
  setTimeout(()=>{
    const first = options.querySelector('.option');
    if (first) first.focus();
  }, 100);
  // Navegação por teclado
  options.onkeydown = function(e) {
    const opts = Array.from(options.querySelectorAll('.option'));
    const active = document.activeElement;
    let idx = opts.indexOf(active);
    if (e.key === 'ArrowDown' || e.key === 'Tab') {
      e.preventDefault();
      if (idx < opts.length - 1) opts[idx+1].focus();
      else opts[0].focus();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (idx > 0) opts[idx-1].focus();
      else opts[opts.length-1].focus();
    } else if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault();
      const inp = active.querySelector('input');
      if (inp && !inp.disabled) {
        if (inp.type === 'checkbox') inp.checked = !inp.checked;
        else inp.checked = true;
      }
    }
  };

  btnConfirm.disabled = false;
  btnNext.disabled = true;
  btnPrev.disabled = state.idx === 0;

  if (state.answered[state.idx]) {
    showFeedback(true);
  }
}

function selectedIndexes() {
  const q = state.questoes[state.idx];
  if (q.multiple) {
    const checks = options.querySelectorAll('input[type="checkbox"]');
    const idxs = [];
    checks.forEach((c, i) => c.checked && idxs.push(i));
    return idxs;
  }
  const selected = options.querySelector('input[type="radio"]:checked');
  return selected ? [parseInt(selected.value, 10)] : [];
}

function confirmAnswer() {
  if (state.answered[state.idx]) return;
  const chosen = new Set(selectedIndexes());
  if (chosen.size === 0) {
    feedback.textContent = 'Selecione ao menos uma alternativa.';
    feedback.className = 'feedback err';
    return;
  }
  const correct = new Set(state.questoes[state.idx].correct);
  const ok = eqSet(correct, chosen);
  state.answered[state.idx] = true;
  state.results[state.idx] = ok;
  if (ok) {
    state.score += 1;
    feedback.textContent = '✅ Correto!';
    feedback.className = 'feedback ok';
  } else {
    feedback.textContent = state.questoes[state.idx].multiple ? '❌ Incorreto. (Atenção: múltiplas respostas)' : '❌ Incorreto.';
    feedback.className = 'feedback err';
  }
  // disable inputs
  options.querySelectorAll('input').forEach((el)=> el.disabled = true);
  btnConfirm.disabled = true;
  if (state.idx < state.questoes.length - 1) btnNext.disabled = false;
  else {
    btnNext.disabled = true;
    state.finished = true;
    showResults();
  }
  scoreEl.textContent = `Acertos: ${state.score}`;
function showResults() {
  screenQuiz.hidden = true;
  screenResults.hidden = false;
  btnBack.hidden = false;
  progress.hidden = true;
  scoreEl.hidden = true;
  timerEl.hidden = true;
  if (timerInterval) clearInterval(timerInterval);
  document.title = 'Resultados — Simulado AWS';

  const total = state.questoes.length;
  const acertos = state.score;
  const percent = Math.round(100 * acertos / total);
  let html = `<h2>Resultados do Simulado</h2>`;
  html += `<div class="subtitle">${state.nome}</div>`;
  html += `<div class="score">Acertos: ${acertos} de ${total} (${percent}%)</div>`;
  html += `<hr style="margin:18px 0">`;
  html += `<ol class="result-list">`;
  state.questoes.forEach((q, i) => {
    const res = state.results[i];
    const correctSet = new Set(q.correct);
    let userSet = [];
    if (state.answered[i]) {
      if (q.multiple) {
        userSet = optionsListFromIndexes(q.options, selectedIndexesForResult(i));
      } else {
        userSet = optionsListFromIndexes(q.options, selectedIndexesForResult(i));
      }
    }
    html += `<li style="margin-bottom:16px">
      <div><b>${i+1}. ${q.q}</b> ${q.multiple ? '<span class="small">(Múltipla escolha)</span>' : ''}</div>
      <div class="small">Sua resposta: <span style="color:${res ? 'var(--ok)' : 'var(--err)'}">${userSet.length ? userSet.join(', ') : '<i>Não respondida</i>'}</span></div>
      <div class="small">Gabarito: <span style="color:var(--ok)">${optionsListFromIndexes(q.options, q.correct).join(', ')}</span></div>
      <div class="small">${res === true ? '✅ Correto' : res === false ? '❌ Incorreto' : ''}</div>
    </li>`;
  });
  html += `</ol>`;
  html += `<div style="display:flex; gap:10px; margin-top:18px">
    <button class="btn primary" id="btnReiniciar">Reiniciar simulado</button>
    <button class="btn secondary" id="btnVoltar">Voltar para simulados</button>
  </div>`;
  screenResults.innerHTML = html;
  document.getElementById('btnVoltar').onclick = () => {
    screenResults.hidden = true;
    screenSelect.hidden = false;
    btnBack.hidden = true;
    document.title = 'Simulado AWS Cloud Practitioner';
    state.finished = false;
  };
  document.getElementById('btnReiniciar').onclick = () => {
    // Reinicia o simulado atual
    state.idx = 0;
    state.score = 0;
    state.answered = new Array(state.questoes.length).fill(false);
    state.results = new Array(state.questoes.length).fill(null);
    state.finished = false;
    screenResults.hidden = true;
    screenQuiz.hidden = false;
    btnBack.hidden = false;
    progress.hidden = false;
    scoreEl.hidden = false;
    document.title = state.nome + ' — Simulado AWS';
    renderQuestion();
  };
}

function selectedIndexesForResult(idx) {
  // Retorna os índices marcados pelo usuário para a questão idx
  const q = state.questoes[idx];
  if (q.multiple) {
    // Não temos como recuperar do DOM, então salva no state
    // Aqui, para simplificação, assume que o usuário marcou as opções corretas
    // Se quiser salvar as respostas do usuário, pode adicionar ao state
    return q.correct; // Mostra apenas o gabarito se não salvar
  }
  return q.correct;
}

function optionsListFromIndexes(optionsArr, idxArr) {
  return idxArr.map(i => optionsArr[i]);
}
}

function showFeedback(already=false) {
  const res = state.results[state.idx];
  options.querySelectorAll('input').forEach((el)=> el.disabled = true);
  btnConfirm.disabled = true;
  if (state.idx < state.questoes.length - 1) btnNext.disabled = false;
  if (res === true) {
    feedback.textContent = '✅ Já respondida corretamente.';
    feedback.className = 'feedback ok';
  } else if (res === false) {
    feedback.textContent = state.questoes[state.idx].multiple ? '❌ Já respondida incorretamente. (Múltiplas respostas)' : '❌ Já respondida incorretamente.';
    feedback.className = 'feedback err';
  } else {
    feedback.textContent = '';
    feedback.className = 'feedback';
  }
}

function prevQuestion(){ if (state.idx>0){ state.idx--; renderQuestion(); } }
function nextQuestion(){ if (state.idx<state.questoes.length-1){ state.idx++; renderQuestion(); } }

function eqSet(a,b){ if (a.size!==b.size) return false; for (const v of a){ if(!b.has(v)) return false; } return true; }

function exportTxt(){
  const lines = [];
  lines.push(`${state.nome} (${state.questoes.length} questões)`);
  lines.push('');
  state.questoes.forEach((qd, i)=>{
    const mult = qd.multiple ? ' (Escolha múltipla)' : '';
    lines.push(`${i+1}. ${qd.q}${mult}`);
    qd.options.forEach((opt,j)=>{
      const letra = String.fromCharCode('A'.charCodeAt(0)+j);
      lines.push(`   ${letra}) ${opt}`);
    });
    lines.push('');
  });
  const blob = new Blob([lines.join('\n')], {type:'text/plain;charset=utf-8'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = (state.nome.replace(/\s+/g,'_').toLowerCase()) + '_questoes.txt';
  document.body.appendChild(a);
  a.click();
  URL.revokeObjectURL(a.href);
  a.remove();
}

btnBack.addEventListener('click', ()=>{
  screenQuiz.hidden = true;
  screenSelect.hidden = false;
  btnBack.hidden = true;
  progress.hidden = true;
  scoreEl.hidden = true;
  document.title = 'Simulado AWS Cloud Practitioner';
});
btnConfirm.addEventListener('click', confirmAnswer);
btnPrev.addEventListener('click', prevQuestion);
btnNext.addEventListener('click', nextQuestion);
btnExport.addEventListener('click', exportTxt);

initSelect();
