# Web Bot Authentication Skill

## Overview
This skill provides AI agents and automated clients with the required
authentication flow for accessing protected TriadicFrameworks API endpoints.
It defines how agents obtain tokens, how they refresh them, and how they
present credentials during API calls.

## Authentication Model
TriadicFrameworks uses a token-based authentication model. Agents must obtain
an access token before calling any protected API routes.

### Token Endpoint
POST /.well-known/auth/token

**Request**
Content-Type: application/json
{
  "client_id": "<agent-id>",
  "client_secret": "<agent-secret>"
}

**Response**
{
  "access_token": "<token>",
  "expires_in": 3600,
  "token_type": "Bearer"
}

### Using the Token
Include the token in the Authorization header:

Authorization: Bearer <access_token>

### Refreshing Tokens
POST /.well-known/auth/refresh

**Request**
{
  "refresh_token": "<refresh-token>"
}

**Response**
{
  "access_token": "<new-token>",
  "expires_in": 3600
}

## Error Responses
- 401 Unauthorized — Missing or invalid token  
- 403 Forbidden — Token lacks required scope  
- 429 Too Many Requests — Rate limit exceeded  

## Scopes
- read:docs  
- read:modules  
- read:canon  
- read:ideas  
- admin:site (restricted)

## Documentation
Additional authentication details are available at:
`/.well-known/Auth.md`

## Notes
This skill is intended for automated agents that need structured access to
TriadicFrameworks protected API endpoints.

