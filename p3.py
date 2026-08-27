students = []

"""ورودی نام و نمرات رو گرفتم"""
while True:
    name = input("enter your name(Whenever it's finished, write the exit):")
    if name.lower() == "exit":
        break
    score = float(input("enter your score:"))
    
    
    """یک دیکشنری برای ورودی ایجاد کردم و داخل لیست خالی قرار دادم"""
    student = {"name":name, "score":score}
    students.append(student)
    print("The student's name was successfully registered")
    
    
    """برای محاسبه میانگین ابتدا یه لیست خالی برای نمرات ایجاد کرم و نمرات رو جدا کردم بعد میانگین رو حساب کردم """
if len(students) > 0 :
    score = []
    for i in students:
        score.append(i["score"])   
    avg = sum(score)/len(score)
    
    
    """برای بدست اوردن دانش اموز برتر تابع تعریف کردم و نمرات رو سورت کردم"""
    def get_score(student):
        return student["score"]
    students.sort(key=get_score, reverse=True)
    print("Top Student is:", students[0]["name"])
    print("with a score of:", students[0]["score"])
