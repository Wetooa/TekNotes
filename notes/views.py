from django.shortcuts import render


def index(request):
    return render(
        request,
        "home.html",
        {
            "notes": [
                {
                    "title": "The Future of Robotics",
                    "creator": "Simon Escano",
                    "content": "Robots are becoming integral in various industries, from manufacturing to healthcare.",
                },
                {
                    "title": "The Future of Robotics",
                    "creator": "Simon Escano",
                    "content": "Robots are becoming integral in various industries, from manufacturing to healthcare.",
                },
                {
                    "title": "The Future of Robotics",
                    "creator": "Simon Escano",
                    "content": "Robots are becoming integral in various industries, from manufacturing to healthcare.",
                },
                {
                    "title": "The Future of Robotics",
                    "creator": "Simon Escano",
                    "content": "Robots are becoming integral in various industries, from manufacturing to healthcare.",
                },
            ],
            "tags": ["Robotics", "AI", "Machine Learning"],
        },
    )


def tek_a_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        creator = request.POST.get("creator")
        content = request.POST.get("content")
        print(title, creator, content)

    return render(request, "tek_a_note.html")
