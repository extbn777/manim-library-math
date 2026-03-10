from manim import *


class PresentacionIngles(Scene):
    """Parte 1 (~60s): presentación frente a cámara."""

    def construct(self):
        titulo = Text("Part 1 - Presentation in English", font_size=44, color=BLUE)
        self.play(FadeIn(titulo, shift=UP), run_time=1.2)
        self.wait(0.8)
        self.play(titulo.animate.to_edge(UP), run_time=0.8)

        script = [
            ("0-6 s", '"Hello, Teacher Luz Azucena."', 6),
            ("6-12 s", '"My name is Esteban Rafael Fontanilla Ramirez."', 6),
            ("12-18 s", '"I am studying Systems Engineering."', 6),
            (
                "18-24 s",
                '"I decided to study this because I am very interested in software development and creating technological solutions."',
                6,
            ),
            (
                "24-60 s",
                '"My experience with application exercises has allowed me to understand that integral calculus can be used to model a wide range of scientific processes, it is applicable to various professions, and contributes to solving real world problems."',
                8,
            ),
        ]

        active = None
        for tramo, texto, espera in script:
            bloque = VGroup(
                Text(tramo, font_size=24, color=YELLOW),
                Paragraph(texto, font_size=30, line_spacing=0.78).scale_to_fit_width(config.frame_width - 1.2),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(titulo, DOWN, buff=0.55)

            if active is None:
                self.play(FadeIn(bloque, shift=UP * 0.2), run_time=0.8)
            else:
                self.play(ReplacementTransform(active, bloque), run_time=0.65)

            active = bloque
            self.wait(espera)

        cierre = Text("Target duration: about 1 minute", font_size=28, color=GREY_B)
        cierre.to_edge(DOWN)
        self.play(FadeIn(cierre), run_time=0.6)
        self.wait(2)


class ExplicacionEspanolPizarra(Scene):
    """Parte 2: estilo pizarra, paso a paso."""

    def construct(self):
        # Fondo tipo pizarra
        fondo = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            fill_color="#1E3A2F",
            stroke_width=0,
        )
        self.add(fondo)

        titulo = Text("Parte 2 - Explicación en Español", font_size=40, color=WHITE)
        titulo.to_edge(UP)
        subtitulo = Text("Ejercicio D: Volumen de agua bombeada", font_size=30, color=TEAL_A)
        subtitulo.next_to(titulo, DOWN, buff=0.15)
        self.play(Write(titulo), FadeIn(subtitulo, shift=UP * 0.2), run_time=1.3)

        marco = RoundedRectangle(
            corner_radius=0.12,
            width=config.frame_width - 1,
            height=config.frame_height - 2.2,
            stroke_color=WHITE,
            stroke_width=2,
            fill_opacity=0.08,
            fill_color=BLACK,
        ).next_to(subtitulo, DOWN, buff=0.28)
        self.play(Create(marco), run_time=0.9)

        linea_actual = VGroup()

        def write_step(narracion: str, formula: Mobject, wait_s: float = 3.0):
            nonlocal linea_actual
            narr = Paragraph(narracion, font_size=29, line_spacing=0.8, color=WHITE)
            narr.scale_to_fit_width(marco.width - 0.8)
            contenido = VGroup(narr, formula).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            contenido.move_to(marco.get_center())
            if len(linea_actual) == 0:
                self.play(FadeIn(contenido, shift=UP * 0.2), run_time=1.0)
            else:
                self.play(ReplacementTransform(linea_actual, contenido), run_time=0.9)
            linea_actual = contenido
            self.wait(wait_s)

        write_step(
            "Voy a sustentar el ejercicio de aplicación sobre el volumen de agua bombeada.\n"
            "La razón de extracción es R(t)=6+2sen(t) litros por segundo y se pide el total en 10 segundos.",
            MathTex(r"R(t)=6+2\sin(t)", font_size=58, color=YELLOW),
            wait_s=4,
        )

        write_step(
            "Para hallar el volumen total, planteamos una integral definida entre 0 y 10 segundos.",
            MathTex(r"V=\int_{0}^{10}(6+2\sin(t))\,dt", font_size=62, color=YELLOW),
            wait_s=4,
        )

        write_step(
            "Calculamos la antiderivada: integral de 6 es 6t e integral de 2sen(t) es -2cos(t).",
            MathTex(r"V=\left[6t-2\cos(t)\right]_{0}^{10}", font_size=62, color=YELLOW),
            wait_s=4,
        )

        write_step(
            "Evaluamos con el Teorema Fundamental del Cálculo: valor en 10 menos valor en 0.",
            MathTex(r"V=(6(10)-2\cos(10))-(6(0)-2\cos(0))", font_size=56, color=YELLOW),
            wait_s=4,
        )

        resultado = VGroup(
            Text("Calculadora en radianes", font_size=30, color=TEAL_A),
            MathTex(r"V=(60-2(-0.839))-(0-2(1))", font_size=52, color=WHITE),
            MathTex(r"V=61.678-(-2)", font_size=52, color=WHITE),
            MathTex(r"V\approx 63.678\ \text{litros}", font_size=62, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        resultado.move_to(marco.get_center())

        self.play(ReplacementTransform(linea_actual, resultado), run_time=1.0)
        self.wait(5)


class DespedidaIngles(Scene):
    def construct(self):
        titulo = Text("Part 3 - Closing", font_size=46, color=BLUE)
        frase = Text('"Goodbye, thank you for your attention."', font_size=40)
        self.play(FadeIn(titulo, shift=UP * 0.3), run_time=0.8)
        self.play(titulo.animate.to_edge(UP), run_time=0.6)
        self.play(Write(frase), run_time=1.2)
        self.wait(3)


class VideoCompleto(Scene):
    """Escena guía de estructura total."""

    def construct(self):
        portada = VGroup(
            Text("Guion de Video - Cálculo Integral", font_size=50, color=BLUE),
            Text("Máximo 8 minutos", font_size=34, color=YELLOW),
        ).arrange(DOWN, buff=0.35)
        self.play(FadeIn(portada, shift=UP * 0.2), run_time=1.0)
        self.wait(1.4)
        self.play(FadeOut(portada), run_time=0.7)

        checklist = VGroup(
            Text("1) Preséntate en inglés mirando a cámara (~1 min)", font_size=32),
            Text("2) Explica en español en tablero/hoja (ejercicio D)", font_size=32),
            Text("3) Cierra en inglés mirando a cámara", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        self.play(LaggedStart(*[FadeIn(x, shift=RIGHT * 0.2) for x in checklist], lag_ratio=0.2), run_time=1.6)
        self.wait(2.2)

        tip = Text("Consejo: deja pausas breves para respirar y señalar operaciones.", font_size=28, color=GREEN)
        tip.to_edge(DOWN)
        self.play(FadeIn(tip), run_time=0.8)
        self.wait(2.5)
