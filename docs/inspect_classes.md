# Inspect HTML Classes

This page will help us inspect the HTML classes that Pygments is generating.

```st
PROGRAM MainProgram
  VAR_INPUT
    Start : BOOL;
  END_VAR
END_PROGRAM
```

<script>
document.addEventListener('DOMContentLoaded', function() {
  const codeBlock = document.querySelector('pre code.language-st');
  if (codeBlock) {
    // Log the HTML structure
    console.log('Code block HTML:', codeBlock.innerHTML);
    
    // Create a div to display the HTML structure
    const debugDiv = document.createElement('div');
    debugDiv.style.whiteSpace = 'pre-wrap';
    debugDiv.style.fontFamily = 'monospace';
    debugDiv.style.border = '1px solid #ccc';
    debugDiv.style.padding = '10px';
    debugDiv.style.marginTop = '20px';
    debugDiv.textContent = 'HTML Structure:\n\n' + codeBlock.innerHTML;
    
    // Add it after the code block
    codeBlock.parentNode.parentNode.appendChild(debugDiv);
    
    // Highlight spans with class information
    const spans = codeBlock.querySelectorAll('span');
    spans.forEach(span => {
      if (span.className) {
        console.log(`Span with text "${span.textContent}" has class "${span.className}"`);
        
        // Add a data attribute to show the class
        span.setAttribute('data-class', span.className);
        
        // Add a tooltip
        span.title = `Class: ${span.className}`;
        
        // Add inline style to show a border
        span.style.border = '1px dashed #999';
        span.style.position = 'relative';
      }
    });
  }
});
</script> 