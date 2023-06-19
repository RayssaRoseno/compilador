import sys
import ply.lex as lex

# Lista de tokens
tokens = [
    'PALAVRA_RESERVADA',
    'OPERADOR_RELACIONAL',
    'OPERADOR_ARITMETICO',
    'DELIMITADOR',
    'IDENTIFICADOR',
    'NUMERO_INTEIRO',
    'NUMERO_REAL',
    'COMENTARIO',
    'STRING',
    'ASPAS_SIMPLES',
    'ASPAS_DUPLAS',
    'ESPACO_EM_BRANCO',
    'ERRO_LEXICO'
]

# Regras de expressões regulares para os tokens
def t_PALAVRA_RESERVADA(t):
    r'(program|var|begin|end|procedure|function|integer|real|read|write|for|to|do|repeat|until|while|if|then|else|pos)\b'
    return t

def t_OPERADOR_RELACIONAL(t):
    r'>=|<=|<>|>|<|=|\('
    return t

def t_OPERADOR_ARITMETICO(t):
    r'(\+|-|\*|/|//)'
    return t

def t_DELIMITADOR(t):
    r'[,();{}]'
    return t

def t_IDENTIFICADOR(t):
    r'[\w_.]+'
    if t.value.lower() in ['program', 'var', 'begin', 'end', 'procedure', 'function', 'integer', 'real', 'read', 'write', 'for', 'to', 'do', 'repeat', 'until', 'while', 'if', 'then', 'else', 'pos']:
        t.type = 'PALAVRA_RESERVADA'
    return t

def t_NUMERO_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMERO_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_COMENTARIO(t):
    r'(/\*(.|\n)*?\*/|//.*)'
    pass

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_ASPAS_SIMPLES(t):
    r'\''
    return t

def t_ASPAS_DUPLAS(t):
    r'\"'
    return t

def t_ESPACO_EM_BRANCO(t):
    r'\s+'
    pass

def t_ERRO_LEXICO(t):
    r'[^a-zA-Z0-9_\s.]'
    print(f"Erro léxico: {t.value}")
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Criação do analisador léxico
lexer = lex.lex()

# Função para realizar a análise léxica do código fonte
def analyze_lexical(code):
    lexer.input(code)
    tokens = []
    while True:
        token = lexer.token()
        if not token:
            break
        tokens.append(token)
    return tokens

if len(sys.argv) < 2:
    print("Por favor, forneça o nome do arquivo como argumento.")
    sys.exit(1)

# Obtém o nome do arquivo do primeiro argumento
filename = sys.argv[1]

# Lê o código-fonte do arquivo
with open(filename, 'r') as file:
    code = file.read()

# Realiza análise léxica
tokens = analyze_lexical(code)
for token in tokens:
    print(token)
