from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from ..database import get_db
from .. import oauth2, schemas, models, utils

router = APIRouter(prefix='/auth', tags=['Authentication'])

# https://www.youtube.com/watch?v=0sOvCWFmrtA 7:08

@router.get('/users')
def login_user( db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):  
    users = db.query(models.User).all()
    return users


@router.get('/login', response_model= schemas.Token)
def login_user(user: OAuth2PasswordRequestForm = Depends(),  db: Session = Depends(get_db)):  
    login_user = db.query(models.User).filter(
                            models.User.email == user.username).first() 
    if not login_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"Invalid credentials")

    if not utils.verify(user.password, login_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                                detail=f"Invalid credentials ")
    else:
        access_token = oauth2.create_access_token(data ={'id': login_user.id})
        return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/register', status_code= status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate,  db: Session = Depends(get_db)):
    new_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not new_user:
        user.password = utils.hash(user.password)
        add_user = models.User(**user.dict())
        db.add(add_user)     
        db.commit()
        db.refresh(add_user)
        return add_user

    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                detail=f"User email {user.email} not valid")


@router.delete('/{id}')
def delete_user(id: int,  db: Session = Depends(get_db),
            user_id: int = Depends(oauth2.get_current_user)):  #protected route

    delete_user = db.query(models.User).filter(models.User.id == id)

    if not delete_user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                        detail = f'User not found')
    else:
        delete_user.delete(synchronize_session= False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)



