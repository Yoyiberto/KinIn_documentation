# Inspect HTML Classes

This page will help us inspect the HTML classes that Pygments is generating.

```st
PROGRAM MainProgram
  VAR_INPUT
    Start : BOOL;
    Stop : BOOL;
  END_VAR
  
  VAR_OUTPUT
    Running : BOOL;
    Error : BOOL;
  END_VAR
  
  VAR
    Timer1 : TON;
    Counter : INT := 0;
  END_VAR
  
  // This is a comment
  IF Start AND NOT Stop THEN
    Running := TRUE;
    Counter := Counter + 1;
  ELSIF Stop THEN
    Running := FALSE;
    Error := FALSE;
  END_IF;
  
  (* This is a multi-line comment
     that spans multiple lines *)
  
  // Function call example
  Timer1(IN := Running, PT := T#5S);
  
  // Conditional logic
  CASE Counter OF
    0: 
      // Do nothing
    1..10: 
      // Do something for values 1-10
    ELSE
      Counter := 0;
  END_CASE;
  
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
    
    // Add a legend for the classes
    const legendDiv = document.createElement('div');
    legendDiv.style.marginTop = '20px';
    legendDiv.style.padding = '10px';
    legendDiv.style.border = '1px solid #ccc';
    legendDiv.innerHTML = `
      <h3>CSS Class Legend</h3>
      <ul style="list-style-type: none; padding: 0;">
        <li><span style="display: inline-block; width: 20px; height: 20px; background-color: #569cd6; margin-right: 10px;"></span> .nc - Keywords (PROGRAM, VAR_INPUT, etc.)</li>
        <li><span style="display: inline-block; width: 20px; height: 20px; background-color: #9cdcfe; margin-right: 10px;"></span> .nf - Identifiers (variable names, etc.)</li>
        <li><span style="display: inline-block; width: 20px; height: 20px; background-color: #4ec9b0; margin-right: 10px;"></span> .kt - Types (BOOL, INT, etc.)</li>
        <li><span style="display: inline-block; width: 20px; height: 20px; background-color: #6a9955; margin-right: 10px;"></span> .c, .c1, .cm - Comments</li>
        <li><span style="display: inline-block; width: 20px; height: 20px; background-color: #b5cea8; margin-right: 10px;"></span> .m, .mi, .mf - Numbers</li>
        <li><span style="display: inline-block; width: 20px; height: 20px; background-color: #ce9178; margin-right: 10px;"></span> .s - Strings</li>
        <li><span style="display: inline-block; width: 20px; height: 20px; background-color: #d4d4d4; margin-right: 10px;"></span> .p - Punctuation</li>
        <li><span style="display: inline-block; width: 20px; height: 20px; background-color: #d4d4d4; margin-right: 10px;"></span> .err - Error (used for symbols like :)</li>
      </ul>
    `;
    
    codeBlock.parentNode.parentNode.appendChild(legendDiv);
  }
});
</script> 