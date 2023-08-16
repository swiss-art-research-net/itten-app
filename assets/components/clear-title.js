class ClearTitleComponent extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
      // Clear titles after a delay of 2 seconds (2000 milliseconds)
      const delay = 2000;
      setTimeout(() => {
        const elementsWithMatchingTitle = document.querySelectorAll('[title="title"], [title*="&lt;"]');
        elementsWithMatchingTitle.forEach(element => {
          element.setAttribute('title', '');
        });
      }, delay);
    }
  }
  
  customElements.define('clear-title', ClearTitleComponent);
  