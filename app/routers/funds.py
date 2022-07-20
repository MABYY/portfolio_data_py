from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy import null
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models , oauth2


router = APIRouter(prefix='/funds', tags=['Funds'])


@router.get('/')
def select_all_funds(db: Session = Depends(get_db),
        user_id: int = Depends(oauth2.get_current_user)):

    funds = db.query(models.Fund).all()
    return funds


@router.get('/select')
def select_fund(fund: schemas.FundSelect, db: Session = Depends(get_db),
                user_id: int = Depends(oauth2.get_current_user)):
    fund_select = db.query(models.Fund).filter(models.Fund.Nombre_Fondo == fund.Nombre_Fondo
                                                ).filter(models.Fund.Fecha == fund.Fecha)

    if not fund_select.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Fund {fund.Nombre_Fondo} on {fund.Fecha} was not found')
    else:
        return fund_select.first()


@router.post('/add', status_code=status.HTTP_201_CREATED)
def create_new_fund(fund: schemas.FundCreate,  db: Session = Depends(get_db)):

    add_fund = db.query(models.Fund).filter(
        models.Fund.Api == fund.Api).first()

    
    if not add_fund:
        new_fund = models.Fund(**fund.dict())
        db.add(new_fund)
        db.commit()
        db.refresh(new_fund)
        return new_fund
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"The API {fund.Api} is already taken")


@router.delete('/delete/{Api}')
def delete_fund(fund: schemas.FundCreate,  db: Session = Depends(get_db),
            user_id: int = Depends(oauth2.get_current_user)):

    delete_fund = db.query(models.Fund).filter(models.Fund.Api == fund.Api)
    if not delete_fund.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Api/Fund {fund.Api} {fund.Nombre_Fondo} was not found')
    else:
        delete_fund.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
