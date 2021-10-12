from reviews.models import Category
from .add_genre import Command as GenreCommand


class Command(GenreCommand):
    help = 'add csv to Category model'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Category
