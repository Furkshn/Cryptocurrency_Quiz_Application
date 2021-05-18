

# ------------------------ Cryptocurrency Quiz Application ------------------------

import time
# Class Question

class Question():


    def __init__(self,text,choices,answer):

        self.text = text
        self.choices = choices
        self.answer = answer


    def chechAnswers(self,answer):

        if answer not in self.choices:
            raise ValueError("Hatalı Seçenek !!!")

        return  self.answer == answer



# Class Quiz

class Quiz():

    def __init__(self,questions):

        self.questions = questions
        self.questionIndex = 0
        self.score = 0


    def getQuestion(self):

        return  self.questions[self.questionIndex]    # Index numarasına göre index oluşur.


    def displayQuestion(self):

        question = self.getQuestion()

        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for options in question.choices:

            print("-" + options)

        print("")
        answer = input("Lütfen Cevabı Yazınız:")
        question.chechAnswers(answer)

        if (question.chechAnswers(answer)):   # Cevap True ise direk +1 olarak ekler.
            self.score += 1
            print("Tebrikler !!! Soruyu Doğru Cevapladınız.")

        self.questionIndex +=1

        self.loadQuestion()

    def loadQuestion(self):

        if len(self.questions) == self.questionIndex:
            self.displayScore()

        else:

            self.displayProgress()
            self.displayQuestion()


    def displayScore(self):

        print("\n" +"! Quiz Başarıyla Tamamlandı !".center(100,"*")+"\n")
        print(f"{len(self.questions)} sorunun {self.score} tanesini doğru cevapladınız.")
        print("")
        print(f" Quiz Skoru:{self.score}" .center(40,"*"))

    def displayProgress(self):

        totalQuestion = len(self.questions)
        numberQuestions = self.questionIndex + 1

        print(f"Toplam {totalQuestion} sorunun {numberQuestions}. sorusundasınız.".center(100,"*"))





while True:

    start_button = input("Quize Başlamak İçin Lütfen Herhangi Bir Tuşa Basınız :)" + "\n")

    q1 = Question("En Değerli Kripto Para Hangisidir ?",["Bitcoin","Ethereum","Avax","Litecoin","Dogecoin"],"Bitcoin")
    q2 = Question("Kripto Para Dünyasının Petrolü Olarak Adlandırılan Kripto Para Hangisidir ?",["Polkadot","Ethereum","Avax","Chainlink","Stellar"],"Ethereum")
    q3 = Question("Kripto Para Dünyasının Gümüşü Olarak Adlandırılan Kripto Para Hangisidir ?",["Uniswap","Cardano","Tether","Litecoin","Algorand"],"Litecoin")

    sorular = [q1,q2,q3]


    quiz = Quiz(sorular)


    print(quiz.displayQuestion())




    resolve_quiz = input("Quiz Uygulamasını Yeniden Çözmek İster Misiniz ? (E veya H)")

    if resolve_quiz == "H" or resolve_quiz == "h" or resolve_quiz == "Hayır" or resolve_quiz == "hayır":


        print("Quiz uygulamasından çıkılıyor...")
        time.sleep(0.5)
        print("Quiz uygulamasından çıkılıyor...")
        break

    elif resolve_quiz == "E" or resolve_quiz == "Evet" or resolve_quiz == "e" or resolve_quiz == "evet":

        print("Quiz uygulaması yeniden başlatılıyor...")
        time.sleep(0.5)
        continue

    else:

        print(" ! UYARI !")
        time.sleep(0.5)
        print("Lütfen Geçerli Bir Cevap Giriniz !" + "\n")
        time.sleep(1)








