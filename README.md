# hello-world-mcp-server

This repository provides the `hello-world-mcp-server`, an implementation of a Model Context Protocol (MCP) server using the FastMCP Python framework. This makes it easy to build, run, and extend MCP servers that communicate with clients such as **Caude**, **Cline**, **Cursor**, **VSCode**, and more.

## Features

- **Weather Reporting**: Fetch real-time weather data using a simple API tool.
- **Addition Tool**: Basic sample tool illustrating how to extend your own MCP tools.
- **Extensible & Pythonic**: Built on [FastMCP](https://fastmcp.wiki/en/getting-started/welcome), supporting composability and minimal setup.
- **Ready for MCP Clients**: Compatible with the growing ecosystem of MCP-capable applications.

## Prerequisites

- **Python 3.12+**
- **uv**: [astral.sh/uv](https://docs.astral.sh/uv/) (Recommended, used for fast, dependency-isolated execution)
- An [OpenWeather API key](https://openweathermap.org/api) (free signup)

#### Install `uv`

- Windows:
  ```powershell
  irm https://astral.sh/uv/install.ps1 | iex
  ```
- Mac/Linux:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
  Ensure that `uvx` runs in your shell after install:

```bash
uvx --help
```

## Quick Start: Run from Your MCP Client

Paste the following JSON into your MCP-compatible client (**Cursor**, **Cline**, **Caude**, etc), after putting in your OpenWeather API key:

```json
{
  "mcpServers": {
    "hello-world-mcp-server": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/BapanBigData/helloworld-mcp-server-deployment.git",
        "--",
        "mcp-server"
      ],
      "env": {
        "OPENWEATHER_API_KEY": "your-openweather-api-key"
      }
    }
  }
}
```

**Configure:**

- Replace `your-openweather-api-key` with your own key (required).
- The above runs the latest main branch. Clients communicate via stdio.

## How it Works

- The server leverages **FastMCP** for defining tools via decorators for simple, Pythonic extension.
- The weather tool uses the [OpenWeather API](https://openweathermap.org/api) and requires your key as `OPENWEATHER_API_KEY`.

## Technical Overview

- **Framework:** [FastMCP](https://fastmcp.wiki/en/getting-started/welcome)
- **Language:** Python 3.12+
- **Dependencies:** See `pyproject.toml` (uses `mcp[cli]`, `requests`)
- **Entrypoint:** The CLI command `mcp-server` executes `src/mcpserver/__main__.py` which runs the FastMCP-powered server.
- **Config:** All sensitive values are managed via environment variables.
- **Deployment:** Zero-install for users via `uvx --from git+...` means you never need to manually clone or pip install—`uvx` handles dependencies in temporary sandboxes.

### About FastMCP

FastMCP is a lightweight Python framework for building Model Context Protocol servers and clients. **Key features:**

- Low-boilerplate: Define tools with decorators.
- Flexibility: Compose/modify servers with ease.
- Integration: Supports OpenAPI, FastAPI, and more for rapid tool creation.
- Proxying & Composability: Easily create proxies, multiplexers, and transformations.

See the [FastMCP documentation](https://fastmcp.wiki/en/getting-started/welcome) for advanced features and usage.

### About `uv` and `uvx`

- **uv:** A blazingly fast Python package/project manager written in Rust. Provides robust, reproducible environments and universal lockfiles.
- **uvx:** A command-line utility allowing instant, dependency-isolated execution of Python packages directly from a Git repository, without explicit installs. Ideal for running global tools/MCP servers.

Read more at the [`uv` documentation](https://docs.astral.sh/uv/).

## Environment & Security

- Place your OpenWeather API key in the environment as shown above. Never commit secrets to source control.
- All run environments are sandboxed using `uv`.

## Support

For issues or feature requests, open an issue on [GitHub](https://github.com/BapanBigData/helloworld-mcp-server-deployment).

---
