# Asset Tracker
# Copyright (C) 2023  Arjun VedBrat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import Flask
from waitress import serve
from configparser import ConfigParser

app: Flask = Flask(__name__)

configuration: ConfigParser = ConfigParser()
configuration.read("config.ini")

port: int = int(configuration["http"]["port"])
listen_addr: str = configuration["http"]["listen_addr"]


@app.route("/")
def index():
    return "Hello world!"


if __name__ == "__main__":
    print(f"Starting server at {listen_addr}:{str(port)}")
    serve(app=app, host=listen_addr, port=port)
