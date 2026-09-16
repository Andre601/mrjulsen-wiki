---
status: unreleased
categories:
  - Create Railways Navigator
---

# Web Features

Create Railways Navigator can expose your rail network over the network so external websites, tools and dashboards can read live train data. All of this is provided by the built-in [REST API](api/index.md).

The web server is turned **off by default**. It only starts when you enable it in the config. Since this is a real network service, see the [Security](#security) note before enabling it.

## Enabling the Web Server

The web server is configured in the `common-config` of the server or singleplayer world. Set `web.enabled` to `true` and restart your world or server.

Once running, it listens on the configured address and port and serves the content under one of these URLs:

```
http://<host>:<port>/crn
http://<host>:<port>/createrailwaysnavigator
```

## Configuration

You can find all options under the `web` keys of the `common-config`. Please read the description of the config file for more information.

## Security

/// warning | The web server is unauthenticated
Anyone who can reach the port can read all data the API exposes. There is **no login or API key** yet.
///

- Leave the web features off unless you actually need it.
- To only allow access from the same machine (for example behind a reverse proxy), set `web.bind_address` to `127.0.0.1`. Use `0.0.0.0` to allow any machine on the internet to access your API.
- The server speaks plain **HTTP** only. For HTTPS, put a reverse proxy (nginx, Caddy, ...) in front of it.
- `web.cors_allowed_origins` only controls which websites a **browser** lets read the responses. It is not an access restriction for other clients.
