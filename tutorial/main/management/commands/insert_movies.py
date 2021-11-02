from django.core.management.base import BaseCommand
from faker import Faker

from main.models import Movie, Actor


class Command(BaseCommand):
    help = 'Add new movie(s) to the system'

    # все аргументы парсяться в этом методе
    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)
        parser.add_argument('--year', type=int, default=2012)

    # сама логика команды распологаеться здесь
    def handle(self, *args, **options):

        # для работы с Faker надо его заинициализировать
        faker = Faker()

        # для вывода информации о выполнении команды лучше использовать self.stdout.write('текст') вместо принта
        self.stdout.write('Start inserting Movies')
        for _ in range(options['len']):
            self.stdout.write('Start inserting Movies')

            movie = Movie()

            new_title = ' '.join(faker.text().split()[:3])
            movie.title = new_title
            movie.plot = faker.text()
            movie.year = options['year']
            movie.runtime = 120
            movie.rating = 0
            movie.save()

            for _ in range(10):
                actor = Actor()
                actor.name = faker.name()
                actor.save()
                movie.actors.add(actor)

            self.stdout.write(f'New movie: {movie}')
        self.stdout.write('End inserting Movies')
