from django.shortcuts import render
from django.templatetags.static import static  # Adicione isso

def home(request):
    return render(request, 'home.html')

def movie_detail(request):
    film_id = request.GET.get('filmId')
    
    # Dicionário de dados do filme, incluindo o caminho da imagem
    filmes = {
        '1': {
            'titulo': 'Interstellar',
            'ano': 2014,
            'genero': 'Ficção Científica',
            'resumo': 'Um grupo de astronautas viaja por um buraco de minhoca em busca de um novo lar para a humanidade.',
            'imagem': static('FepiCineClup/images/EntreEstrelas.jpg')  # Corrigido
        },
        '2': {
            'titulo': 'Jurassic Park',
            'ano': 1993,
            'genero': 'Aventura/Ficção',
            'resumo': 'Um parque com dinossauros clonados enfrenta o caos quando as criaturas escapam de seus recintos.',
            'imagem': static('FepiCineClup/images/JurasQuePark.jpg')  # Corrigido
        },
        '3': {
            'titulo': 'O Paizão',
            'ano': 1999,
            'genero': 'Comédia',
            'resumo': 'Um homem imaturo adota um menino para impressionar sua namorada, mas acaba se apegando a ele.',
            'imagem': static('FepiCineClup/images/Opaizao.jpg')  # Corrigido
        }
    }

    filme = filmes.get(film_id, None)

    if filme:
        return render(request, 'movie_detail.html', {'filme': filme})
    else:
        # Lida com o caso de filme não encontrado
        return render(request, '404.html')
