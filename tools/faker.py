from uuid import uuid4, UUID

from faker import Faker



class Fake:

    def __init__(self, faker=None):
        self.faker = faker or Faker()

    def random_name(self) -> str:
        return str(uuid4())


fake = Fake(faker=Faker())

