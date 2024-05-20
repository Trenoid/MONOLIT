from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Каталог проектов",
        "catalog": [
            {
                "image": "source/images/a-17.jpg",
                "floor": "Одноэтажный",
                "index": "A-17",
                "price": "40 000",
                "description": "Габариты: 23,2 х 11,8 Площадь: 263,68 м²",
            },
            {
                "image": "source/images/a-110.jpg",
                "floor": "Одноэтажный",
                "index": "A-110",
                "price": "40 000",
                "description": "Габариты: 14,8 х 17,3 Площадь: 228.27 м²",
            },
            {
                "image": "source/images/b-22.jpg",
                "floor": "Двухэтажный",
                "index": "B-22",
                "price": "40 000",
                "description": "Площадь: от 250 м²",
            },
            {
                "image": "source/images/b-109.jpg",
                "floor": "Одноэтажный",
                "index": "B-109",
                "price": "40 000",
                "description": "Площадь : 449,22 м² Габариты: 16,7 х 19,5",
            },
            {
                "image": "source/images/c-115.jpg",
                "floor": "Трехэтажный",
                "index": "C-115",
                "price": "40 000",
                "description": "Площадь: от 250 м²",
            },
            {
                "image": "source/images/c-116.jpg",
                "floor": "Трехэтажный",
                "index": "C-116",
                "price": "40 000",
                "description": "Габариты: 18,7 х 15,0 Площадь: 426 м²",
            },
        ],
    }

    return render(request, "projects/catalog.html", context)


def project(request):
    context = {
        "title": "Проект",
    }

    return render(request, "projects/project.html", context)
