from app import db


class Quiz(db.Model):
    '''
    Quiz model:
    - Contains of multiple questions
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    due_date_time = db.Column(db.DateTime())
    is_draft = db.Column(db.Boolean, default=True)

    classes = db.relationship('ClassCode', 'quiz_class', backref='quiz', lazy='dynamic')
    questions = db.relationship('Question', backref='quiz', lazy='dynamic')
     
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Question(db.Model):
    '''
    Question model:
    - Can have multiple answers (multiple choice)
    - Text input answer '''
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id', ondelete='CASCADE'))
    
    # reference to the answers
    multiple_choice_answers = db.relationship('MultipleChoiceAnswer', backref='question', lazy='dynamic')

    def __str__(self):
        return self.id


class MultipleChoiceAnswer(db.Model):
    '''
    '''
    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.Text, nullable=False)
    correct = db.Column(db.Boolean, default=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))


class QuizClass(db.Model):
    '''
    '''
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id', ondelete='CASCADE'))
    class_id = db.Column(db.Integer, db.ForeignKey('class_code.id', ondelete='CASCADE'))

