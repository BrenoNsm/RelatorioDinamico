from django.shortcuts import render
from django.db import connection

def selecao_tabela(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'django_%' AND name NOT LIKE 'auth_%'")
        tables = [table[0] for table in cursor.fetchall()]
        
        return render(request, 'relatorio/selecao_tabela.html', {'tables': tables})

def visualizacao(request):
    if request.method == 'POST':
        selected_table = request.POST.get('selected_table')  # Corrigido para 'selected_table'
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {selected_table}")
            columns = [col[0] for col in cursor.description]  # Obter os nomes das colunas
            results = cursor.fetchall()
        
        return render(request, 'relatorio/visualizacao.html', {'columns': columns, 'results': results})
    else:
        return selecao_tabela(request)
