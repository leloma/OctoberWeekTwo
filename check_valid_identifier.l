%{
#include <stdio.h>
%}

%%

[^a-zA-Z_].*             { 
    printf("%s is not a valid identifier\n", yytext);
    yyterminate();
}

[a-zA-Z_][a-zA-Z0-9_]*   { 
    printf("%s is a valid identifier\n", yytext);
}
%%

int main() {
    yylex();
    return 0;
}
