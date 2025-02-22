from fastapi import Request
from fastapi.responses import JSONResponse
from .exceptions import AppException

async def error_handler_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except AppException as e:
        return JSONResponse(
            status_code=400,
            content={"code": e.code, "message": e.message, "details": e.details}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"code": "internal_error", "message": str(e)}
        )
