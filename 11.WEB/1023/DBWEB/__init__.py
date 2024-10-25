#-----------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명: app.py
#-----------------

#모듈 로딩
from flask import Flask

#db 관련 설정
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db=SQLAlchemy()
migrate=Migrate()       #db 컨트롤러


#사용자 정의 함수
def create_app():

    #전역변수
    # - Flask Web Server 인스턴스 생성
    APP=Flask(__name__)
    
    #db 관련 초기화 설정
    APP.config.from_object(config)


    #db 초기화 및 연동
    db.init_app(APP)
    migrate.init_app(APP,db)

    #db 클래스 정의 모듈
    from .models import models
    

    # #url(클라이언트 요청 페이지) 주소를 보여주는 기능의 함수
    # def printPage():
    #     return '<h1>하잉 😶‍🌫️</h1>'

    # #url 함수 연결
    # APP.add_url_rule('/',view_func=printPage,endpoint='INDEX')

    # #위의 단계를 한번해 해결하려면
    # @APP.route('/',endpoint='INDEX')
    # def printPage():
    #     return '<h1> 😶‍🌫️ 하잉 😶‍🌫️ </h1>'

    #url 처리 모듈 등록 - 블루프린트 관련
    from.views import main_view,answer_views
    APP.register_blueprint(main_view.main_bp)
    APP.register_blueprint(answer_views.ans_bp)

    return APP


#조건부 실행
if __name__ == '__main':
    #flask web server 구동
    app=create_app()
    app.run