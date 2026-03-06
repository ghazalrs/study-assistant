import os
from typing import Annotated
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt

bearer = HTTPBearer()


def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Security(bearer)],
) -> str:
    """Decode the NextAuth JWT and return the user_id."""
    try:
        payload = jwt.decode(
            credentials.credentials,
            os.environ["NEXTAUTH_SECRET"],
            algorithms=["HS256"],
        )
        user_id: str = payload.get("userId")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


CurrentUser = Annotated[str, Depends(get_current_user)]
