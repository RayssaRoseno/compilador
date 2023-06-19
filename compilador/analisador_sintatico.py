from ply import yacc
import lexer  #analisador léxico

# Aqui você precisa ler a gramática do arquivo .txt e armazená-la em uma string
with open('gramatica.txt', 'r') as file:
    grammar = file.read()

# Defina as regras de produção do analisador sintático
def p_programa(p):
    'programa : PROGRAM ID SEMICOLON corpo DOT'
    # Ação semântica do não terminal <programa>

def p_corpo(p):
    'corpo : declara rotina BEGIN sentencas END'
    # Ação semântica do não terminal <corpo>

def p_declara(p):
    '''declara : VAR dvar mais_dc
               | empty'''
    # Ação semântica do não terminal <declara>

def p_mais_dc(p):
    '''mais_dc : SEMICOLON cont_dc'''
    # Ação semântica do não terminal <mais_dc>

def p_cont_dc(p):
    '''cont_dc : dvar mais_dc
               | empty'''
    # Ação semântica do não terminal <cont_dc>

def p_dvar(p):
    'dvar : variaveis COLON tipo_var'
    # Ação semântica do não terminal <dvar>

def p_tipo_var(p):
    '''tipo_var : INTEGER
                | REAL
                | LBRACE INTEGER RBRACE
                | LBRACE REAL RBRACE'''
    # Ação semântica do não terminal <tipo_var>

def p_variaveis(p):
    'variaveis : id mais_var'
    # Ação semântica do não terminal <variaveis>

def p_mais_var(p):
    '''mais_var : COMMA variaveis
                | empty'''
    # Ação semântica do não terminal <mais_var>

def p_rotina(p):
    '''rotina : procedimento
              | funcao
              | empty'''
    # Ação semântica do não terminal <rotina>

def p_procedimento(p):
    'procedimento : PROCEDURE id parametros SEMICOLON corpo SEMICOLON rotina'
    # Ação semântica do não terminal <procedimento>

def p_funcao(p):
    'funcao : FUNCTION id parametros COLON tipo_funcao SEMICOLON corpo SEMICOLON rotina'
    # Ação semântica do não terminal <funcao>

def p_parametros(p):
    '''parametros : LPAREN lista_parametros RPAREN
                  | empty'''
    # Ação semântica do não terminal <parametros>

def p_lista_parametros(p):
    'lista_parametros : lista_id COLON tipo_var cont_lista_par'
    # Ação semântica do não terminal <lista_parametros>

def p_cont_lista_par(p):
    '''cont_lista_par : SEMICOLON lista_parametros
                      | empty'''
    # Ação semântica do não terminal <cont_lista_par>

def p_lista_id(p):
    'lista_id : id cont_lista_id'
    # Ação semântica do não terminal <lista_id>

def p_cont_lista_id(p):
    '''cont_lista_id : COMMA lista_id
                      | empty'''
    # Ação semântica do não terminal <cont_lista_id>

def p_tipo_funcao(p):
    '''tipo_funcao : INTEGER
                   | REAL
                   | LBRACE INTEGER RBRACE
                   | LBRACE REAL RBRACE'''
    # Ação semântica do não terminal <tipo_funcao>

def p_sentencas(p):
    'sentencas : comando mais_sentencas'
    # Ação semântica do não terminal <sentencas>

def p_mais_sentencas(p):
    '''mais_sentencas : SEMICOLON cont_sentencas'''
    # Ação semântica do não terminal <mais_sentencas>

def p_cont_sentencas(p):
    '''cont_sentencas : sentencas
                      | empty'''
    # Ação semântica do não terminal <cont_sentencas>

def p_var_read(p):
    'var_read : id mais_var_read'
    # Ação semântica do não terminal <var_read>

def p_mais_var_read(p):
    '''mais_var_read : COMMA var_read
                     | empty'''
    # Ação semântica do não terminal <mais_var_read>

def p_var_write(p):
    'var_write : id mais_var_write'
    # Ação semântica do não terminal <var_write>

def p_mais_var_write(p):
    '''mais_var_write : COMMA var_write
                      | empty'''
    # Ação semântica do não terminal <mais_var_write>

def p_comando(p):
    '''comando : READ LPAREN var_read RPAREN
               | WRITE LPAREN var_write RPAREN
               | FOR id ASSIGN expressao TO expressao DO BEGIN sentencas END
               | REPEAT sentencas UNTIL LPAREN condicao RPAREN
               | WHILE LPAREN condicao RPAREN DO BEGIN sentencas END
               | IF LPAREN condicao RPAREN THEN BEGIN sentencas END pfalsa
               | id ASSIGN expressao
               | chamada_procedimento'''
    # Ação semântica do não terminal <comando>

def p_start(p):
    'start : programa'
    # Ação semântica do não terminal <start>


def p_chamada_procedimento(p):
    'chamada_procedimento : id argumentos'
    # Ação semântica do não terminal <chamada_procedimento>

def p_argumentos(p):
    '''argumentos : LPAREN lista_arg RPAREN
                  | empty'''
    # Ação semântica do não terminal <argumentos>

