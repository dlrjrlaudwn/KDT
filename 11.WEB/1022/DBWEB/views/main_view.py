#------
#Flask Framework에서 모듈 단위 url 처리 파일
#-----

#모듈 로딩
from flask import Blueprint,render_template

#blueprint 인스턴스 생성
main_bp=Blueprint('MAIN',import_name=__name__,
                  url_prefix='/',
                  template_folder='templates')

#url 처리 라우팅 함수
@main_bp.route('/')
def index():
    return render_template('index.html')