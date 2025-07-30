from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Create a security scheme using HTTP Bearer authentication (token in header)
security = HTTPBearer()
auth_router = APIRouter()

# This is a fake token for demonstration. In real apps, generate tokens dynamically.
FAKE_TOKEN = "secrettoken123"

# Dependency function to verify the token from the Authorization header
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Check if the provided token matches the expected token
    if credentials.credentials != FAKE_TOKEN:
        # If not, raise an HTTP 401 Unauthorized error
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing token")

# Endpoint for login (usually you would check username/password here)
@auth_router.post("/login")
def login():
    # For demo, just return the fake token. In real apps, validate user credentials and generate a token.
    return {"access_token": FAKE_TOKEN}