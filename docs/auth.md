# Auth.md

## Overview
TriadicFrameworks APIs use token-based authentication. Agents must obtain a
token before accessing protected endpoints.

## agent_auth
skill: "auth-md"
register_uri: "/agent/register"

methods:
  - type: "anonymous"
    description: "Agents may register anonymously to obtain a token."
    credential_types_supported: ["none"]
    claim_uri: "/agent/register"

## Token Endpoint
POST /.well-known/auth/token

### Request
Content-Type: application/json
{
  "client_id": "...",
  "client_secret": "..."
}

### Response
{
  "access_token": "...",
  "expires_in": 3600,
  "token_type": "Bearer"
}

## Using the Token
Include the token in the Authorization header:

Authorization: Bearer <access_token>

## Refreshing Tokens
POST /.well-known/auth/refresh

### Request
{
  "refresh_token": "..."
}

### Response
{
  "access_token": "...",
  "expires_in": 3600
}

## Error Responses
401 Unauthorized – Missing or invalid token  
403 Forbidden – Token lacks required scope  
429 Too Many Requests – Rate limit exceeded

## Scopes
- read:docs  
- read:modules  
- read:canon  
- read:ideas  
- admin:site (restricted)
