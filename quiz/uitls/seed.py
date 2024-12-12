import random
from faker import Faker
from quiz.models import Question

def seed_database():
    """
    Function to seed the database with random quiz questions using Faker.
    This clears the existing questions and adds new ones.
    """
    fake = Faker()

    # Clear existing questions (optional, based on requirements)
    Question.objects.all().delete()

    for _ in range(20):  # Generate 20 random questions
        Question.objects.create(
            text=fake.sentence(nb_words=6),
            option_a=fake.word().capitalize(),
            option_b=fake.word().capitalize(),
            option_c=fake.word().capitalize(),
            option_d=fake.word().capitalize(),
            correct_option=random.choice(['A', 'B', 'C', 'D']),
        )

    print("Database successfully seeded with random questions!")
