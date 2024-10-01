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
                {
                    "title": "The Future of Robotics",
                    "creator": "Simon Escano",
                    "content": "Robots are becoming integral in various industries, from manufacturing to healthcare.",
                },
            ],
            "tags": ["Robotics", "AI", "Machine Learning"],
        },
    )
