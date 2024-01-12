from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'  # 数据库文件名为votes.db
db = SQLAlchemy(app)

# 定义投票数据模型
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.String(100), nullable=False)

# 初始化数据库
#db.create_all()

# 首页
@app.route('/')
def index():
    return render_template('tou.html')

# 投票处理
@app.route('/vote', methods=['POST'])
def vote():
    option = request.form['option']
    if 'voted' not in request.cookies:
        # 如果用户未投过票，则记录cookie并保存投票数据
        vote = Vote(option=option)
        db.session.add(vote)
        db.session.commit()
        resp = jsonify(success=True)
        resp.set_cookie('voted', '1')
        return resp
    else:
        return jsonify(success=False, message='您已经投过票了')

# 获取投票数据
@app.route('/get_votes')
def get_votes():
    votes = Vote.query.all()
    options = {}
    total = len(votes)
    for vote in votes:
        if vote.option in options:
            options[vote.option] += 1
        else:
            options[vote.option] = 1
    return jsonify(options=options, total=total)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

