import cv2
import random
import yaml

class JobApp:
    def __init__(self, config):
        self.options = config['options']
        self.question = config['question']
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        self.number = self.options[random.randint(0, len(self.options) - 1)]
        self.fsize = config['fsize']
        self.white = tuple(config['white'])
        self.black = tuple(config['black'])
        self.i = 0

    def put_text(self, img, x, y):
        rnum = self.options[random.randint(0, len(self.options) - 1)]
        cv2.putText(img, rnum, (x + 150, y - 50), cv2.FONT_ITALIC, self.fsize, self.white, 6)
        cv2.putText(img, rnum, (x + 150, y - 50), cv2.FONT_ITALIC, self.fsize, self.black, 2)

    def run(self):
        while True:
            _, img = self.cap.read()
            faces = self.face_cascade.detectMultiScale(img, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), self.black, 12)
                cv2.rectangle(img, (x, y), (x + w, y + h), self.white, 2)
                if self.i < 40:
                    cv2.putText(img, self.question, (x - 230, y - 30), cv2.FONT_ITALIC, 2, self.white, 6)
                    cv2.putText(img, self.question, (x - 230, y - 30), cv2.FONT_ITALIC, 2, self.black, 2)
                elif self.i > 40 and self.i < 130:
                    self.put_text(img, x - 230, y-50)
                else:
                    cv2.putText(img, self.number, (x - 230, y - 50), cv2.FONT_ITALIC, self.fsize, self.white, 6)
                    cv2.putText(img, self.number, (x - 230, y - 50), cv2.FONT_ITALIC, self.fsize, self.black, 2)
                self.i += 1
            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    app = JobApp(config)
    app.run()
