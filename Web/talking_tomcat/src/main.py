import os
import secrets
from urllib.parse import parse_qs

import asyncio
from quart import render_template, Quart, request, session, send_file

from check_url import check_url

app = Quart(__name__)

app.config.update({
    "SECRET_KEY": secrets.token_hex(32),
})

@app.route("/")
async def index():
    query = parse_qs(request.query_string)
    if b"xss" in query:
        session["xss"] = sanitize(query[b"xss"][0].decode())
    return await render_template("index.html")

def sanitize(input):
    brackets = 0
    result = ''
    for i in range(len(input)):
        current = input[i]
        if (current == '<'):
            brackets+=1
        if (brackets == 0):
            result += current
        if (current == '>'):
            brackets-=1
    return result

@app.route("/source")
async def source():
    return await send_file(__file__)

@app.route("/report", methods=["POST"])
async def report():
    data = (await request.get_data()).decode('utf-8')
    #if "xss=" in data:
    #    asyncio.ensure_future(check_url(data[len("xss="):]))
    #return "OK"
    form = await request.form
    if form["url"]:
        asyncio.ensure_future(check_url(form["url"]))
        print( data + " from " +request.remote_addr)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
