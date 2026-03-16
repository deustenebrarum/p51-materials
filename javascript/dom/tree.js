function MyElement(tagName) {
  this.tagName = tagName;
  this.children = [];
}

const myDocument = new MyElement("html");

const head = new MyElement("head");
const title = new MyElement("title");
const meta = new MyElement("meta");
head.children.push(title);
head.children.push(meta);
myDocument.children.push(head);

const body = new MyElement("body");
myDocument.children.push(body);
