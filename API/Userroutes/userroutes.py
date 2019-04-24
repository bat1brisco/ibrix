from flask import Blueprint
from API.Controllers.usercontroller import Usercontroller
mod = Blueprint('userroutes', __name__)

@mod.route('/homepage')
def homepage():
    user_controller = Usercontroller()
    sig = user_controller.show()
    
    return sig