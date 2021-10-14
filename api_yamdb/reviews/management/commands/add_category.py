from reviews.models import Category
from .add_model import GenreCategoryCommand


class Command(GenreCategoryCommand):
    help = 'add csv to Category model'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = Category
