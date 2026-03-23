from manim import *


class OrnamentDemo(Scene):
    def construct(self):
        # 1. Створення фундаментальної області (мотиву) [1, 2]

        position_list = [
            [0, 0, 0],  #
            [0, 2, 0],  #
            [1, 0, 0]]

        # Використовуємо трикутник як базовий елемент орнаменту
        motif = Polygon(*position_list, color=PURPLE_B).set_fill(BLUE, opacity=0.8)
        self.add( motif)
        self.play(Create(motif))
        self.wait(1)

        # 2. Демонстрація паралельного перенесення (Translation - T) [4, 5]
        # Зсуваємо копію фігури вправо на певний вектор
        copy_t = motif.copy()
        self.play(copy_t.animate.shift(RIGHT * 2))
        self.wait(0.5)

        # 3. Демонстрація осьової симетрії (Reflection - V) [5, 6]
        # Створюємо дзеркальне відображення відносно вертикальної осі
        copy_v = copy_t.copy()
        self.play(copy_v.animate.flip(RIGHT))  # Віддзеркалення
        self.play(copy_v.animate.shift(RIGHT * 2))
        self.wait(1)

        # 4. Формування простого фризу (лінійного орнаменту) [3, 7]
        # Повторюємо ці дії для створення ряду
        ornament = VGroup(motif, copy_t, copy_v)
        full_row = VGroup()
        for i in range(-2, 3):
            full_row.add(ornament.copy().shift(RIGHT * i * 6))

        self.play(FadeOut(motif, copy_t, copy_v))
        self.play(Create(full_row))
        self.play(full_row.animate.scale(0.6))
        self.wait(2)