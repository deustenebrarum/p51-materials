import { notifier } from "./Notifier/Notifier.js";

document.body.style.fontFamily = "system-ui, sans-serif";
document.body.innerHTML = `
  <main style="display: grid; gap: 12px; max-width: 360px; padding: 32px;">
    <h1 style="margin: 0;">Notifier demo</h1>
    <button id="info">Show info</button>
    <button id="success">Show success</button>
    <button id="warning">Show warning</button>
    <button id="error">Show error</button>
  </main>
`;

document.querySelector("#info").addEventListener("click", () => {
  notifier.show_info("it's info");
});

document.querySelector("#success").addEventListener("click", () => {
  notifier.show_success("it's success");
});

document.querySelector("#warning").addEventListener("click", () => {
  notifier.show_warning("it's warning");
});

document.querySelector("#error").addEventListener("click", () => {
  notifier.show_error("it's error");
});
