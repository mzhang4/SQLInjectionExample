import web
from web import form
import model

urls = (
    '/', 'userInfo'
)

render = web.template.render('templates', base='base')

class userInfo:
    loginForm = form.Form(
        form.Textbox("username", description="Username"),
        form.Password("password", description="Password"),
        form.Textbox("sqlInject", description="SQLInjection or not(1. yes, 0. no)"),
        form.Button("submit", type="submit", description="Submit")
        )

    def GET(self):
        f = self.loginForm()
        return render.index(f)

    def POST(self):
        f = self.loginForm()
        f.validates()

        userInfo = {}
        if int(f["sqlInject"].value) == 1:
            userInfo = model.getUserInfo(f["username"].value, f["password"].value)
        elif int(f["sqlInject"].value) == 0:
            userInfo = model.getUserInfoSec(f["username"].value, f["password"].value)

        if not userInfo:
            return render.error()
        else:
            return render.info(userInfo)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()