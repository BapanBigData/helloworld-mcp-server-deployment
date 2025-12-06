import argparse
from mcpserver import config
from mcpserver.server import mcp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", required=True)
    args = parser.parse_args()

    # set the weather API key
    config.API_KEY = args.api_key

    # start the server
    mcp.run()


if __name__ == "__main__":
    main()

# command to run on windows machine to start the server:
# uv run -- mcp-server --api-key <your-api-key>
