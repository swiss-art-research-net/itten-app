class ClearTitleComponent extends HTMLElement {
    constructor() {
      super();
    }
    
    connectedCallback() {
      const elementsWithMatchingTitle = document.querySelectorAll('[title="title"]');
      console.log("Hello from ClearTitleComponent")
      
      elementsWithMatchingTitle.forEach(element => {
        element.removeAttribute('title');
      });
    }
  }
  
  customElements.define('clear-title', ClearTitleComponent);
  