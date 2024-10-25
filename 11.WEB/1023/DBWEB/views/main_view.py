#------
#Flask Framework에서 모듈 단위 url 처리 파일
#-----

#모듈 로딩
from flask import Blueprint,render_template
from DBWEB.models.models import Question

#blueprint 인스턴스 생성
main_bp=Blueprint('MAIN',import_name=__name__,
                  url_prefix='/',
                  template_folder='templates')

#url 처리 라우팅 함수
@main_bp.route('/')
def index():
    return render_template('index.html',name='@dlrj_rlaudwn')

@main_bp.route('/qlist/')
def printList():
    #db에서 조회한 결과를 html 파일로 전달
    q_list=Question.query.all()
    return  render_template('question/question_list.html', question_list=q_list)

@main_bp.route('/qdetail/<int:question_id>')
def detail(question_id):
    #db에서 조회한 1개의 question 인스턴스를 html 파일로 전달
    question=Question.query.get(question_id)
    return  render_template('question_detail.html', question=question)