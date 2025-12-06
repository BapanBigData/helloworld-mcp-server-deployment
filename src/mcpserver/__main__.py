from mcpserver.server import mcp


def main():
    # start the server
    mcp.run()


if __name__ == "__main__":
    main()

# command to run on windows machine to start the server:
# uv run -- mcp-server --api-key <your-api-key>
