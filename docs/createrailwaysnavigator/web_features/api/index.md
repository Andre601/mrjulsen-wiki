---
title: API
status: unreleased
categories:
  - Create Railways navigator
---

# REST API

The REST API lets external websites and tools read data from your rail network via HTTP, like trains, stations, journeys, boards, [[Global Settings]] and more. It has to be enabled first (see [Web Features](../index.md) for setup and configuration).

/// note | Authentication
The API is currently **unauthenticated** which means that every enabled endpoint is public. Do not expose it to untrusted networks. See [Security](../index.md#security) for more information.
///

## Response Compression

If gzip is enabled and the client sends `Accept-Encoding: gzip`, larger responses are returned compressed.

## Common parameters

Every response accepts a set of query parameters to trim and order the output. They can be combined freely and can always be used in addition to the endpoint-specific parameters.

| Parameter | Type      | Applies to    | Description                                                            | Example                 |
|-----------|-----------|---------------|------------------------------------------------------------------------|-------------------------|
| `fields`  | `string`  | any response  | Comma-separated list of fields to keep. Use dots for nested fields.    | `fields=id,position.x`. |
| `sort`    | `string`  | list response | Comma-separated sort keys. Prefix a key with `-` for descending order. | `sort=-delay,name`.     |
| `limit`   | `integer` | list response | Maximum number of entries to return.                                   | `limit=12`              |
| `offset`  | `integer` | list response | Number of entries to skip before `limit` is applied.                   | `offset=7`              |

When `limit` or `offset` is used, the response also carries `X-Total-Count`, `X-Offset` and `X-Limit` headers describing the full result set.

/// details | Example
    type: example

```
GET /crn/api/v1/trains?fields=id,name,speed&sort=-speed&limit=10
```
Returns the ten fastest trains, each reduced to its `id`, `name` and `speed`.
///