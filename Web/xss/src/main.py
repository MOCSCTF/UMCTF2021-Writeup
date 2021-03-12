import secrets
from urllib.parse import parse_qs
from quart import render_template, Quart, request, session, send_file
import asyncio
from check_url import check_url

app = Quart(__name__)

app.config.update({
    "SECRET_KEY": secrets.token_hex(32),
})

@app.route("/")
async def index():
    query = parse_qs(request.query_string)
    if b"xss" in query:
        session["xss"] = query[b"xss"][0].decode()
    return await render_template("index.html")


@app.route("/source")
async def source():
    return await send_file(__file__)

@app.route("/report", methods=["POST"])
async def report():
    data = (await request.get_data()).decode('utf-8')
    if "url=" in data:
        asyncio.ensure_future(check_url(data[len("url="):]))
        print( data + " from " +request.remote_addr)
    return "OK "


if __name__ == "__main__":
    app.run(port=5000)
