import assert from "node:assert/strict";
import test from "node:test";

class TestHTMLElement {
  constructor() {
    this.attributes = new Map();
    this.children = [];
    this.parentNode = null;
    this.shadowRoot = null;
  }

  attachShadow() {
    this.shadowRoot = new TestElement("#shadow-root");
    return this.shadowRoot;
  }

  setAttribute(name, value) {
    const oldValue = this.getAttribute(name);
    this.attributes.set(name, String(value));
    this.attributeChangedCallback?.(name, oldValue, String(value));
  }

  getAttribute(name) {
    return this.attributes.get(name) ?? null;
  }

  appendChild(child) {
    this.children.push(child);
    child.parentNode = this;
    child.connectedCallback?.();
    return child;
  }

  append(...children) {
    for (const child of children) {
      this.appendChild(child);
    }
  }

  replaceChildren(...children) {
    this.children = [];
    this.append(...children);
  }

  get isConnected() {
    return this === document.body || Boolean(this.parentNode?.isConnected);
  }

  remove() {
    if (!this.parentNode) return;
    this.parentNode.children = this.parentNode.children.filter((child) => child !== this);
    this.parentNode = null;
  }
}

class TestElement extends TestHTMLElement {
  constructor(tagName) {
    super();
    this.tagName = tagName;
    this.textContent = "";
    this.className = "";
    this.part = "";
    this.type = "";
    this.ariaLabel = "";
    this.listeners = {};
    this.style = { cssText: "" };
  }

  addEventListener(type, listener) {
    this.listeners[type] = listener;
  }

  click() {
    this.listeners.click?.();
  }
}

const registry = new Map();

globalThis.HTMLElement = TestHTMLElement;
globalThis.customElements = {
  define(name, elementClass) {
    registry.set(name, elementClass);
  },
  get(name) {
    return registry.get(name);
  },
};
globalThis.document = {
  body: new TestElement("body"),
  createElement(name) {
    const ElementClass = registry.get(name);
    return ElementClass ? new ElementClass() : new TestElement(name);
  },
};

const { Toast, Notifier, notifier } = await import("./Notifier.js");

function findByPart(element, part) {
  if (element.part === part) return element;
  for (const child of element.children) {
    const match = findByPart(child, part);
    if (match) return match;
  }
  return null;
}

test("exports and registers the toast custom element", () => {
  assert.equal(typeof Toast, "function");
  assert.equal(typeof Notifier, "function");
  assert.equal(customElements.get("app-toast"), Toast);
});

test("notifier creates warning toast with text and default duration", () => {
  const toast = notifier.show_warning("it's warning");

  assert.equal(toast.getAttribute("variant"), "warning");
  assert.equal(toast.getAttribute("duration"), "3000");
  assert.equal(toast.getAttribute("message"), "it's warning");
  assert.equal(document.body.children[0].part, "container");
  assert.equal(document.body.children[0].children.includes(toast), true);
});

test("toast renders text and can be closed", () => {
  const container = document.body.children[0];
  const toast = notifier.show_success("it's success", 0);
  const message = findByPart(toast.shadowRoot, "message");
  const closeButton = findByPart(toast.shadowRoot, "close");

  assert.equal(message.textContent, "it's success");
  assert.equal(closeButton.ariaLabel, "Close notification");

  closeButton.click();

  assert.equal(container.children.includes(toast), false);
});
