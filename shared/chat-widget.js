(function () {
  const STARTER_QUESTIONS = [
    "What's the cost of living in Chiang Mai?",
    "Which neighbourhood should I stay in?",
    "What visa do I need to move here?",
    "Where's the best food in Chiang Mai?",
  ];

  const STYLE = `
  #cma-chat-btn{position:fixed;bottom:20px;right:20px;z-index:9999;width:56px;height:56px;border-radius:50%;
    background:#EAB308;color:#0F172A;border:none;box-shadow:0 4px 14px rgba(0,0,0,.35);cursor:pointer;font-size:24px}
  #cma-chat-btn:hover{background:#F5C430}
  #cma-chat-panel{position:fixed;bottom:88px;right:20px;z-index:9999;width:340px;max-width:90vw;height:460px;
    max-height:70vh;background:#1E293B;border:1px solid #334155;border-radius:12px;box-shadow:0 10px 40px rgba(0,0,0,.4);
    display:none;flex-direction:column;overflow:hidden;font-family:'Plus Jakarta Sans',system-ui,sans-serif}
  #cma-chat-panel.open{display:flex}
  #cma-chat-head{background:#0F172A;color:#fff;padding:12px 14px;font-weight:600;font-size:14px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #334155}
  #cma-chat-reset{background:none;border:none;color:#94A3B8;font-size:11px;cursor:pointer;text-decoration:underline}
  #cma-chat-log{flex:1;overflow-y:auto;padding:12px;font-size:13px;line-height:1.45;color:#F1F5F9}
  .cma-chat-msg{margin-bottom:10px;padding:8px 10px;border-radius:8px;max-width:88%}
  .cma-chat-msg.user{background:#334155;margin-left:auto}
  .cma-chat-msg.bot{background:#0F172A;margin-right:auto}
  .cma-chat-msg a{color:#EAB308}
  #cma-chat-chips{display:flex;flex-wrap:wrap;gap:6px;padding:0 12px 10px}
  .cma-chat-chip{background:rgba(234,179,8,0.1);border:1px solid rgba(234,179,8,0.35);color:#EAB308;border-radius:14px;padding:5px 10px;
    font-size:12px;cursor:pointer;text-align:left}
  .cma-chat-chip:hover{background:rgba(234,179,8,0.2)}
  #cma-chat-form{display:flex;border-top:1px solid #334155}
  #cma-chat-input{flex:1;border:none;padding:10px;font-size:13px;outline:none;background:#1E293B;color:#F1F5F9}
  #cma-chat-input::placeholder{color:#94A3B8}
  #cma-chat-form button{border:none;background:#EAB308;color:#0F172A;font-weight:600;padding:0 14px;cursor:pointer}
  #cma-chat-form button:hover{background:#F5C430}
  @media(max-width:480px){#cma-chat-btn{right:16px;bottom:16px}#cma-chat-panel{right:8px;bottom:80px}}
  `;

  const style = document.createElement("style");
  style.textContent = STYLE;
  document.head.appendChild(style);

  const btn = document.createElement("button");
  btn.id = "cma-chat-btn";
  btn.setAttribute("aria-label", "Open chat");
  btn.textContent = "💬";

  const panel = document.createElement("div");
  panel.id = "cma-chat-panel";
  panel.innerHTML = `
    <div id="cma-chat-head"><span>Ask Chiang Mai Ambassador</span><button id="cma-chat-reset" type="button">Reset</button></div>
    <div id="cma-chat-log"></div>
    <div id="cma-chat-chips"></div>
    <form id="cma-chat-form">
      <input id="cma-chat-input" type="text" placeholder="Ask about Chiang Mai..." autocomplete="off" />
      <button type="submit">Send</button>
    </form>
  `;

  document.body.appendChild(btn);
  document.body.appendChild(panel);

  const log = panel.querySelector("#cma-chat-log");
  const chipsEl = panel.querySelector("#cma-chat-chips");
  const form = panel.querySelector("#cma-chat-form");
  const input = panel.querySelector("#cma-chat-input");
  const resetBtn = panel.querySelector("#cma-chat-reset");

  let history = [];

  function addMessage(text, role) {
    const div = document.createElement("div");
    div.className = "cma-chat-msg " + role;
    div.innerHTML = text;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
    return div;
  }

  function renderChips() {
    chipsEl.innerHTML = "";
    STARTER_QUESTIONS.forEach((q) => {
      const chip = document.createElement("button");
      chip.type = "button";
      chip.className = "cma-chat-chip";
      chip.textContent = q;
      chip.addEventListener("click", () => askQuestion(q));
      chipsEl.appendChild(chip);
    });
  }

  function resetConversation() {
    history = [];
    log.innerHTML = "";
    addMessage("Hi! Ask me anything about Chiang Mai living, visas, food, or neighbourhoods.", "bot");
    renderChips();
  }

  let opened = false;
  btn.addEventListener("click", () => {
    panel.classList.toggle("open");
    if (!opened) {
      resetConversation();
      opened = true;
    }
  });

  resetBtn.addEventListener("click", resetConversation);

  async function askQuestion(question) {
    chipsEl.style.display = "none";
    addMessage(escapeHtml(question), "user");
    const loadingId = "loading-" + Date.now();
    addMessage('<span id="' + loadingId + '">Thinking...</span>', "bot");

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question, history }),
      });
      const data = await res.json();
      const loadingEl = document.getElementById(loadingId);
      const sourcesHtml = (data.sources || [])
        .map((s) => `<a href="${s.url}">${escapeHtml(s.title)}</a>`)
        .join("<br>");
      const answer = data.answer || "Sorry, something went wrong.";
      loadingEl.parentElement.innerHTML =
        escapeHtml(answer) + (sourcesHtml ? "<br><br><small>" + sourcesHtml + "</small>" : "");

      history.push({ role: "user", content: question });
      history.push({ role: "assistant", content: answer });
    } catch (err) {
      const loadingEl = document.getElementById(loadingId);
      loadingEl.parentElement.textContent = "Sorry, the chat is unavailable right now.";
    }
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const question = input.value.trim();
    if (!question) return;
    input.value = "";
    askQuestion(question);
  });

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }
})();
