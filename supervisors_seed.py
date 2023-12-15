from sqlalchemy.orm import sessionmaker
from models import engine, Supervisor
import click

Session = sessionmaker(bind=engine)
session = Session()

@click.command()
@click.option("--count", default=2)
@click.option("--super_id", prompt="ID", type=int)
@click.option("--super_name", prompt="Name")
@click.option("--super_email", prompt="Email")
@click.option("--super_major", prompt="Major")

def supervisor_handler(count, super_id, super_name, super_email, super_major):
    for _ in range(count):
        # click.echo("Sup ID: %d" % id)
        # click.echo("Name: %s" % name)
        # click.echo("Email: %s" % email)
        # click.echo("Major: %s" % major)
        sup = {"ID": super_id, "name": super_name, "email": super_email, "major": super_major}
        print(sup)

        new_supervisor = Supervisor(sup_id = super_id, name = super_name, email = super_email, major = super_major)

        session.add(new_supervisor)
        session.commit()
        

if __name__ == '__main__':
    supervisor_handler()
    pass

supervisor1 = Supervisor(sup_id = 1, name="Khalifa", email="kmuyeeden@gmail.com", major="Software Engineering")
supervisor2 = Supervisor(sup_id = 2, name="Abdul", email="abdul@gmail.com", major="Science")

# session.add_all([supervisor1, supervisor2])
# session.commit()