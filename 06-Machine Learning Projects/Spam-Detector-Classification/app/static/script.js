const messageEl = document.getElementById("message");
const sortBtn = document.getElementById("sort-btn");
const clearBtn = document.getElementById("clear-btn");
const errorMsg = document.getElementById("error-msg");
const stampEl = document.getElementById("stamp");
const stampText = document.getElementById("stamp-text");
const confidenceRow = document.getElementById("confidence-row");
const confidenceFill = document.getElementById("confidence-fill");
const confidenceValue = document.getElementById("confidence-value");
const logList = document.getElementById("log-list");
const modelNameEl = document.getElementById("model-name");

let logEntries = [];

async function loadHealth() {
  try {
    const res = await fetch("/api/health");
    const data = await res.json();
    modelNameEl.textContent = `model: ${data.model}`;
  } catch (e) {
    modelNameEl.textContent = "model: unavailable";
  }
}

function resetResult() {
  stampEl.hidden = true;
  stampEl.classList.remove("spam", "ham");
  confidenceRow.hidden = true;
  errorMsg.hidden = true;
}

function renderLog() {
  if (logEntries.length === 0) {
    logList.innerHTML = '<li class="log-empty">Nothing sorted yet.</li>';
    return;
  }
  logList.innerHTML = logEntries
    .slice(0, 12)
    .map(
      (entry) => `
      <li class="log-item">
        <span class="snippet">${entry.snippet}</span>
        <span class="verdict ${entry.label}">${entry.label.toUpperCase()}</span>
      </li>`
    )
    .join("");
}

async function sortMail() {
  const text = messageEl.value.trim();
  resetResult();

  if (!text) {
    errorMsg.textContent = "Paste a message first — the slot is empty.";
    errorMsg.hidden = false;
    return;
  }

  sortBtn.disabled = true;
  sortBtn.querySelector(".btn-label").textContent = "Sorting…";

  try {
    const res = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `Request failed (${res.status})`);
    }

    const data = await res.json();

    stampText.textContent = data.label === "spam" ? "SPAM" : "HAM";
    stampEl.classList.add(data.label);
    stampEl.hidden = false;

    const pct = Math.round(data.confidence * 100);
    confidenceFill.style.width = `${pct}%`;
    confidenceValue.textContent = `${pct}%`;
    confidenceRow.hidden = false;

    logEntries.unshift({
      snippet: text.length > 46 ? text.slice(0, 46) + "…" : text,
      label: data.label,
    });
    renderLog();
  } catch (e) {
    errorMsg.textContent = `Could not sort that message: ${e.message}`;
    errorMsg.hidden = false;
  } finally {
    sortBtn.disabled = false;
    sortBtn.querySelector(".btn-label").textContent = "Sort this mail";
  }
}

sortBtn.addEventListener("click", sortMail);
clearBtn.addEventListener("click", () => {
  messageEl.value = "";
  resetResult();
  messageEl.focus();
});
messageEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
    sortMail();
  }
});

loadHealth();
renderLog();
