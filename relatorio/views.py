from django.shortcuts import render, HttpResponse
from django.db import connection
import pandas as pd


def selecao_tabela(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND sql NOT NULL AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'django_%' AND name NOT LIKE 'auth_%'")
        tables = [table[0] for table in cursor.fetchall()]
        
        return render(request, 'relatorio/selecao_tabela.html', {'tables': tables})

def visualizacao(request):
    if request.method == 'POST':
        selected_table = request.POST.get('selected_table')
        file_uploaded = request.FILES.get('file_upload')
        

        if file_uploaded:
            if file_uploaded.name.endswith('.csv'):
                df = pd.read_csv(file_uploaded)
            elif file_uploaded.name.endswith('.xls') or file_uploaded.name.endswith('.xlsx'):
                df = pd.read_excel(file_uploaded)
            else:
                return HttpResponse("Arquivo não suportado.")

            # Verificar se o DataFrame não está vazio antes de renderizar
            if not df.empty:
                return render(request, 'relatorio/visualizacao.html', {'selected_table': selected_table, 'dataframe': df})
            else:
                return HttpResponse("O arquivo está vazio.")

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {selected_table}")
            columns = [col[0] for col in cursor.description]
            results = cursor.fetchall()

        return render(request, 'relatorio/visualizacao.html', {'selected_table': selected_table, 'columns': columns, 'results': results})
    else:
        return selecao_tabela(request)
    
    

