#-----------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명: app.py
#-----------------

#모듈 로딩
from flask import Flask, render_template

#사용자 정의 함수
def create_app():

    #전역변수
    # - Flask Web Server 인스턴스 생성
    APP=Flask(__name__)

    #라우팅 기능 함수
    # - @Flask Web Server 인스턴스 변수명.route('url')
    @APP.route('/')
    def index():
        # return '''<body style='background-color:#C0C4B6;'>
        #             <h1> Hello </h1>
        #         </body>'''
        return render_template('index.html')

    @APP.route('/info')
    @APP.route('/info/')
    def info():
        return'''<body style='backgroud-color: #AEAFB1; text-align: center;'
                    <h1> INFORMATION </h1>
                    </body>'''

    @APP.route('/info/<name>')
    def printInfo(name):
        # return f'''
        #         <body style='backgroud-color: #AEAFB1; text-align: center;'>
        #         <h1>{name} 상태</h1>
        #         흐아아아아ㅏㅏ앙ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ암
        #         </body>
        #         '''
        return render_template('info.html', name=name)

    @APP.route('/info/<int:age>')
    def checkAge(age):
        return f'''
                <body style='backgroud-color: #AEAFB1; text-align: center;'>
                <h1>나이: {age}</h1>
                흐아아아아ㅏㅏ앙ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ암
                </body>
                '''

    @APP.route('/go')
    def goHome():
        return APP.redirect('/')

    return APP


#조건부 실행
if __name__ == '__main':
    #flask web server 구동
    app=create_app()
    app.run