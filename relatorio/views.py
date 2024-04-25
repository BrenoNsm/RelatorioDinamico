from django.shortcuts import render
from django.db import connection

"""
code para tratar a tabela é exibir ja está no ideal.
"""
def teste(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM results_survey385575")
        columns = [col[0] for col in cursor.description]  # Obter os nomes das colunas
        results = cursor.fetchall()
        
    return render(request, 'relatorio/teste.html', {'columns': columns, 'results': results})

"""
code para tratar a tabela é exibir ja está no ideal.
"""

def exibir_tabelas(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM exibir_tabelas")
        tabelas = cursor.fetchall()
    
    return render(request, 'relatorio/tabelas.html', {'tabelas': tabelas})