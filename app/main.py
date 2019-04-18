from bocadillo import App, Templates, static, view
import requests


# Initialize app
app = App(static_dir=None)
templates = Templates(app, directory='../app/static/dist')



# Create index route
@app.route("/")
# Allow post and get methods (only get is allowed by default)
@view(methods=['POST','GET'])
async def homepage(req, res):
    # Call weather api
    darksky = requests.get("https://api.darksky.net/forecast/3752f440b0819d65abc12e7df7e5343b/37.8267,-122.4233")
    weather = darksky.json()
    current_weather = weather["currently"]
    hourly_weather = weather["hourly"]

    res.html = await templates.render("index.html", darksky=hourly_weather)


