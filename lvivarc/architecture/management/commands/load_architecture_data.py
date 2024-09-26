import os
import json
from django.core.management.base import BaseCommand
from architecture.models import ArchitectureGroup, ArchitectureObject
from django.core.files import File

class Command(BaseCommand):
    help = 'Load architecture data from JSON and images'

    def add_arguments(self, parser):
        # Positional argument: directory where output_data.json and Images folder are located
        parser.add_argument('data_dir', type=str, help="Directory containing output_data.json and Images folder")

    def handle(self, *args, **kwargs):
        data_dir = kwargs['data_dir']
        json_file_path = os.path.join(data_dir, 'output_data.json')
        images_dir = os.path.join(data_dir, 'Images')

        # Check if JSON file exists
        if not os.path.exists(json_file_path):
            self.stdout.write(self.style.ERROR(f"File {json_file_path} does not exist"))
            return

        # Load data from JSON file
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Process each item in the JSON data
        for item in data:
            if item['table'] == 'arcgroup':
                # Process ArchitectureGroup
                group, created = ArchitectureGroup.objects.get_or_create(
                    name=item['name'],
                    defaults={
                        'title': item['title'],
                        'slug': item['slug']
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created group: {group.title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Group already exists: {group.title}"))
            
            elif item['table'] == 'arcobject':
                # Process ArchitectureObject
                group = ArchitectureGroup.objects.get(name=item['group'])

                obj, created = ArchitectureObject.objects.get_or_create(
                    title=item['title'],
                    defaults={
                        'text': item['text'],
                        'address': item['address'],
                        'group': group
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created object: {obj.title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Object already exists: {obj.title}"))

                # Handle image (if present)
                if item['image']:
                    image_path = os.path.join(images_dir, os.path.basename(item['image']))
                    if os.path.exists(image_path):
                        with open(image_path, 'rb') as img_file:
                            obj.image.save(os.path.basename(image_path), File(img_file))
                            obj.save()
                        self.stdout.write(self.style.SUCCESS(f"Added image to {obj.title}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"Image not found for {obj.title}: {image_path}"))

        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
