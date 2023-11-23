from .models import recipes
from io import BytesIO
import base64
import matplotlib.pyplot as plt


def get_recipename_from_id(val):
    recipename = recipes.objects.get(id=val)
    return recipename


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph


def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')

    fig = plt.figure(figsize=(6, 3))
    
    # Counting the number of ingredients for each recipe
    data['no_ingredients'] = data['ingredients'].apply(lambda x: len(x.split(',')))


    if chart_type == '1':  # Pie Chart
        plt.pie(data['no_ingredients'], labels=data['name'], autopct='%1.1f%%')
        plt.title('Pie Chart of Number of Ingredients')

    elif chart_type == '2':  # Bar Chart
        plt.bar(data['name'], data['no_ingredients'])
        plt.xlabel('Recipe Name')
        plt.ylabel('Number of Ingredients')
        plt.title('Bar Chart of Number of Ingredients')

    elif chart_type == '3':  # Line Chart
        plt.plot(data['name'], data['no_ingredients'], marker='o')
        plt.xlabel('Recipe Name')
        plt.ylabel('Number of Ingredients')
        plt.title('Line Chart of Number of Ingredients')
        
    else:
        print('unknown chart type')

    plt.tight_layout()

    chart = get_graph()
    return chart