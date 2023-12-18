from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.models import OAuthFlowAuthorizationCode
from fastapi.security import OAuth2AuthorizationCodeBearer
from starlette.middleware import Middleware

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your specific needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted Host Middleware to validate the Host header
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# OAuth2 Authorization Code Bearer
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="token", authorizationUrl="authorize"
)

# Replace the authConfig with your specific configuration
auth_config = {
    "domain": "dev-onrbx061qhmexjpd.us.auth0.com",
    "audience": "https://api.hyprsol.com",
    "appOrigin": "http://localhost:3000",  # Adjust this to your specific needs
}

# Validation of auth_config
if not auth_config["domain"] or not auth_config["audience"] or auth_config["audience"] == "YOUR_API_IDENTIFIER":
    raise Exception(
        "Exiting: Please make sure that auth_config is in place and populated with valid domain and audience values"
    )

# Mock of the checkJwt function
async def check_jwt(token: str = Depends(oauth2_scheme)):
    # Replace this with your actual logic for checking JWT
    return token

# Endpoint for /api/external
@app.get("/api/external")
async def read_item(token: str = Depends(check_jwt)):
    return {"msg": "Your access token was successfully validated!"}

# Run the application using Uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3002, reload=True)  # Added 'reload=True' for auto-reloading during development
