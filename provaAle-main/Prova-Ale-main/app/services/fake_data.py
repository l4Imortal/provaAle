from faker import Faker
from app.models import db, Student
from app import create_app

fake = Faker()
app = create_app()
app.app_context().push()

def generate_students(n=10):
    for _ in range(n):
        student = Student(
            full_name=fake.name(),
            birth_date=fake.date_of_birth(minimum_age=2, maximum_age=6),
            contact_info=fake.email()
        )
        db.session.add(student)
    db.session.commit()
    print(f"{n} alunos adicionados.")

if __name__ == "__main__":
    generate_students(10)