def p_lista_arg(p):
    'lista_arg : expressao cont_lista_arg'
    # Ação semântica do não terminal <lista_arg>

def p_cont_lista_arg(p):
    '''cont_lista_arg : COMMA lista_arg
                      | empty'''
    # Ação semântica do não terminal <cont_lista_arg>

def p_condicao(p):
    '''condicao : relacao LPAREN expressao_num COMMA expressao_num RPAREN
                | relacao LPAREN expressao_conjunto COMMA expressao_conjunto RPAREN'''
    # Ação semântica do não terminal <condicao>

def p_pfalsa(p):
    '''pfalsa : ELSE BEGIN sentencas END
              | empty'''
    # Ação semântica do não terminal <pfalsa>

def p_relacao(p):
    '''relacao : EQUAL
               | GREATER
               | LESS
               | GREATEREQUAL
               | LESSEQUAL
               | NOTEQUAL'''
    # Ação semântica do não terminal <relacao>

def p_expressao(p):
    '''expressao : expressao_num
                 | expressao_conjunto'''
    # Ação semântica do não terminal <expressao>

def p_expressao_num(p):
    '''expressao_num : termo
                     | id argumentos'''
    # Ação semântica do não terminal <expressao_num>

def p_operando(p):
    '''operando : id
                | integer_num
                | real_num
                | operador LPAREN operando COMMA operando RPAREN'''
    # Ação semântica do não terminal <operando>

def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | DOUBLESLASH'''
    # Ação semântica do não terminal <operador>

def p_termo(p):
    '''termo : operador LPAREN operando COMMA operando RPAREN
             | id
             | integer_num
             | real_num'''
    # Ação semântica do não terminal <termo>

def p_expressao_conjunto(p):
    '''expressao_conjunto : opConjunto LPAREN conteudo COMMA conteudo RPAREN
                          | POS LPAREN integer_num RPAREN'''
    # Ação semântica do não terminal <expressao_conjunto>

def p_conteudo(p):
    '''conteudo : LBRACE RBRACE
                | LBRACE integer_num integer_num_cont RBRACE
                | LBRACE real_num real_num_cont RBRACE'''
    # Ação semântica do não terminal <conteudo>

def p_integer_num_cont(p):
    '''integer_num_cont : COMMA integer_num integer_num_cont
                        | empty'''
    # Ação semântica do não terminal <integer_num_cont>

def p_real_num_cont(p):
    '''real_num_cont : COMMA real_num real_num_cont
                     | empty'''
    # Ação semântica do não terminal <real_num_cont>

def p_opConjunto(p):
    '''opConjunto : UNION
                  | SUBSETEQ
                  | SUBSET
                  | INTERSECT'''
    # Ação semântica do não terminal <opConjunto>

def p_id(p):
    'id : letra id_cont'
    # Ação semântica do não terminal <id>

def p_id_cont(p):
    '''id_cont : letra id_cont
               | digito id_cont
               | empty'''
    # Ação semântica do não terminal <id_cont>

def p_num(p):
    'num : digit num_cont'
    # Ação semântica do não terminal <num>

def p_num_cont(p):
    '''num_cont : digito num_cont
                | empty'''
    # Ação semântica do não terminal <num_cont>

def p_integer_num(p):
    '''integer_num : PLUS num
                   | MINUS num
                   | num
                   | INTEGER_NUM'''
    # Ação semântica do não terminal <integer_num>

def p_real_num(p):
    '''real_num : PLUS num DOT num
                | MINUS num DOT num
                | PLUS INTEGER_NUM DOT num
                | MINUS INTEGER_NUM DOT num
                | num DOT num
                | INTEGER_NUM DOT num'''
    # Ação semântica do não terminal <real_num>

def p_letra(p):
    '''letra : A
             | B
             | C
             | D
             | E
             | F
             | G
             | H
             | I
             | J
             | K
             | L
             | M
             | N
             | O
             | P
             | Q
             | R
             | S
             | T
             | U
             | V
             | W
             | X
             | Y
             | Z
             | a
             | b
             | c
             | d
             | e
             | f
             | g
             | h
             | i
             | j
             | k
             | l
             | m
             | n
             | o
             | p
             | q
             | r
             | s
             | t
             | u
             | v
             | w
             | x
             | y
             | z'''
    # Ação semântica do não terminal <letra>

def p_digito(p):
    '''digito : ZERO
              | ONE
              | TWO
              | THREE
              | FOUR
              | FIVE
              | SIX
              | SEVEN
              | EIGHT
              | NINE'''
    # Ação semântica do não terminal <digito>

def p_empty(p):
    'empty :'
    pass

# Inicialize o analisador sintático # Construa o parser
precedence = ()

def p_error(p):
    print("Erro de sintaxe: ", p)

parser = yacc.yacc(module=lexer, start='start', errorlog=yacc.NullLogger(), debug=False)

# Teste o parser com uma entrada
input_text = 'program identificador;'
result = parser.parse(input_text)
