const TOAST_TAG = "app-toast";
const DEFAULT_DURATION = 3000;

const variantColors = {
  info: "#2563eb",
  success: "#16a34a",
  warning: "#d97706",
  error: "#dc2626",
};

export class Toast extends HTMLElement {
  static get observedAttributes() {
    return ["message", "variant", "duration"];
  }

  constructor() {
    super();
    this.timerId = null;
    this.attachShadow({ mode: "open" });
  }

  connectedCallback() {
    this.render();
    this.startTimer();
  }

  disconnectedCallback() {
    this.stopTimer();
  }

  attributeChangedCallback() {
    if (!this.shadowRoot) return;
    this.render();
    this.startTimer();
  }

  close() {
    this.remove();
  }

  startTimer() {
    this.stopTimer();

    const duration = Number(this.getAttribute("duration") ?? DEFAULT_DURATION);
    if (duration > 0) {
      this.timerId = setTimeout(() => this.close(), duration);
    }
  }

  stopTimer() {
    if (this.timerId !== null) {
      clearTimeout(this.timerId);
      this.timerId = null;
    }
  }

  render() {
    const message = this.getAttribute("message") ?? "";
    const variant = this.getAttribute("variant") ?? "info";
    const color = variantColors[variant] ?? variantColors.info;

    this.shadowRoot.replaceChildren();

    const style = document.createElement("style");
    style.textContent = `
      :host {
        display: block;
        font: 14px/1.4 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      .toast {
        align-items: start;
        background: #fff;
        border-left: 4px solid ${color};
        border-radius: 10px;
        box-shadow: 0 14px 30px rgba(15, 23, 42, 0.18);
        box-sizing: border-box;
        color: #0f172a;
        display: grid;
        gap: 12px;
        grid-template-columns: minmax(0, 1fr) auto;
        max-width: min(360px, calc(100vw - 32px));
        padding: 14px 12px 14px 16px;
      }

      [part="message"] {
        overflow-wrap: anywhere;
      }

      [part="close"] {
        appearance: none;
        background: transparent;
        border: 0;
        border-radius: 999px;
        color: #64748b;
        cursor: pointer;
        font: inherit;
        line-height: 1;
        padding: 2px 6px;
      }

      [part="close"]:focus-visible {
        outline: 2px solid ${color};
        outline-offset: 2px;
      }
    `;

    const wrapper = document.createElement("div");
    wrapper.className = "toast";
    wrapper.part = "toast";
    wrapper.setAttribute("role", variant === "error" ? "alert" : "status");

    const messageElement = document.createElement("span");
    messageElement.part = "message";
    messageElement.textContent = message;

    const closeButton = document.createElement("button");
    closeButton.part = "close";
    closeButton.type = "button";
    closeButton.ariaLabel = "Close notification";
    closeButton.textContent = "x";
    closeButton.addEventListener("click", () => this.close());

    wrapper.append(messageElement, closeButton);
    this.shadowRoot.append(style, wrapper);
  }
}

export class Notifier {
  constructor() {
    this.container = null;
  }

  show(message, variant = "info", duration = DEFAULT_DURATION) {
    const toast = document.createElement(TOAST_TAG);
    toast.setAttribute("message", message);
    toast.setAttribute("variant", variant);
    toast.setAttribute("duration", String(duration));
    this.getContainer().appendChild(toast);
    return toast;
  }

  show_info(message, duration) {
    return this.show(message, "info", duration);
  }

  show_success(message, duration) {
    return this.show(message, "success", duration);
  }

  show_warning(message, duration) {
    return this.show(message, "warning", duration);
  }

  show_error(message, duration) {
    return this.show(message, "error", duration);
  }

  getContainer() {
    if (this.container?.isConnected) return this.container;

    this.container = document.createElement("div");
    this.container.part = "container";
    this.container.style.cssText = `
      display: grid;
      gap: 12px;
      position: fixed;
      right: 16px;
      top: 16px;
      z-index: 2147483647;
    `;
    document.body.appendChild(this.container);
    return this.container;
  }
}

if (!customElements.get(TOAST_TAG)) {
  customElements.define(TOAST_TAG, Toast);
}

export const notifier = new Notifier();
