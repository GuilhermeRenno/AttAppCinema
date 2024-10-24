from django.shortcuts import render
from django.templatetags.static import static  

def home(request):
    return render(request, 'home.html')

def movie_detail(request):
    film_id = request.GET.get('filmId')
    
    filmes = {
        '1': {
            'titulo': 'Interestelar',
            'ano': 2014,
            'genero': 'Ficção Científica, Aventura',
            'resumo': 'Em um futuro próximo, a Terra enfrenta a extinção devido a catástrofes ecológicas. Cooper, um ex-piloto da NASA, é recrutado para uma missão intergaláctica que busca um novo lar para a humanidade. Junto com uma equipe de astronautas, ele atravessa um buraco de minhoca em busca de planetas habitáveis. O filme explora temas como o amor, a sobrevivência e a relatividade do tempo, enquanto desafia os limites da física e da compreensão humana.',
            'imagem': static('FepiCineClup/images/EntreEstrelas.jpg')  
        },
        '2': {
            'titulo': 'Jurassic Park',
            'ano': 1993,
            'genero': 'Aventura, Ficção Científica',
            'resumo': '"Jurassic Park" segue a história de um parque temático onde dinossauros clonados são trazidos à vida através da engenharia genética. Quando os sistemas de segurança do parque falham, os dinossauros escapam e ameaçam a vida dos visitantes e da equipe do parque. Com um elenco liderado por Alan Grant e Ellie Sattler, o filme é uma mistura de suspense, ação e reflexão sobre os limites da ciência e a natureza.',
            'imagem': static('FepiCineClup/images/JurasQuePark.jpg')  
        },
        '3': {
            'titulo': 'O Poderoso Chefão',
            'ano': 1972,
            'genero': 'Crime, Drama',
            'resumo': 'O Poderoso Chefão" narra a história da família mafiosa Corleone, liderada por Don Vito Corleone, um dos chefes do crime mais respeitados de Nova York. Quando seu filho Michael, um ex-militar, é forçado a se envolver nos negócios da família após um atentado contra seu pai, ele mergulha em um mundo de crime, violência e poder. O filme explora temas de lealdade, justiça e a luta pelo controle de um império criminoso',
            'imagem': static('FepiCineClup/images/Opaizao.jpg')  
        }
    }

    filme = filmes.get(film_id, None)

    if filme:
        return render(request, 'movie_detail.html', {'filme': filme})
    else:
        return render(request, '404.html')
