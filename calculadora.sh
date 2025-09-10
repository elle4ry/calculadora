#!/bin/bash

#pedindo os numeros ao usuário:

read -p "Digite seu primeiro número: " num1
read -p "Digite seu segundo número: " num2

#fazendo a soma:
soma=$((num1 + num2))

#mostrando o resultado da soma:
echo "A samo dos dois números é: $soma"

