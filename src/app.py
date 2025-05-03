from server import createApp
from dotenv import load_dotenv
import os

app = createApp()
load_dotenv()

if __name__ == "__main__":

    host = os.getenv('host')
    port = os.getenv('port')

    app.run(debug=True, host=host, port=port)