class ClearTitleComponent extends HTMLElement {
    constructor() {
      super();
    }

    clearTitles() {
      const elementsWithMatchingTitle = document.querySelectorAll('[title="title"], [title*="&lt;"], [title*="https://"], [title*="http://"]');
        elementsWithMatchingTitle.forEach(element => {
        element.setAttribute('title', '');
      });
    }
  
    connectedCallback() {
      // Clear titles after a delay 
      const delay1 = 2000;
      const delay2 = 3000;
      this.clearTitles();
      setTimeout(this.clearTitles, delay1);
      setTimeout(this.clearTitles, delay2);
    }
  }
  
  customElements.define('clear-title', ClearTitleComponent);
  