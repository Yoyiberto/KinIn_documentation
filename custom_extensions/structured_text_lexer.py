from pygments.lexer import RegexLexer, bygroups, words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation

class StructuredTextLexer(RegexLexer):
    """
    Custom lexer for Structured Text programming language.
    
    This lexer highlights keywords like VAR_INPUT, END_VAR, VAR_OUTPUT, PROGRAM, END_PROGRAM.
    """
    name = 'StructuredText'
    aliases = ['st', 'structured_text']
    filenames = ['*.st']
    mimetypes = ['text/x-structured-text']
    
    # Define the keywords we want to highlight
    keywords = (
        'VAR_INPUT', 'END_VAR', 'VAR_OUTPUT', 'PROGRAM', 'END_PROGRAM',
        'VAR', 'VAR_TEMP', 'VAR_GLOBAL', 'VAR_EXTERNAL', 'VAR_IN_OUT',
        'IF', 'THEN', 'ELSE', 'ELSIF', 'END_IF',
        'CASE', 'OF', 'END_CASE',
        'FOR', 'TO', 'BY', 'DO', 'END_FOR',
        'WHILE', 'END_WHILE',
        'REPEAT', 'UNTIL', 'END_REPEAT',
        'FUNCTION', 'END_FUNCTION',
        'FUNCTION_BLOCK', 'END_FUNCTION_BLOCK',
        'RETURN', 'EXIT',
        'TRUE', 'FALSE'
    )
    
    # Define data types
    types = (
        'BOOL', 'BYTE', 'WORD', 'DWORD', 'LWORD',
        'SINT', 'INT', 'DINT', 'LINT',
        'USINT', 'UINT', 'UDINT', 'ULINT',
        'REAL', 'LREAL', 'TIME', 'DATE', 'TIME_OF_DAY', 'DATE_AND_TIME',
        'STRING', 'WSTRING', 'ARRAY', 'STRUCT', 'END_STRUCT'
    )
    
    # Define the token patterns
    tokens = {
        'root': [
            (r'\s+', Text),  # Whitespace
            (r'\(\*', Comment.Multiline, 'comment'),  # Multi-line comments
            (r'//.*?$', Comment.Single),  # Single line comments
            
            # Keywords with special highlighting
            (words(keywords, suffix=r'\b'), Keyword),
            (words(types, suffix=r'\b'), Keyword.Type),
            
            # Identifiers
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),
            
            # Numbers
            (r'[0-9]+\.[0-9]*([eE][+-]?[0-9]+)?', Number.Float),
            (r'[0-9]+', Number.Integer),
            
            # Strings
            (r"'", String, 'string'),
            
            # Operators
            (r'[+\-*/=<>]', Operator),
            
            # Punctuation
            (r'[;:,.()\[\]{}]', Punctuation),
        ],
        'comment': [
            (r'[^*)]', Comment.Multiline),
            (r'\*\)', Comment.Multiline, '#pop'),
            (r'[*)]', Comment.Multiline),
        ],
        'string': [
            (r"[^']*'", String, '#pop'),
        ],
    }

# Function to register the lexer with Pygments
def register_lexer(config):
    """
    Register the StructuredText lexer with Pygments.
    This function is called by the mkdocs-simple-hooks plugin.
    
    Args:
        config: The MkDocs configuration object
        
    Returns:
        The modified config
    """
    from pygments.lexers._mapping import LEXERS
    
    # Only register if not already registered
    if 'StructuredTextLexer' not in LEXERS:
        LEXERS['StructuredTextLexer'] = (
            'custom_extensions.structured_text_lexer',
            'StructuredText',
            ('StructuredText',),
            ('*.st',),
            ('text/x-structured-text',)
        )
        
        # Also register with pygments.lexers
        from pygments.lexers import _lexer_cache
        if 'StructuredText' not in _lexer_cache:
            from pygments.lexers import LEXERS as LEXERS_CACHE
            LEXERS_CACHE['StructuredText'] = (
                'custom_extensions.structured_text_lexer',
                'StructuredText',
                ('StructuredText',),
                ('*.st',),
                ('text/x-structured-text',)
            )
    
    # Debug log to confirm registration
    print("StructuredText lexer registered successfully!")
    
    return config 