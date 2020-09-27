import uuid
from user.models import User

users = []
for i in range(10_000):
    u = User(
        email=str(uuid.uuid4()) + '@gmail.com',
        first_name='first_name',
        last_name='last_name',
    )
    users.append(u)

User.objects.bulk_create(users)


# for i in range(10_000):
#     User.objects.create(
#         email=str(uuid.uuid4()) + '@gmail.com',
#         first_name='first_name',
#         last_name='last_name',
#     )
