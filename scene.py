Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from manim import *
... 
... 
... class CreateCircle(Scene):
...     def construct(self):
...         circle = Circle()  # create a circle
...         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
