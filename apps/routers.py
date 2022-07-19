
from apps.users.v1 import users

def routes(api, prefix="/api/v1"):
    api.add_resource(users.CallSaving, f'{prefix}/mobile/<user_name>/call')
    api.add_resource(users.BillCalculating, f'{prefix}/mobile/<user_name>/billing')

