import os
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Create the default avatar image in media/avatars/default.jpg"

    def handle(self, *args, **options):
        from PIL import Image, ImageDraw

        dest = os.path.join(settings.MEDIA_ROOT, "avatars", "default.jpg")
        if os.path.exists(dest):
            self.stdout.write(f"Already exists: {dest}")
            return

        os.makedirs(os.path.dirname(dest), exist_ok=True)

        size = 64
        img = Image.new("RGB", (size, size), color=(229, 231, 235))
        draw = ImageDraw.Draw(img)
        draw.ellipse([4, 4, size - 4, size - 4], fill=(156, 163, 175))
        img.save(dest, "JPEG", quality=90)

        self.stdout.write(self.style.SUCCESS(f"Created {dest}"))
