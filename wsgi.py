from web import app
import config

if __name__ == "__main__":
    app.run(host=config.ifaceAddress, port=config.tcpPort)
